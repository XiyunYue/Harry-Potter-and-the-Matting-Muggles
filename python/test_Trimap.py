# Copyright 2023 by Xiaoru Liu, Trinity College Dublin. All rights reserved.
#
# This file is the function for testing the form for trimap. Checking if the value in it are between 0,1
# ==================================================
"Create a function to test the form for trimap"
import unittest
from read_Trimap import read_Trimap


class Test_Trimap(unittest.TestCase):

    def testTrimap(self):
        name = 'image1/trimap.png'
        result = read_Trimap(name)
        for row in result:
            for value in row:
                self.assertGreaterEqual(value, 0)
                self.assertLessEqual(value, 1)

if __name__ == '__main__':
    unittest.main()