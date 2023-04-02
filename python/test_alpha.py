# Copyright 2023 by Xiaoru Liu, Trinity College Dublin. All rights reserved.
#
# This file is the function for testing the form for trimap. Checking if the value in it are between 0,1
# ==================================================
"Create a function to test the form for trimap"
import unittest
import numpy as np
from read_image import read_image
from main_Bayesian import bayesian_matte
from read_Trimap import read_Trimap


class Test_Trimap(unittest.TestCase):

    def testTrimap(self):

        image_name = 'image1/input.png'
        image = read_image(image_name)
        name = 'image1/trimap.png'
        Trimap = read_Trimap(name)
        alpha = bayesian_matte(image, Trimap, sigma=8, N=50, minN=10)
        for row in alpha:
            self.assertGreaterEqual(alpha, 0)
            self.assertLessEqual(alpha, 1)


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
