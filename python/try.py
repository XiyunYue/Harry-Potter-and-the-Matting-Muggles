from test_Trimap import test_Trimap
import numpy as np
from MSE import MSE_calculation
from combining import combining
import cv2
from test_SameSize import test_SameSize
from change_SameColorform import change_SameColorform
from test_alpha import test_alpha

img_input = cv2.imread('input.png')
img_input = change_SameColorform(img_input)

img_trimap = cv2.imread('trimap.png')
img_trimap = change_SameColorform(img_trimap)
fg = (img_trimap > 0.9).astype(int)
bg = (img_trimap < 0.01).astype(int)
unk = np.ones((img_trimap.shape))
unk = unk - fg - bg



# a = unk.dtype
# max_value = np.amax(unk)
# print(max_value)

location = np.where(unk == 1)
b = len(location)
# a = location.dtype
# max_value = np.amax(location)
# b = location.shape
print(b)

# print(location_X)




# output_alpha = cv2.imread('output_alpha.png')##
# output_alpha = output_alpha.astype("float64")/255
# background_input = cv2.imread('background.png')
# background_input = background_input.astype("float64")/255

# a,b,c = img_input.shape
# alpha_fg = output_alpha
# alpha_bg = 1 - output_alpha

# output = np.zeros((a,b,c))

# # for i in range(c):
# #     output[:,:,i] = alpha_fg[:,:,i] * img_input[:,:,i] + alpha_bg[:,:,i] * background_input[:,:,i]


# output = alpha_fg * img_input + alpha_bg * background_input

# # # img = Image.fromarray(output)
# cv2.imshow('Composite Image',output)
# cv2.waitKey(0)
# # # img.save('output.png')


