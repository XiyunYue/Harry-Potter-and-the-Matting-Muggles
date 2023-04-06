import numpy as np
from PIL import Image, ImageOps
import matplotlib.pyplot as plt
import cv2
import os

# orchard_bouman_clust.py which was used given by the marco's code
from orchard_bouman_clust import clustFunc


# Provided by Matlab
def matlab_style_gauss2d(shape=(3, 3), sigma=0.5):
    """
    2D gaussian mask - should give the same result as MATLAB's
    fspecial('gaussian',[shape],[sigma])
    """
    m, n = [(ss-1.)/2. for ss in shape]
    y, x = np.ogrid[-m:m+1, -n:n+1]
    h = np.exp(-(x*x + y*y)/(2.*sigma*sigma))
    h[h < np.finfo(h.dtype).eps*h.max()] = 0
    sumh = h.sum()
    if sumh != 0:
        h /= sumh
    return h


# For a size (N,N) we get a window where center is (x,y)
def get_window(img,x,y,N=55):
    """
    This function retrieves a small window of the input image around the center coordinates (x,y):

    "img": the input image
    "x" and "y": the coordinates of the center pixel
    "N": the size of the window to be extracted, which should be an odd number and is represented as (N,N).
    """

    h, w, c = img.shape             # defining dimensions
    
    arm = N//2                      # centering around to get the window
    window = np.zeros((N,N,c))      

    xmin = max(0,x-arm)
    xmax = min(w,x+arm+1)
    ymin = max(0,y-arm)
    ymax = min(h,y+arm+1)

    window[arm - (y-ymin):arm +(ymax-y),arm - (x-xmin):arm +(xmax-x)] = img[ymin:ymax,xmin:xmax]

    return window
    
## To solve individual pixels
def solve(mu_F, Sigma_F, mu_B, Sigma_B, C, Sigma_C, alpha_init, maxIter = 50, minLike = 1e-6):
    """
    The following are the variables used in solving the pixel value during foreground-background mapping:

    "mu_F": the mean of the foreground pixel
    "Sigma_F": the covariance matrix of the foreground pixel
    "mu_B" and "Sigma_B": the mean and covariance of the background pixel
    "C" and "Sigma_C": the current pixel and its variance
    "alpha_init": the initial alpha value used for solving
    "maxIter": the number of iterations to be performed for finding the pixel value
    "minLike": the minimum likelihood value to be reached before stopping the algorithm before reaching the maximum number of iterations.
    """

    # We initialize the matrices
    I = np.eye(3)
    fg_best = np.zeros(3)
    bg_best = np.zeros(3)
    a_best = np.zeros(1)
    maxlike = -np.inf
    
    invsgma2 = 1/Sigma_C**2
    
    for i in range(mu_F.shape[0]):
        # Mean of Foreground pixel can have multiple possible values, iterating for all.
        mu_Fi = mu_F[i]
        invSigma_Fi = np.linalg.inv(Sigma_F[i])

        for j in range(mu_B.shape[0]):
            # Similarly, multiple mean values be possible for background pixel.
            mu_Bj = mu_B[j]
            invSigma_Bj = np.linalg.inv(Sigma_B[j])

            alpha = alpha_init
            myiter = 1
            lastLike = -1.7977e+308

            # Solving Minimum likelihood through numerical methods
            while True:
                # Making Equations for AX = b, where we solve for X.abs
                # X here has 3 values of forground pixel (RGB) and 3 values for background
                A = np.zeros((6,6))
                A[:3,:3] = invSigma_Fi + I*alpha**2 * invsgma2
                A[:3,3:] = A[3:,:3] = I*alpha*(1-alpha) * invsgma2
                A[3:,3:] = invSigma_Bj+I*(1-alpha)**2 * invsgma2
                
                b = np.zeros((6,1))
                b[:3] = np.reshape(invSigma_Fi @ mu_Fi + C*(alpha) * invsgma2,(3,1))
                b[3:] = np.reshape(invSigma_Bj @ mu_Bj + C*(1-alpha) * invsgma2,(3,1))

                # Solving for X and storing values for Forground and Background Pixels 
                X = np.linalg.solve(A, b)
                F = np.maximum(0, np.minimum(1, X[0:3]))
                B = np.maximum(0, np.minimum(1, X[3:6]))
                
                # Solving for value of alpha once F and B are calculated
                alpha = np.maximum(0, np.minimum(1, ((np.atleast_2d(C).T-B).T @ (F-B))/np.sum((F-B)**2)))[0,0]
                
                # Calculating likelihood value for
                like_C = - np.sum((np.atleast_2d(C).T -alpha*F-(1-alpha)*B)**2) * invsgma2
                like_fg = (- ((F- np.atleast_2d(mu_Fi).T).T @ invSigma_Fi @ (F-np.atleast_2d(mu_Fi).T))/2)[0,0]
                like_bg = (- ((B- np.atleast_2d(mu_Bj).T).T @ invSigma_Bj @ (B-np.atleast_2d(mu_Bj).T))/2)[0,0]
                like = (like_C + like_fg + like_bg)

                if like > maxlike:
                    a_best = alpha
                    maxlike = like
                    fg_best = F.ravel()
                    bg_best = B.ravel()

                if myiter >= maxIter or abs(like-lastLike) <= minLike:
                    break

                lastLike = like
                myiter += 1
    return fg_best, bg_best, a_best 

