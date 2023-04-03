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

# Proposed End to End and Unit Tests
 Performance Evaluation
- For the operation of the entire algorithm we propose a time recording to avoid producing an overly complex or inefficient program.

Unit test input
- Detect whether the read Trimap is in the correct form: detect the matrix data where the read Trimap is located. 
- Avoid it consisting only of 0 or 1, no other data.

Unit test algorithms
- Check whether the output of the alpha matte is composed of 0’s and 1’s. 
- If the output matte has either all 0’s or all 1’s it is invalid. If the output matte has any other value, it is invalid.  
- Testing whether the color of our extracted foreground changes when combined with the new background. Lastly, check if the algorithm for combining the background is correct.








