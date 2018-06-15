import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2
import math

def regionOfInterest(img,vertices):
	mask =np.zeros_like(img)

	if len(img.shape)>2:
		channel_count=img.shape[2]
		ignoreMaskColor=(255,)*channel_count
	else:
		ignoreMaskColor=255

	cv2.fillPoly(mask,vertices,ignoreMaskColor)
	masked_image=cv2.bitwise_and(img,mask)
	return masked_image

def draw_lines(img, lines, color=[0, 0, 255], thickness=2):
    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(img, (x1, y1), (x2, y2), color, thickness)
    return img 


cap=cv2.VideoCapture('solidWhiteRight.mp4')


while(1):
	ret, frame=cap.read()
	gray=cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
	edges=cv2.Canny(gray,500,550)
	blur=cv2.GaussianBlur(edges,(11,11),0)
	ysize=frame.shape[0]
	xsize=frame.shape[1]
	# vertices=np.array([[ [3*width/2, 2*height/3], [width/10, 2*height/8], [40, height],[width - 40, height]]], dtype=np.int32)
    # xsize = frame.shape[1]
    # ysize = frame.shape[0]

	dx1 =int(0.0725*xsize)
	dx2 =int(0.425*xsize)
	dy =int(0.6*ysize)

	vertices = np.array([[(dx1, ysize), (dx2, dy), (xsize-dx2, dy), (xsize-dx1, ysize)]], dtype=np.int32)

	regionOfInterestImage=regionOfInterest(blur,vertices)

	minLineLength=100
	maxLineGap=2
	lines=cv2.HoughLinesP(regionOfInterestImage,1,np.pi/4,100,10,1)
	line_image = draw_lines(frame, lines, [0, 0, 255], 2)



	# cv2.imshow('Edges', edges)
	cv2.imshow('Lines', line_image)
	

	if cv2.waitKey(10)&0xff==ord('q'):
		break


