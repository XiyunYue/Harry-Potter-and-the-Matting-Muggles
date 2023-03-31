# Copyright 2023 by Xiaoru Liu, Trinity College Dublin. All rights reserved.
#
# This file is the function for read trimap.Can accept input image as 8-bitRGB and change it to normalized pixels.
# Can accept trimap as 3D data and convert it to the correct format.
# ==================================================
"Create a function to test the form for trimap"
import numpy as np
from change_SameColorform import change_SameColorform
import cv2

def read_Trimap(name):
    '''
    input the trimap's name to get trimap matrix
    Args:
        name: str
    Returns:
        trimap:numpy.ndarray
    '''
    img_trimap = cv2.imread(name)
    trimap = change_SameColorform(img_trimap)
    ndim = trimap.ndim
    if ndim == 3:
        trimap = trimap[:, :, 0]

    # if np.any(np.logical_or(trimap > 1, trimap < 0)):
    #     output = 'Trimap has something wrong'
    # else:
    #     output = 'Trimap is ready'
    return trimap
