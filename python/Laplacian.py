# Copyright 2023 by Xiaoru Liu, Trinity College Dublin. All rights reserved.
#
# This file is the function for calculate Laplacian result and output it in unknow area in alpha
# ==================================================
"Create a function to use Laplacian function for matting "
import numpy as np
import cv2
from change_SameColorform import change_SameColorform
from scipy import ndimage


def Laplacian_matting(trimap, img):
    '''
    input the trimap and use Laplacian function for matting
    Args:
        trimap: numpy.ndarray
        im: numpy.ndarray
    Returns:
        alpha: numpy.ndarray
    '''

    a, b = trimap.shape
    alpha = np.zeros((a, b))

    fg = (trimap > 0.9).astype(int)
    bg = (trimap < 0.01).astype(int)

    unk = np.ones((trimap.shape))
    unk = unk - fg - bg
    a, b = trimap.shape
    alpha = np.zeros((a, b))
    b, g, r = cv2.split(img)
    laplacian_b = cv2.Laplacian(b, cv2.CV_64F)
    laplacian_g = cv2.Laplacian(g, cv2.CV_64F)
    laplacian_r = cv2.Laplacian(r, cv2.CV_64F)
    location = np.where(unk == 1)
    X = location[0]
    Y = location[1]

    for k in range(len(Y)):
        alpha[X[k], Y[k]] += laplacian_b[X[k], Y[k]] ** 2 + \
            laplacian_g[X[k], Y[k]] ** 2 + laplacian_r[X[k], Y[k]] ** 2

        alpha = 1 - np.sqrt(alpha / 3)
        bg_x, bg_y = np.where(bg == 1)
        alpha[bg_x, bg_y] = 0
        fg_x, fg_y = np.where(fg == 1)
        alpha[fg_x, fg_y] = 1
        return alpha
