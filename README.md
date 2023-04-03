# Harry-Potter-and-the-Matting-Muggles

# Implementing Bayesian Matting

Description of Bayesian Matting
Bayesian matting is a technique used for image and video editing that allows for the extraction of a foreground object from its background in an image or a video. The algorithm uses a probabilistic model to estimate the foreground and background colors and the alpha matte, which is the per-pixel opacity or transparency of the foreground object.

The Math: 
The compositing equation:

![image](https://user-images.githubusercontent.com/117815807/229576357-7e12d244-b296-4083-816e-004a4badda85.png)

Where, C is the composite, α is the pixel’s opacity value, F is the foreground and B is the background.
We further use the Maximum a posteriori (MAP) technique to estimate the α, F and B given the observation C. We express this over a probability distribution which is further reduced to an maximum likelihood estimate of the sum of log likelihood.

![image](https://user-images.githubusercontent.com/117815807/229576513-46fe39cd-a570-44d9-b7bc-ce3fe1e4e6ab.png)
![image](https://user-images.githubusercontent.com/117815807/229576542-3c2102b8-5470-4bee-8fba-47e3fa40966b.png)

The above equation of log likelihoods can be estimated using,

![image](https://user-images.githubusercontent.com/117815807/229576603-7e3fe3da-2199-47a6-ae58-01661c96d228.png)

Which stems out of the error term. The log likelihood for the foreground and the background can be estimated using 

![image](https://user-images.githubusercontent.com/117815807/229576657-085780d8-133a-4d0b-b8ca-27ee41bcd2ac.png)

With a similarly analogous equation for the background. 
![image](https://user-images.githubusercontent.com/117815807/229576574-539cb2d2-e44b-498f-be00-7e3a3393cc2f.png)

The ultimate goal is to maximize the above functions by alternating between keeping α constant and varying F and B

![image](https://user-images.githubusercontent.com/117815807/229576758-c245b752-38c2-41d7-846b-e2aea84e914a.png)

Where we can solve the above using linear algebra to find the values of F and B. Next we keep F and B constant and vary the α
![image](https://user-images.githubusercontent.com/117815807/229576791-40dde41e-0138-4278-a849-f05b22b70cc7.png)


Steps involved in Bayesian Matting and incorporated in this project
We initialize the values of foreground and background using the trimap. 
We cluster the neighbourhood values of foreground and background pixels using known clustering algorithms for the unknown regions of the trimap based on the known values of the foreground and background pixels.
Now we try to estimate the F and B values by keeping the α constant.
Then we estimate the value of α while F and B are constant. We run this in an iterative loop until we find the optimal values for all the variables.
We then use this α value to estimate the F and B values (1’s and 0’s) corresponding to the unknown region which is going to be the desired α matte. 
We can use this α matte to further superimpose various backgrounds by our foreground using the composite equation discussed in the math.