def Bayesian_Matte1(img,trimap,N = 55,sig = 8,minNeighbours = 6):
    '''
    The following are the parameters for performing foreground-background mapping on an input image given by the user:

    "img": the input image
    "trimap": an alpha mapping that specifies the foreground and background regions
    "N": a window size that determines the number of pixels to be sampled around the pixel being solved; it should always be an odd number
    "sig": weights given to neighboring pixels; lower values mean more emphasis is placed on the central pixel
    "minNeighbours": the minimum number of neighboring pixels available for solving; it should be greater than 0, or else the inverse cannot be calculated.
    '''
    
    # We Convert the Images to float so that we are able to play with the pixel values
    img = np.array(img,dtype = 'float')
    trimap = np.array(trimap, dtype = 'float')
    
    # From the range 0 and 1, here we normalize the images.
    img /= 255

    # defining dimensions
    h,w,c = img.shape
    
    # Preparing the gaussian weights for window
    gaussian_weights = matlab_style_gauss2d((N,N),sig)
    gaussian_weights /= np.max(gaussian_weights)

    # We seperate the foreground specified in the trimap from the main image.
    fg_map = trimap == 1
    fg_actual = np.zeros((h,w,c))
    fg_actual = img * np.reshape(fg_map,(h,w,1))

    # We seperate the background specified in the trimap from the main image. 
    bg_map = trimap == 0
    bg_actual = np.zeros((h,w,c))
    bg_actual = img * np.reshape(bg_map,(h,w,1))
    
    # Creating empty alpha channel to fill in by the program
    unknown_map = np.logical_or(fg_map,bg_map) == False
    a_channel = np.zeros(unknown_map.shape)
    a_channel[fg_map] = 1
    a_channel[unknown_map] = np.nan

    # Finding total number of unkown pixels to be calculated
    n_unknown = np.sum(unknown_map)

    # Making the datastructure for finding pixel values and saving id they have been solved yet or not.
    A,B = np.where(unknown_map == True)
    not_visited = np.vstack((A,B,np.zeros(A.shape))).T

    print("Solving Image with {} unsovled pixels... Please wait...".format(len))

    # running till all the pixels are solved.
    while(sum(not_visited[:,2]) != n_unknown):
        last_n = sum(not_visited[:,2])

        # iterating for all pixels
        for i in range(n_unknown): 
            # checking if solved or not
            if not_visited[i,2] == 1:
                continue
            
            # If not solved, we try to solve
            else:
                # We get the location of the unsolved pixel
                y,x = map(int,not_visited[i,:2])
                
                # Creating an window which states what pixels around it are solved(forground/background)
                a_window = get_window(a_channel[:, :, np.newaxis], x, y, N)[:,:,0]
                
                # Creating a window and weights of solved foreground window
                fg_window = get_window(fg_actual,x,y,N)
                fg_weights = np.reshape(a_window**2 * gaussian_weights,-1)
                values_to_keep = np.nan_to_num(fg_weights) > 0
                fg_pixels = np.reshape(fg_window,(-1,3))[values_to_keep,:]
                fg_weights = fg_weights[values_to_keep]
        
                # Creating a window and weights of solved background window
                bg_window = get_window(bg_actual,x,y,N)
                bg_weights = np.reshape((1-a_window)**2 * gaussian_weights,-1)
                values_to_keep = np.nan_to_num(bg_weights) > 0
                bg_pixels = np.reshape(bg_window,(-1,3))[values_to_keep,:]
                bg_weights = bg_weights[values_to_keep]
                
                # We come back to this pixel later if it doesnt has enough solved pixels around it.
                if len(bg_weights) < minNeighbours or len(fg_weights) < minNeighbours:
                    continue
                
                # If enough pixels, we cluster these pixels to get clustered colour centers and their covariance    matrices
                mean_fg, cov_fg = clustFunc(fg_pixels,fg_weights)
                mean_bg, cov_bg = clustFunc(bg_pixels,bg_weights)
                alpha_init = np.nanmean(a_window.ravel())
                
                # We try to solve our 3 equation 7 variable problem with minimum likelihood estimation
                fg_pred,bg_pred,alpha_pred = solve(mean_fg,cov_fg,mean_bg,cov_bg,img[y,x],0.7,alpha_init)

                # storing the predicted values in appropriate windows for use for later pixels.
                fg_actual[y, x] = fg_pred.ravel()
                bg_actual[y, x] = bg_pred.ravel()
                a_channel[y, x] = alpha_pred
                not_visited[i,2] = 1
                if(np.sum(not_visited[:,2])%1000 == 0):
                    print("Solved {} out of {}.".format(np.sum(not_visited[:,2]),len(not_visited)))

        if sum(not_visited[:,2]) == last_n:
            # ChangingWindow Size
            N += 2
            # Now we reuse the gaussian weights for the changing window
            gaussian_weights = matlab_style_gauss2d((N,N),sig)
            gaussian_weights /= np.max(gaussian_weights)
            print(N)
        if N>300:
            break

    return a_channel,n_unknown
