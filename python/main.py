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
from Bayessian_matte1 import Bayesian_Matte1
from change_background import change_background
import time
import psutil

start_time = time.time()
picture_number = 'GT01'
trimap_level = 'lowers/'
trimap_arrea = 'Trimap1/'

trimap_name = trimap_level + 'trimap/' + trimap_arrea + picture_number + '.png'
img_trimap = read_Trimap(trimap_name)

img_name = trimap_level + 'input/' + picture_number + '.png'
img_input = read_image(img_name)

##
# output_alpha = cv2.imread('image1/output_alpha.png')
# output_alpha = change_SameColorform(output_alpha)
# output_alpha = change_Size(output_alpha)
##

output_alpha, unknow = Bayesian_Matte1(img_input, img_trimap)
plt.imshow(output_alpha, cmap="gray")
plt.show()
# a = output_alpha.dtype
# max_value = np.amax(output_alpha)
# print(max_value)
# nan_locs = np.isnan(output_alpha)
# print(np.argwhere(nan_locs))


output_alpha = change_SameColorform(output_alpha)
output_alpha = change_Size(output_alpha)
# a = output_alpha.dtype
# max_value = np.amax(output_alpha)
# print(a)


# print(output_alpha.shape)
output_name = trimap_level + picture_number + '.png'
img_uint8 = (output_alpha * 255).astype(np.uint8)
cv2.imwrite(output_name, img_uint8)


alpha_name = trimap_level + 'groundtruth/' + picture_number + '.png'
alpha_ground = cv2.imread(alpha_name)
# print(alpha_ground.shape)
alpha_ground = change_SameColorform(alpha_ground)
alpha_ground = change_Size(alpha_ground)
print(alpha_ground.shape)

MSE = MSE_calculation(output_alpha, alpha_ground)
print("The MSE of our output = ", MSE)
PSNR = PSNR_calculation(output_alpha, alpha_ground)
print("The PSNR of our output = ", PSNR)
SAD = SAD_calculation(output_alpha, alpha_ground)
print("The SAD of our output = ", SAD)


background_input = cv2.imread('background.jpg')
background_input = change_SameColorform(background_input)
background_input = change_background(img_input, background_input)

img_new = combining(output_alpha, background_input, img_input)
# a = img_new.dtype
# max_value = np.amax(img_new)
# print(a)
cv2.imshow('Composite Image', img_new)
cv2.waitKey(0)
img_uint8 = (img_new * 255).astype(np.uint8)
combining_name = trimap_level + 'combining/' + picture_number + '.png'
cv2.imwrite('combining_name', img_uint8)


if __name__ == "__main__":
    pid = psutil.Process().pid
    memory_info = psutil.Process(pid).memory_info()
    print("Memory usage of the main program:：")
    print(f"RSS（resident set size）：{memory_info.rss / 1024 / 1024:.2f} MB")
    print(f"VMS（virtual memory set）：{memory_info.vms / 1024 / 1024:.2f} MB")

end_time = time.time()
run_time = end_time - start_time
print("Running time：", run_time, "s")
print("Done")
