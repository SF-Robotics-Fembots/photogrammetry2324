#land test
#libraries
import numpy as np
import cv2
import math
from PIL import Image, ImageFilter
import matplotlib.pyplot as plt

# image = cv2.imread("C:/Users/rosar/Pictures/bloopbloop.jpeg")
# cv2.imshow("image", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# #cv2.resize(image, (400, 325))
# #img_75 = cv2.resize(image, None, fx = 0.75, fy = 0.75)

# #resizing
# image = cv2.imread('C:/Users/rosar/Pictures/bloopbloop.jpeg', cv2.IMREAD_UNCHANGED)
# print('Original Dimensions : ',image.shape)
# width = 380
# height = 450
# dim = (width, height)
# resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
# print('Resized Dimensions : ',resized.shape)
# #cv2.imshow("Resized image", resized)

# rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
# rotated_resized = cv2.resize(rotated_image, dim, interpolation = cv2.INTER_AREA)
# #cv2.imshow("Rotated and resized image", rotated_resized)

# line_image = cv2.line(rotated_resized, (100, 210), (155, 210), (0, 0, 255), 10) 
# #cv2.imshow('with 1 bar', line_image)

# two_bars = cv2.line(line_image, (210, 210), (265, 210), (0, 0, 255), 10)
# cv2.imshow('with 2 bars', two_bars)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


#enter the number of pixels for the 32 cm area
pixelsthirtytwo = float(input("pixels 32 cm area: "))

#get the px per cm
ppcm = float(pixelsthirtytwo/32)

#pixels for the different sides
ppx = float(input("pixels left side (x): "))
ppy = float(input("pixels right side (y): "))
ppz = ppx + ppy + pixelsthirtytwo

#calculations
cmz = ppz/ppcm
print("The width is: " + str(cmz) + "cm")

#get the pixels for the height
pph = float(input("pixels height (top of coral to bottom): "))

#calculations pt. 2
cmh = pph/(ppz*ppcm)

print("The height is: " + str(cmh) + "cm")

