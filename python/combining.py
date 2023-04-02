# Copyright 2023 by Xiaoru Liu, Trinity College Dublin. All rights reserved.
#
# This file is the function for combining the image foreground with a new background
# ==================================================
"Create a function to combine the foreground with a new background"
import numpy as np
from PIL import Image
import cv2


def combining(alpha, background, img):
    '''
    input the alpha and use it combine foreground with a new background
    Args:
        alpha: numpy.ndarray
        background: numpy.ndarray
        img: numpy.ndarray
    Returns:
        output: numpy.ndarray
    '''
    a, b, c = img.shape
    alpha_fg = alpha
    alpha_bg = 1 - alpha

    output = np.zeros((a, b, c))

    for i in range(c):
        output[:, :, i] = alpha_fg * img[:, :, i] + \
            alpha_bg * background[:, :, i]
    return output
