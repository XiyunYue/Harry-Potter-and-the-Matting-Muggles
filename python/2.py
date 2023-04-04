import numpy as np
import unittest

from orchard_bouman_clust import clustFunc


class TestClustFunc(unittest.TestCase):
    
    def setUp(self):
        self.S = np.array([[1, 2, 3], [3, 4, 5], [5, 6, 7], [7, 8, 9], [9, 10, 11]])
        self.w = np.array([1, 1, 1, 1, 1])
    
    def test_clustering(self):
        mu, sigma = clustFunc(self.S, self.w)
        self.assertEqual(mu.shape[0], sigma.shape[0]) 
        self.assertGreater(mu.shape[0], 1)
        self.assertEqual(mu.shape[1], self.S.shape[1]) 
        
    def test_minVar(self):
        mu, sigma = clustFunc(self.S, self.w, minVar=0.5)
        self.assertEqual(mu.shape[0], 5) 
        
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()