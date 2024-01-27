#land test
#libraries
import numpy as np
import cv2
import math
from PIL import Image, ImageFilter
import matplotlib.pyplot as plt

image = cv2.imread("C:/Users/rosar/Pictures/bloopbloop.jpeg")
cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
#cv2.resize(image, (400, 325))
#img_75 = cv2.resize(image, None, fx = 0.75, fy = 0.75)

#resizing
image = cv2.imread('C:/Users/rosar/Pictures/bloopbloop.jpeg', cv2.IMREAD_UNCHANGED)
print('Original Dimensions : ',image.shape)
width = 380
height = 450
dim = (width, height)
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
print('Resized Dimensions : ',resized.shape)
#cv2.imshow("Resized image", resized)

rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
rotated_resized = cv2.resize(rotated_image, dim, interpolation = cv2.INTER_AREA)
#cv2.imshow("Rotated and resized image", rotated_resized)

line_image = cv2.line(rotated_resized, (100, 210), (155, 210), (0, 0, 255), 10) 
#cv2.imshow('with 1 bar', line_image)

two_bars = cv2.line(line_image, (210, 210), (265, 210), (0, 0, 255), 10)
cv2.imshow('with 2 bars', two_bars)

cv2.waitKey(0)
cv2.destroyAllWindows()


#variables
ppmm = 5.855555

#ppmm means pixels per mm
pixels = 0
mm = 0.00

pixels = int(input("num of pix: "))

#calculations
mm = pixels/ppmm
print(str(mm) + " mm")

#finding total width 
#zpixels = 0

#ask for input on zpixels
#zpixels = int(input("num of zpixels: "))

#calculations on total width
