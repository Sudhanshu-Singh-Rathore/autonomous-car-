import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2
import math

global avgLeft,avgRight
def perp( a ) :
    b = np.empty_like(a)
    b[0] = -a[1]
    b[1] = a[0]
    return b

def seg_intersect(a1,a2, b1,b2):
    da = a2-a1
    db = b2-b1
    dp = a1-b1
    dap = perp(da)
    denom = np.dot( dap, db)
    num = np.dot( dap, dp )
    return (num / denom.astype(float))*db + b1

def movingAverage(avg, new_sample, N=20):
    if (avg == 0):
        return new_sample
    avg -= avg / N;
    avg += new_sample / N;
    return avg;

def grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
def canny(img, low_threshold, high_threshold): 
    return cv2.Canny(img, low_threshold, high_threshold)

def gaussian_blur(img, kernel_size): 
    return cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)

def region_of_interest(img, vertices):
    
    mask = np.zeros_like(img)   
    
    if len(img.shape) > 2:
        channel_count = img.shape[2]  # i.e. 3 or 4 depending on your image
        ignore_mask_color = (255,) * channel_count
    else:
        ignore_mask_color = 255
        
    cv2.fillPoly(mask, vertices, ignore_mask_color)    
    
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image

def draw_lines(img, lines, color=[0, 0, 255], thickness=2):
    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(img, (x1, y1), (x2, y2), color, thickness)
    return img 

# def hough_lines(img, rho, theta, threshold, min_line_len, max_line_gap):
#     """
#     `img` should be the output of a Canny transform.
        
#     Returns an image with hough lines drawn.
#     """
#     lines = cv2.HoughLinesP(img, rho, theta, threshold, np.array([]), minLineLength=min_line_len, maxLineGap=max_line_gap)

#     lines_image = np.zeros((img.shape, 3), dtype=np.uint8)
#     draw_lines(lines_image, lines)
#     return lines_image 

#Main program
img=cv2.imread('solidWhiteCurve.jpg')
gray=grayscale(img)
canEdge=canny(img,100,150)
blur=gaussian_blur(canEdge,11)


xsize = img.shape[1]
ysize = img.shape[0]
dx1 = int(0.0425 * xsize)
dx2 = int(0.425 * xsize)
dy = int(0.6 * ysize)

vertices = np.array([[(dx1, ysize), (dx2, dy), (xsize - dx2, dy), (xsize - dx1, ysize)]], dtype=np.int32)


regionInterestImage = region_of_interest(blur, vertices)

minLineLength = 100
maxLineGap = 2
lines = cv2.HoughLinesP(regionInterestImage,1,np.pi/180,100,minLineLength,maxLineGap)



line_image = draw_lines(img, lines, [0, 0, 255], 2)
# final_image=weighted_image(regionInterestImage, img)

cv2.imshow('GoodImage', blur)
cv2.waitKey(0)

