#land test
#libraries
import math

#variables
ppmm = 5.855555
#ppmm means pixels per mm
pixels = 0
mm = 0.00

pixels = int(input("num of pix: "))

#calculations
mm = pixels/ppmm
print(str(mm) + " mm")