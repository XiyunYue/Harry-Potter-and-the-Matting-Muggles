# Copyright 2023 by Xiaoru Liu, Trinity College Dublin. All rights reserved.
#
# This file is the unit test for MSE.
# ==================================================
"Create a function to test MSE"
import unittest
import numpy as np
from Quality_Inspection import MSE_calculation, PSNR_calculation, SAD_calculation


class Test_Quality(unittest.TestCase):

    def setUp(self):
        self.x1 = np.array([[1, 2], [3, 4]])
        self.y1 = np.array([[4, 3], [2, 1]])
        self.x2 = np.array([[12, 11], [10, 10]])
        self.y2 = np.array([[10, 10], [10, 10]])

    def testMSE(self):

        # expected_output = 5.0
        # output = MSE_calculation(x1, y1)
        # self.assertAlmostEqual(output, expected_output)
        self.assertAlmostEqual(MSE_calculation(self.x1, self.y1), 5, places=4)
        self.assertAlmostEqual(MSE_calculation(
            self.x2, self.y2), 1.25, places=4)

    def testSAD(self):

        self.assertAlmostEqual(SAD_calculation(self.x1, self.y1), 8)
        self.assertAlmostEqual(SAD_calculation(self.x2, self.y2), 3)

    def testPSNR(self):

        self.assertAlmostEqual(PSNR_calculation(self.x1, self.y1), 41.14110, places=4)
        self.assertAlmostEqual(PSNR_calculation(self.x2, self.y2), 47.16170, places=4)


if __name__ == '__main__':
    unittest.main()
