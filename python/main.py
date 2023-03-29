from test_Trimap import test_Trimap
import numpy as np
from MSE import MSE_calculation
from combining import combining
import cv2
from test_SameSize import test_SameSize
from change_SameColorform import change_SameColorform
from test_alpha import test_alpha
import scipy.special
from Laplacian import Laplacian_matting



img_trimap = cv2.imread('trimap.png')
img_trimap = change_SameColorform(img_trimap)
a, img_trimap = test_Trimap(img_trimap)
print(a)

img_input = cv2.imread('input.png')
img_input = change_SameColorform(img_input)

b = test_SameSize(img_trimap, img_input)
print("Size of trimap and input image are", b)

##
output_alpha = cv2.imread('output_alpha.png')###
output_alpha = change_SameColorform(output_alpha)
c, output_alpha = test_alpha(output_alpha)
print(c)
d = test_SameSize(output_alpha, img_trimap)
print("Size of output alpha and trimap are", d)

e = MSE_calculation(output_alpha)
print("The MSE of our output = ", e)

background_input = cv2.imread('background.png')
background_input = change_SameColorform(background_input)
f = test_SameSize(output_alpha, background_input)
print("Size of output alpha and background are", f)


Laplacian_alpha = Laplacian_matting(img_trimap, img_input)
# a = Laplacian_alpha.dtype
# max_value = np.amax(Laplacian_alpha)
# print(max_value)


g = test_SameSize(Laplacian_alpha, background_input)

print("Size of Laplacian alpha and background are", g)

img_new = combining(Laplacian_alpha, background_input, img_input)

cv2.imshow('Composite Image', img_new)
cv2.waitKey(0)