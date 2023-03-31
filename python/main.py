from read_Trimap import read_Trimap
from read_image import read_image
from Quality_Inspection import MSE_calculation, PSNR_calculation, SAD_calculation
from combining import combining
import cv2
from change_SameColorform import change_SameColorform
from change_Size import change_Size
from main_Bayesian import bayesian_matte

trimap_name = 'image16/trimap.png'
img_trimap = read_Trimap(trimap_name)

img_name = 'image16/input.png'
img_input = read_image(img_name)

##
# output_alpha = cv2.imread('output_alpha.png')
# output_alpha = change_SameColorform(output_alpha)
# output_alpha = change_Size(output_alpha)
##

output_alpha = bayesian_matte(img_input, img_trimap)
output_alpha = change_SameColorform(output_alpha)
output_alpha = change_Size(output_alpha)

alpha_ground = cv2.imread('image16/groundtruth.png')
alpha_ground = change_SameColorform(alpha_ground)
alpha_ground = change_Size(alpha_ground)


MSE = MSE_calculation(output_alpha, alpha_ground)
print("The MSE of our output = ", MSE)
PSNR = PSNR_calculation(MSE)
print("The PSNR of our output = ", PSNR)
SAD = SAD_calculation(output_alpha, alpha_ground)
print("The SAD of our output = ", SAD)

background_input = cv2.imread('background.png')
background_input = change_SameColorform(background_input)


img_new = combining(output_alpha, background_input, img_input)
cv2.imshow('Composite Image', img_new)
cv2.waitKey(0)
print("Done")
