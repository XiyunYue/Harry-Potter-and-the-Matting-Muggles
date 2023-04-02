# Copyright 2023 by Xiaoru Liu, Trinity College Dublin. All rights reserved.
#
# This file is the main code for using Bayes method for matting
# ==================================================
"Run this can get the Bayes matting result"

from read_Trimap import read_Trimap
from read_image import read_image
from Quality_Inspection import MSE_calculation, PSNR_calculation, SAD_calculation
from combining import combining
import cv2
import numpy as np
import matplotlib.pyplot as plt
from change_SameColorform import change_SameColorform
from change_Size import change_Size
from main_Bayesian import bayesian_matte
from change_background import change_background

trimap_name = 'image2/trimap.png'
img_trimap = read_Trimap(trimap_name)

img_name = 'image2/input.png'
img_input = read_image(img_name)

##
# output_alpha = cv2.imread('image2/output_alpha.png')
# output_alpha = change_SameColorform(output_alpha)
# output_alpha = change_Size(output_alpha)
##

output_alpha = bayesian_matte(img_input, img_trimap)
plt.imshow(output_alpha, cmap = "gray")
plt.show()
# a = output_alpha.dtype
# max_value = np.amax(output_alpha)
# print(max_value)
nan_locs = np.isnan(output_alpha)
print(np.argwhere(nan_locs))


output_alpha = change_SameColorform(output_alpha)
output_alpha = change_Size(output_alpha)
# a = output_alpha.dtype
# max_value = np.amax(output_alpha)
# print(a)


print(output_alpha.shape)
img_uint8 = (output_alpha * 255).astype(np.uint8)
cv2.imwrite('image2/output_alpha.png', img_uint8)

alpha_ground = cv2.imread('image2/groundtruth.png')
# print(alpha_ground.shape)
alpha_ground = change_SameColorform(alpha_ground)
alpha_ground = change_Size(alpha_ground)
print(alpha_ground.shape)

MSE = MSE_calculation(output_alpha, alpha_ground)
print("The MSE of our output = ", MSE)
PSNR = PSNR_calculation(MSE)
print("The PSNR of our output = ", PSNR)
SAD = SAD_calculation(output_alpha, alpha_ground)
print("The SAD of our output = ", SAD)


background_input = cv2.imread('background.jpg')
background_input = change_SameColorform(background_input)
background_input = change_background(img_input, background_input)

img_new = combining(output_alpha, background_input, img_input)
a = img_new.dtype
max_value = np.amax(img_new)
print(a)
cv2.imshow('Composite Image', img_new)
cv2.waitKey(0)
img_uint8 = (img_new * 255).astype(np.uint8)
cv2.imwrite('image2/combining_image.png', img_uint8)

print("Done")
