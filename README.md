# Implementation Steps for each method

# Bayesian Matting
a)	Load the image and trimap (initial segmentation of image into foreground, background, and unknown regions)
b)	Convert the image to grayscale if it is not already in grayscale.
c)	Calculate the alpha matte using the following steps: 
d)	Estimate the foreground and background color distributions using the pixels in their respective regions of the trimap. 
e)	For each pixel in the unknown region of the trimap, calculate the probability that it belongs to the foreground or background using Bayes' theorem and the color distributions. 
f)	Use the probabilities to calculate the alpha matte for each pixel in the unknown region.
g)	Refine the alpha matte using a post-processing method.
h)	Composite the foreground onto a new background using the alpha matte.

# Laplacian Matting
a)	Load the image and trimap
b)	Convert the image to grayscale if it is not already in grayscale.
c)	Compute the Laplacian matrix for the unknown region of the trimap.
d)	Compute the inverse of the Laplacian matrix using a sparse matrix solver.
e)	Construct the Laplacian matrix for the entire image by combining the Laplacian matrix for the unknown region with identity matrices for the foreground and background regions.
f)	Compute the alpha matte by solving a linear system of equations using the Laplacian matrix and the color values of the image.
g)	Refine the alpha matte using a post-processing method such as Poisson matting.
h)	Composite the foreground onto a new background using the alpha matte.
