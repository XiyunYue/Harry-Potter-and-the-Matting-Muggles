# Copyright 2023 by Xiaoru Liu, Trinity College Dublin. All rights reserved.
#
# This file is the function for testing images color format and change them if there are not unit8
# ==================================================
"Create a function to test images color format"
import numpy as np


def change_Size(image):
    '''
    input images, test the color format for it
    Args:
        image: numpy.ndarray
    Returns:
        outputs: numpy.ndarray
    '''
    ndim = image.ndim
    if ndim == 3:
        image = image[:, :, 0]

    return image
