# Copyright 2023 by Xiaoru Liu, Trinity College Dublin. All rights reserved.
#
# This file is the function for Comparing two images to see if they are the same size
# ==================================================
"Create a function to compare two images to see if they are the same size"
import unittest
import numpy as np
from read_image import read_image
from Bayessian_matte1 import Bayesian_Matte1
from read_Trimap import read_Trimap
from change_Size import change_Size

class Test_alpha(unittest.TestCase):

    def testalpha_sameSize(self):

        image_name = 'image1/input.png'
        image = read_image(image_name)
        name = 'image1/trimap.png'
        Trimap = read_Trimap(name)        
        alpha, unknow = Bayesian_Matte1(image, Trimap)
        alpha = change_Size(alpha)
        
        self.assertTrue(np.array_equal(np.shape(Trimap), np.shape(alpha)))
        

if __name__ == '__main__':
    unittest.main()

# def test_alpha(alpha):
#     '''
#     input the alpha, test the value in it
#     Args:
#         alpha: numpy.ndarray
#     Returns:
#         outputs: str
#         alpha : numpy.ndarray
#     '''
#     alpha = change_SameColorform(alpha)
#     ndim = alpha.ndim
#     if ndim == 3:
#         alpha = alpha[:, :, 0]

#     if np.any(np.logical_or(alpha != 1, alpha != 0)):
#         outputs = 'Alpha image has something wrong'
#     else:
#         outputs = 'Alpha image is in right format'
#     return outputs, alpha
