#Copyright 2023 by Xiaoru Liu, Trinity College Dublin. All rights reserved.
#
#This file is the function for using Laplacian function for matting
#==================================================
"Create a function to use Laplacian function for matting "
import numpy as np
import cv2
from change_SameColorform import change_SameColorform
import scipy.special

def Laplacian_matting(trimap, img):
    '''
    input the trimap and use Laplacian function for matting
    Args:
        trimap: numpy.ndarray
        im: numpy.ndarray
    Returns:
        alpha: numpy.ndarray
    '''
    fg = trimap > 0.9
    bg = trimap < 0.01
    unk = ~(fg | bg)
    X, Y = np.where(unk == 1)
    Laplacian = scipy.special.laplace(img)
    alpha = np.zeros((x, y))
    alpha[bg[:, :, 0]] = 0
    alpha[fg[:, :, 0]] = 1
    
    for i in unk:
        for i in range(c):
            alpha[X[k], Y[k]] += Laplacian[X[k], Y[k], i] ** 2
    
    alpha = 1 - np.sqrt(alpha / c)
    alpha[bg[:, :, 0]] = 0
    alpha[fg[:, :, 0]] = 1
    
    return alpha