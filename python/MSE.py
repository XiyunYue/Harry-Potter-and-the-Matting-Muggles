#Copyright 2023 by Xiaoru Liu, Trinity College Dublin. All rights reserved.
#
#This file is the function for calculate the MSE of the output 
#==================================================
"Create a function to calculate the MSE of the output "
import numpy as np
from PIL import Image
import cv2
from change_SameColorform import change_SameColorform

def MSE_calculation(result):
    '''
    input the output alpha and calculate the MSE for it
    Args:
        result: numpy.ndarray
    Returns:
        output: numpy.dtype
    '''
    alpha_ground = cv2.imread('groundtruth.png')
    alpha_ground = change_SameColorform(alpha_ground)
    ndim_alpha = alpha_ground.ndim
    if ndim_alpha == 3:
        alpha_ground  = alpha_ground [:,:,0]
    x_max, y_max = result.shape
    n = x_max * y_max
    output = 0
    output += np.sum(np.square(alpha_ground - result)) / n
    return output