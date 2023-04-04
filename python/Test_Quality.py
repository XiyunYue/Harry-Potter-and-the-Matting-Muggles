# Copyright 2023 by Xiaoru Liu, Trinity College Dublin. All rights reserved.
#
# This file is the unit test for MSE.
# ==================================================
"Create a function to test MSE"
import unittest
import numpy as np
from Quality_Inspection import MSE_calculation, PSNR_calculation, SAD_calculation



class Test_Quality(unittest.TestCase):

    def testMSE(self):

        x1 = np.array([[1, 2], [3, 4]])
        y1 = np.array([[4, 3], [2, 1]])
        # expected_output = 5.0
        # output = MSE_calculation(x1, y1)
        # self.assertAlmostEqual(output, expected_output)
        self.assertAlmostEqual(MSE_calculation(x1, y1), 5, places=4)
        x1 = np.array([[12, 11], [10, 10]])
        y1 = np.array([[10, 10], [10, 10]])
        self.assertAlmostEqual(MSE_calculation(x1, y1), 1.25, places=4)

    def testMSE(self):

        x1 = np.array([[1, 2], [3, 4]])
        y1 = np.array([[4, 3], [2, 1]])
        self.assertAlmostEqual(SAD_calculation(x1, y1), 8)
        x1 = np.array([[12, 11], [10, 10]])
        y1 = np.array([[10, 10], [10, 10]])
        self.assertAlmostEqual(SAD_calculation(x1, y1), 3)
        
    def testPSNR(self):

        x1 = np.array([[1, 2], [3, 4]])
        y1 = np.array([[4, 3], [2, 1]])
        self.assertAlmostEqual(PSNR_calculation(x1, y1), 4.77121, places=4)
        x1 = np.array([[12, 11], [10, 10]])
        y1 = np.array([[10, 10], [10, 10]])
        self.assertAlmostEqual(PSNR_calculation(x1, y1), 27.0555, places=4)


if __name__ == '__main__':
    unittest.main()