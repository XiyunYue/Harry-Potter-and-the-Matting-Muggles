#Copyright 2023 by Xiaoru Liu, Trinity College Dublin. All rights reserved.
#
#This file is the function for testing the form for trimap.Can accept input image as 8-bitRGB and change it to normalized pixels.
#Can accept trimap as 3D data and convert it to the correct format.
#==================================================
"Create a function to test the form for trimap"
import numpy as np
from change_SameColorform import change_SameColorform

def test_Trimap(trimap):
    '''
    input the trimap and test the form for it, change it to 1 channel
    Args:
        trimap: numpy.ndarray
    Returns:
        output: str
        trimap:numpy.ndarray
    '''
    trimap = change_SameColorform(trimap)
    ndim = trimap .ndim
    if ndim == 3:
        trimap  = trimap [:,:,0]

    if np.any(np.logical_or(trimap > 1, trimap < 0)):
        output = 'Trimap has something wrong'
    else:
        output = 'Trimap is ready'
    return output, trimap