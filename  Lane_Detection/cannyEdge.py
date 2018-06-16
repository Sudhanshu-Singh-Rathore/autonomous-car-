import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('neural.png',1)
edges = cv2.Canny(img,100,150)
edges1=cv2.GaussianBlur(edges, (5,5), 0)  
# plt.subplot(121),plt.imshow(img,cmap = 'gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# # resized_image = cv2.resize(edges, (100, 50)) 	
# plt.subplot(122),plt.imshow(edges,cmap = 'gray')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

# plt.show()

cv2.imshow('edges',edges)
cv2.waitKey(0)