import cv2
import numpy as np
import math
from scipy import ndimage

#from matplotlib import pyplot as plt

img = cv2.imread('run21.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray= cv2.bilateralFilter(gray,7,40,40)
gray = cv2.Canny(gray,100,300,3)
kernel = np.ones((5,5),np.uint8)
# gray= cv2.dilate(gray,kernel,iterations = 2)
#(thresh, bw) = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
#print('type gray',type(gray))
print('gray',gray)
print(gray.shape)


# def var(im):
  # varianceMatrix = np.zeros(im.shape,np.uint8)
  # w = 1          # the radius of pixels neighbors 
  # rows = len(im)
  # columns = len(im[0])


  # for i in range(w,columns-w):
  #     for j in range(w,rows-w):
  #       sampleframe = []
  #       for k in range (-1,2):
        
  #           sampleframe.append(im[j-w:j+w, i+k-w:i+k+w])
  #           print("sampleframe",sampleframe)
  #       variance    = np.var(sampleframe[0])
  #       print(variance)
  #       if (math.isnan(variance) == False):
  #         varianceMatrix[j][i] = int(variance)

varianceMatrix = ndimage.generic_filter(gray, np.var, size = 3)

  # return varianceMatrix


print ('varianceMatrix',varianceMatrix)
# variance=var(gray)
# print ('varinace',variance)
variance= varianceMatrix
(thresh, edges) = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

print ('edges bw',edges)
print(edges.shape)

#edges=edges[edges > 240]
#print ('edges',edges)
#print(edges.shape)
gray1=gray[:][:]
x,y=gray1.shape
#print ('gray1',gray1)
#print(gray1.shape)

for i in range(x):
  for j in range(y):
    if (variance[i,j] < 100):
      gray1[i,j]=0.0
      
      
#1) what to do here 0 or what
#2) try parallel after that

lines = cv2.HoughLines(gray1,1,np.pi/720,35)
# 57 all filles and on 58 no lines ????
print('lines',lines)
print(lines.shape)

for i in range(len(lines)-1):
        if (np.abs(lines[i][0][1]-lines [i+1][0][1]) <=0.5 and np.abs(lines[i][0][0])>5):
          rho,theta=lines[i][0]
          a = np.cos(theta)        
          b = np.sin(theta)
          x0 = a*rho
          y0 = b*rho
          x1 = int(x0 + 900*(-b))
          y1 = int(y0 + 900*(a))
          x2 = int(x0 - 900*(-b))
          y2 = int(y0 - 900*(a))
                                  
          cv2.line(img,(x1,y1),(x2,y2),(0,0,255),1)


# for line in lines:
#         rho, theta = line[0]
#         a = np.cos(theta)        
#         b = np.sin(theta)
#         x0 = a*rho
#         y0 = b*rho
#         x1 = int(x0 + 900*(-b))
#         y1 = int(y0 + 900*(a))
#         x2 = int(x0 - 900*(-b))
#         y2 = int(y0 - 900*(a))

#         cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
            
           

        




cv2.imwrite('canny.jpg',edges)
cv2.imwrite('s.jpg',img)