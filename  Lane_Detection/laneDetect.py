import cv2
import numpy as np

vertices=np.array([[0,360], [0,250],[274,165],[355,165],[570,250],[640,0]]) 

def roi(img, vertices):
    mask=np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked=cv2.bitwise_and(img, mask)
    return masked

# '''CANNY EDGE DETECTION WITH GAUSSIAN BLUR'''

img = cv2.imread('solidWhiteCurve.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,200,300,apertureSize = 3)
blur = cv2.GaussianBlur(img,(5,5), 0)

img1 = roi(edges,[vertices])

'''HOUGH TRANSFORMATION'''
minLineLength = 100
maxLineGap = 2
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
for x1,y1,x2,y2 in lines[0]:
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),8)



cv2.imshow('newImage',img1)
cv2.waitKey(0)

