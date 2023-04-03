# Copyright 2023 by Xiaoru Liu, Trinity College Dublin. All rights reserved.
#
# This file is the function for Comparing two images to see if they are the same size
# ==================================================
"Create a function to compare two images to see if they are the same size"
import unittest
from read_image import read_image
from Bayessian_matte1 import Bayesian_Matte1
from read_Trimap import read_Trimap
class test_Samesize(unittest.TestCase):
    
    def test_sameSize(self):

        
        image_name = 'image1/input.png'
        image = read_image(image_name)
        name = 'image1/trimap.png'
        Trimap = read_Trimap(name)        
        alpha = Bayesian_Matte1(image, Trimap, sigma=8, N=50 , minN=10)
        image = read_image(image_name)
        self.assertEqual(Trimap.shape, alpha.shape)
        
if __name__ == '__main__':
    unittest.main()



# def test_SameSize(image1, image2):
#     '''
#     input the two images, test the form for them
#     Args:
#         image1, image2: numpy.ndarray
#     Returns:
#         outputs: str
#     '''

#     ndim_1 = image1.ndim
#     ndim_2 = image2.ndim
#     if ndim_1 == 3:
#         a1, b1, c1 = image1.shape
#     else:
#         a1, b1 = image1.shape
#     if ndim_2 == 3:
#         a2, b2, c2 = image2.shape
#     else:
#         a2, b2 = image2.shape

#     if a1 == a2 and b1 == b2:
#         outputs = "same"
#     else:
#         outputs = "different"
#     return outputs
