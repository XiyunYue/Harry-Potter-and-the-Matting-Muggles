from read_Trimap import read_Trimap
from read_image import read_image
import numpy as np
from Quality_Inspection import MSE_calculation, PSNR_calculation, SAD_calculation
from combining import combining
import cv2
from change_SameColorform import change_SameColorform
from Laplacian import Laplacian_matting
from change_Size import change_Size

trimap_name = 'image16/trimap.png'
img_trimap = read_Trimap(trimap_name)

img_name = 'image16/input.png'
img_input = read_image(img_name)

alpha_ground = cv2.imread('image16/groundtruth.png')
alpha_ground = change_SameColorform(alpha_ground)
alpha_ground = change_Size(alpha_ground)

background_input = cv2.imread('image16/background.jpg')
background_input = change_SameColorform(background_input)


Laplacian_alpha = Laplacian_matting(img_trimap, img_input)

MSE = MSE_calculation(Laplacian_alpha, alpha_ground)
print("The MSE of our output = ", MSE)
PSNR = PSNR_calculation(MSE)
print("The PSNR of our output = ", PSNR)
SAD = SAD_calculation(Laplacian_alpha, alpha_ground)
print("The SAD of our output = ", SAD)

img_Laplacian = combining(Laplacian_alpha, background_input, img_input)
cv2.imshow('Composite Image', img_Laplacian)
cv2.waitKey(0)
print("Done")
