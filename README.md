# Harry-Potter-and-the-Matting-Muggles

# Implementing Bayesian Matting

Description of Bayesian Matting
Bayesian matting is a technique used for image and video editing that allows for the extraction of a foreground object from its background in an image or a video. The algorithm uses a probabilistic model to estimate the foreground and background colors and the alpha matte, which is the per-pixel opacity or transparency of the foreground object.



Steps involved in Bayesian Matting and incorporated in this project:

- We initialize the values of foreground and background using the trimap. 

- We cluster the neighbourhood values of foreground and background pixels using known clustering algorithms for the unknown regions of the trimap based on the known values of the foreground and background pixels.
 
- We then try to estimate the F and B values by keeping the α constant.

- Then we estimate the value of α while F and B are constant. We run this in an iterative loop until we find the optimal values for all the variables.
 
- We then use this α value to estimate the F and B values (1’s and 0’s) corresponding to the unknown region which is going to be the desired α matte. 

- We can use this α matte to further superimpose various backgrounds by our foreground using the composite equation discussed in the math.
