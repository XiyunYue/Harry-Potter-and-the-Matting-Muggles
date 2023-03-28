#Copyright 2023 by Xiaoru Liu, Trinity College Dublin. All rights reserved.
#
#This file is the function for test the form for image and trimap
#==================================================
"Create a function to test the value of alpha matting image"
import numpy as np
from change_SameColorform import change_SameColorform

def test_alpha(alpha):
    '''
    input the alpha, test the value in it
    Args:
        alpha: numpy.ndarray
    Returns:
        outputs: str
        alpha : numpy.ndarray
    '''
    alpha = change_SameColorform(alpha)
    ndim = alpha.ndim
    if ndim == 3:
        alpha  = alpha [:,:,0]


    if np.any(np.logical_or(alpha != 1, alpha != 0)):
        outputs = 'Alpha image has something wrong'
    else:
        outputs = 'Alpha image is in right format'
    return outputs, alpha