# Copyright 2023 by Xiaoru Liu, Trinity College Dublin. All rights reserved.
#
# This file is the function for read image.
# ==================================================
"Create a function to read image and change it type of colour value"
from change_SameColorform import change_SameColorform
import cv2

def read_image(name):
    '''
    input the image's name to get trimap matrix
    Args:
        name: str
    Returns:
        image:numpy.ndarray
    '''
    img_input = cv2.imread(name)
    image = change_SameColorform(img_input)
    return image
