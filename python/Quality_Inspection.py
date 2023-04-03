# Copyright 2023 by Xiaoru Liu, Trinity College Dublin. All rights reserved.
#
# This file is the function for calculate the MSE,PSNR and SAD of the output
# ==================================================
"Create a function to calculate the different quality assessment for the output "
import numpy as np
import math


def SAD_calculation(result, alpha_ground):
    '''
    input the output alpha and calculate the SAD for it
    Args:
        result: numpy.ndarray
    Returns:
        output: numpy.dtype
    '''
    SAD = 0
    SAD = np.sum(abs(alpha_ground - result))
    return SAD


def MSE_calculation(result, alpha_ground):
    '''
    input the output alpha and calculate the MSE for it
    Args:
        result: numpy.ndarray
    Returns:
        output: numpy.dtype
    '''

    output = 0
    output =  np.mean(np.square(alpha_ground - result))
    return output


def PSNR_calculation(MSE):
    '''
    input the MSE result and calculate the PSNR for it
    Args:
        result: numpy.ndarray
    Returns:
        output: numpy.dtype
    '''

    output = 10 * math.log(1/MSE, 10)
    return output
