import cv2
import numpy as np

vertices=np.array([[0,360], [0,300],[160,300],[380,400],[300,640],[800,600]]) 

def roi(img, vertices):
    mask=np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked=cv2.bitwise_and(img, mask)
    return masked


img = cv2.imread('road-generic.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,400,500,apertureSize = 3)
# roi = roi(edges, vertices)

lines = cv2.HoughLines(edges,1,np.pi/180,200)
for rho,theta in lines[0]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))

        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),4) 

cv2.imshow('newImage', img)
cv2.waitKey(0)