import numpy as np
from PIL import Image, ImageOps
import matplotlib.pyplot as plt
import cv2
import os

# orchard_bouman_clust.py should be in the folder
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


# To get a window where center is (x,y) that is of size (N,N)
def get_window(img,x,y,N=55):
    """
    Extracts a small window of input image, around the center (x,y)
    img - input image
    x,y - cordinates of center
    N - size of window (N,N) {should be odd}
    """

    h, w, c = img.shape             # Extracting Image Dimensions
    
    arm = N//2                      # Arm from center to get window
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
    mu_F - Mean of foreground pixel
    Sigma_F - Covariance Mat of foreground pixel
    mu_B, Sigma_B - Mean and Covariance of background pixel
    C, Sigma_C - Current pixel, and its variance
    alpha_init - starting alpha value
    maxIter - Iterations to solve the value of the pixel
    minLike - min likelihood to reach to stop before maxIterations. 
    """

    # Initializing Matrices
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
    img - input image that the user will give to perform the foreground-background mapping
    trimap - the alpha mapping that is given with foreground and background determined.
    N - Window size, determines how many pixels will be sampled around the pixel to be solved, should be always odd.
    sig - wieghts of the neighbouring pixels. less means more centered.
    minNeighbours - Neigbour pixels available to solve, should be greater than 0, else inverse wont be calculated
    '''
    
    # We Convert the Images to float so that we are able to play with the pixel values
    img = np.array(img,dtype = 'float')
    trimap = np.array(trimap, dtype = 'float')
    
    # Here we normalise the Images to range from 0 and 1.
    img /= 255
    # trimap /= 255

    # We get the dimensions 
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
            # Preparing the gaussian weights for window
            N += 10
            # sig += 1 
            gaussian_weights = matlab_style_gauss2d((N,N),sig)
            gaussian_weights /= np.max(gaussian_weights)
            print(N)

    return a_channel,n_unknown
# name = "GT05"

# os.path.join("data","gt_training_lowres","{}.png".format(name))

# image = np.array(Image.open(os.path.join("data","input_training_lowres","{}.png".format(name))))
# image_trimap = np.array(ImageOps.grayscale(Image.open(os.path.join("data","trimap_training_lowres","{}.png".format(name)))))

# alpha,pixel_count = Bayesian_Matte(image,image_trimap) 
# alpha *= 255

# image_alpha = np.array(ImageOps.grayscale(Image.open(os.path.join("data","gt_training_lowres","{}.png".format(name))
# )))

# alpha_int8 = np.array(alpha,dtype = int)

# plt.imsave("{}_alpha.png".format(name), alpha, cmap='gray')
# show_im(alpha)

# print("Absolute Loss with ground truth - ", np.sum(np.abs(alpha - image_alpha))/(alpha.shape[0]*alpha.shape[1]))
