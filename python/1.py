import unittest
import numpy as np
from orchard_bouman_clust import split


class TestSplit(unittest.TestCase):

    def __init__(self, matrix, w):
        W = np.sum(w)
        self.w = w
        self.X = matrix
        self.left = None
        self.right = None
        self.mu = np.einsum('ij,i->j', self.X, w)/W
        diff = self.X - np.tile(self.mu, [np.shape(self.X)[0], 1])
        t = np.einsum('ij,i->ij', diff, np.sqrt(w))
        self.cov = (t.T @ t)/W + 1e-5*np.eye(3)
        self.N = self.X.shape[0]
        V, D = np.linalg.eig(self.cov)
        self.lmbda = np.max(np.abs(V))
        self.e = D[np.argmax(np.abs(V))]

    def test_split(self):
        X = np.array([[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]])
        w = np.array([1, 1, 1, 1, 1])
        e = np.array([1, 0])
        mu = np.array([2, 2])
        lmbda = 1
        C_i = split(X, w, e, mu, lmbda)
        nodes = [C_i]
        nodes = split(nodes)
        self.assertEqual(len(nodes), 2)
        self.assertTrue(np.array_equal(nodes[0].X, np.array([[0, 0], [1, 1], [2, 2]])))
        self.assertTrue(np.array_equal(nodes[0].w, np.array([1, 1, 1])))
        self.assertTrue(np.array_equal(nodes[0].e, np.array([1, 0])))
        self.assertTrue(np.array_equal(nodes[0].mu, np.array([1, 1])))
        self.assertEqual(nodes[0].lmbda, 1)
        self.assertTrue(np.array_equal(nodes[1].X, np.array([[3, 3], [4, 4]])))
        self.assertTrue(np.array_equal(nodes[1].w, np.array([1, 1])))
        self.assertTrue(np.array_equal(nodes[1].e, np.array([1, 0])))
        self.assertTrue(np.array_equal(nodes[1].mu, np.array([3.5, 3.5])))
        self.assertEqual(nodes[1].lmbda, 1)


if __name__ == '__main__':
    unittest.main()
