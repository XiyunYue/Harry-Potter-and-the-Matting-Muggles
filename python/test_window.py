import unittest
import numpy as np
from Bayessian_matte1 import get_window
import math


class TestGetWindow(unittest.TestCase):

    def setUp(self):
        self.img = np.random.rand(30, 30, 3)
        self.x_values = [10, 15, 20]
        self.y = 15
        self.N_values = [3, 5, 7]

    def test_size(self):
        for x in self.x_values:
            for n in self.N_values:
                window = get_window(self.img, x, self.y, n)
                self.assertEqual(window.shape, (n, n, 3))

    def test_center(self):
        for x in self.x_values:
            for n in self.N_values:
                window = get_window(self.img, x, self.y, n)
                center_pixel = window[math.floor(n/2), math.floor(n/2)]
                center_pixel_img = self.img[self.y, x]
                self.assertTrue(np.array_equal(center_pixel, center_pixel_img))
                # self.assertEqual( center_pixel.any, center_pixel_img.any)

    def test_window_corner(self):
        for x in self.x_values:
            for n in self.N_values:
                window = get_window(self.img, len(
                    self.img[1, :]) - 1, len(self.img[:, 1]) - 1, n)
                pixel_end = window[math.floor(n/2), math.floor(n/2)]
                pixel_end_img = self.img[len(self.img[1, :]) - 1, len(self.img[:, 1]) - 1]
                # self.assertTrue(np.array_equal(window[0, 0], np.array([1, 1, 1])))
                self.assertTrue(np.array_equal(pixel_end, pixel_end_img))

    def test_window_corner(self):
        for x in self.x_values:
            for n in self.N_values:
                window = get_window(self.img, len(self.img[:, 1]) - 1, 0, n)
                pixel_end = window[math.floor(n/2), math.floor(n/2)]
                pixel_end_img = self.img[0, len(self.img[:, 1]) - 1]
                # self.assertTrue(np.array_equal(window[0, 0], np.array([1, 1, 1])))
                self.assertTrue(np.array_equal(pixel_end, pixel_end_img))


if __name__ == '__main__':
    unittest.main()
