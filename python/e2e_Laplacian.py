from test_Trimap import test_Trimap
import numpy as np
from Quality_Inspection import MSE_calculation, PSNR_calculation
from combining import combining
import cv2
from test_SameSize import test_SameSize
from change_SameColorform import change_SameColorform
from test_alpha import test_alpha
from Laplacian import Laplacian_matting

img_trimap = cv2.imread('trimap.png')
img_trimap = change_SameColorform(img_trimap)
a, img_trimap = test_Trimap(img_trimap)
print(a)

img_input = cv2.imread('input.png')
img_input = change_SameColorform(img_input)

b = test_SameSize(img_trimap, img_input)
print("Size of trimap and input image are", b)

alpha_ground = cv2.imread('groundtruth.png')
alpha_ground = change_SameColorform(alpha_ground)
ndim_alpha = alpha_ground.ndim
if ndim_alpha == 3:
    alpha_ground = alpha_ground[:, :, 0]

background_input = cv2.imread('background.png')
background_input = change_SameColorform(background_input)

Laplacian_alpha = Laplacian_matting(img_trimap, img_input)
g = test_SameSize(Laplacian_alpha, background_input)
print("Size of Laplacian alpha and background are", g)

h = MSE_calculation(Laplacian_alpha, alpha_ground)
print("The MSE of Laplacian = ", h)
c = PSNR_calculation(h)
print("The PSNR of Laplacian = ", c)

img_Laplacian = combining(Laplacian_alpha, background_input, img_input)


print("Done")
