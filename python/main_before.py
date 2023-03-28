from test_Trimap import test_Trimap
import numpy as np
from MSE import MSE_calculation
from combining import combining
import cv2
from test_SameSize import test_SameSize
from change_SameColorform import change_SameColorform
from test_alpha import test_alpha


img_trimap = cv2.imread('trimap.png')
img_trimap = change_SameColorform(img_trimap)
a, trimap = test_Trimap(img_trimap)
print(a)

# ndim = image.ndim
# if ndim == 3:
#     image = image[:,:,0]
# a = img_trimap.dtype
# max_value = np.amax(img_trimap)
# print(a)
img_input = cv2.imread('input.png')
img_input = change_SameColorform(img_input)
# trimap_array = cv2.imread(img_trimap)

b = test_SameSize(img_trimap, img_input)
print("Size of trimap and input image are", b)

##
output_alpha = cv2.imread('output_alpha.png')###
output_alpha = change_SameColorform(output_alpha)
c, output_alpha = test_alpha(output_alpha)
print(c)
d = test_SameSize(output_alpha, img_trimap)
print("Size of output alpha and trimap are", d)

# a = output_alpha.dtype
# max_value = np.amax(output_alpha)
# print(max_value)

e = MSE_calculation(output_alpha)
print(e)

background_input = cv2.imread('background.png')
background_input = change_SameColorform(background_input)
f = test_SameSize(output_alpha, background_input)
print("Size of output alpha and trimap are", f)
img_new = combining(output_alpha, background_input, img_input)

# a = img_new.dtype
# max_value = np.amax(img_new)
# print(a)

cv2.imshow('Composite Image', img_new)
cv2.waitKey(0)

# img_trimap.show()
# img_input = Image.open('input.png')
# input_array = np.array(img_input)
# # img_input.show()
# a, trimap_array = test_Trimap(trimap_array)
# print(a)

# output_alpha = Image.open('output_alpha.png')##
# alpha_array = np.array(output_alpha)##
# # output_alpha.show()

# b = MSE_calculation(alpha_array)
# print(b)

# background_input = Image.open('background.png')
# background_array = np.array(background_input)
# img_new = combining(alpha_array, background_array, input_array)
# print(img_new)
