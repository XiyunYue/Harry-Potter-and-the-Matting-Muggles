# Implementing Bayesian Matting

## High-level Description of the project

This assignment builds on Assignment 2. We want to detect an image foreground and background by using trimap.

---
## Requirements
Python 3.5 +
Numpy
Matplotlib
Opencv


## Installation and Execution                 
```
matplotlib==3.6.2
numpy==1.23.4
Pillow==9.5.0
```


## Running the demo
Afer installing all required packages you can run the demo file simply by typing:

`python main.py`

If you need to run the end to end result, you can run test by typing:

`python main.py`

If you meet some bug and want to test, you need to run the unit test, you can run test by typing:

`Test_Quality.py`

`Test_alpha.py`

`Test_Trimap.py`

`Test_window.py`

## Description of Bayesian Matting

Bayesian matting is a technique used for image and video editing that allows for the extraction of a foreground object from its background in an image or a video. The algorithm uses a probabilistic model to estimate the foreground and background colors and the alpha matte, which is the per-pixel opacity or transparency of the foreground object.

Steps involved in Bayesian Matting:

- We initialize the values of foreground and background using the trimap.

- We cluster the neighbourhood values of foreground and background pixels using known clustering algorithms for the unknown regions of the trimap based on the known values of the foreground and background pixels.

- We then try to estimate the F and B values by keeping the α constant.

- Then we estimate the value of α while F and B are constant. We run this in an iterative loop until we find the optimal values for all the variables.

- We then use this α value to estimate the F and B values (1’s and 0’s) corresponding to the unknown region which is going to be the desired α matte.

- We can use this α matte to further superimpose various backgrounds by our foreground using the composite equation discussed in the math.

## Implementation steps for each method

### Bayesian Matting

a) Load the image and trimap (initial segmentation of image into foreground, background, and unknown regions).

b) Convert the image to grayscale if it is not already in grayscale.

c) Calculate the alpha matte using the following steps:

d) Estimate the foreground and background color distributions using the pixels in their respective regions of the trimap.

e) For each pixel in the unknown region of the trimap, calculate the probability that it belongs to the foreground or background using Bayes' theorem and the color distributions.

f) Use the probabilities to calculate the alpha matte for each pixel in the unknown region.

g) Refine the alpha matte using a post-processing method.

h) Composite the foreground onto a new background using the alpha matte.

### Laplacian Matting

a) Load the image and trimap.

b) Convert the image to grayscale if it is not already in grayscale.

c) Compute the Laplacian matrix for the unknown region of the trimap.

d) Compute the inverse of the Laplacian matrix using a sparse matrix solver.

e) Construct the Laplacian matrix for the entire image by combining the Laplacian matrix for the unknown region with identity matrices for the foreground and background regions.

f) Compute the alpha matte by solving a linear system of equations using the Laplacian matrix and the color values of the image.

g) Refine the alpha matte using a post-processing method such as Poisson matting.

h) Composite the foreground onto a new background using the alpha matte.

## Comparison between Bayesian and Laplacian Matting

Bayesian matting: This method uses a Bayesian framework to estimate the foreground and background colors of a pixel based on the color values of its neighboring pixels, as well as the foreground and background colors of nearby known pixels. It also incorporates prior knowledge about the likelihood of a pixel being foreground or background based on its location in the image. Bayesian matting can produce high-quality mattes with accurate edges and fine details, but it can be computationally sensitive to the quality and quantity of the input data.

Laplacian matting: This method uses a Laplacian equation to solve for the alpha matte, which represents the opacity of each pixel in the foreground object. It relies on the assumption that the color values of the foreground and background regions can be modeled by a linear combination of a small set of basis colors. Laplacian matting can be faster and more robust than Bayesian matting, especially for images with large and smooth background regions, but it may produce artifacts or errors in areas with complex or ambiguous color distributions.

## Proposed end to end and unit tests

Performance Evaluation

- For the operation of the entire algorithm we propose a time recording to avoid producing an overly complex or inefficient program.

Unit test - Input

- Detect whether the read Trimap is in the correct form: detect the matrix data where the read Trimap is located.
- Avoid it consisting only of 0 or 1, no other data.

Unit test - Algorithms

- Check whether the output of the alpha matte is composed of 0’s and 1’s.

- If the output matte has either all 0’s or all 1’s it is invalid. If the output matte has any other value, it is invalid.

- Testing whether the color of our extracted foreground changes when combined with the new background. Lastly, check if the algorithm for combining the background is correct.

Unit test - Test Quality

- SE_calculation
- PSNR_calculation
- SAD_calculation

Unit test - Test Trimap

- Test trimap is a function for testing the form for a trimap. The function checks if the value is between 0 and 1.

Unit test - Test Alpha

- This is a function test to compare two images to see if they are the same size.

Unit test - Test Window

- Test window is a function test for the different window sizes.

End to End test Quality Inspection

- To calculate the different quality assessments for the output of each image.
Laplacian

Function test for Laplacian matting.

### Results
Below the results of a few images are displayed. The output includes the input image, trimap, output alpha and composite image and provides insights into bayesian matting. The results have been generated based on the input parameters.

Input | Trimap | Output Alpha   |  Composite Image | SAD 
:---:|:---:|:---------:|:--------:|:---:
![](Input/GT01-input.png) |![](Trimap/GT01-trimap.png) |![](Output/GT01-output.png) |  ![](Composite/GT01-composite.png) | 2085.50
![](Input/GT02-input.png) |![](Trimap/GT02-trimap.png) |![](Output/GT02-output.png) |  ![](Composite/GT02-composite.png) | 9226.60
![](Input/GT03-input.png) |![](Trimap/GT03-trimap.png) |![](Output/GT03-output.png) |  ![](Composite/GT03-composite.png) | 9205.31
![](Input/GT05-input.png) |![](Trimap/GT05-trimap.png) |![](Output/GT05-output.png) |  ![](Composite/GT05-composite.png) | 2108.46
![](Input/GT06-input.png) |![](Trimap/GT06-trimap.png) |![](Output/GT06-output.png) |  ![](Composite/GT06-composite.png) | 5426.96
![](Input/GT07-input.png) |![](Trimap/GT07-trimap.png) |![](Output/GT07-output.png) |  ![](Composite/GT07-composite.png) | 4860.54
![](Input/GT08-input.png) |![](Trimap/GT08-trimap.png) |![](Output/GT08-output.png) |  ![](Composite/GT08-composite.png) | 28402.85
![](Input/GT09-input.png) |![](Trimap/GT09-trimap.png) |![](Output/GT09-output.png) |  ![](Composite/GT09-composite.png) | 7655.57
![](Input/GT11-input.png) |![](Trimap/GT11-trimap.png) |![](Output/GT11-output.png) |  ![](Composite/GT11-composite.png) | 9026.66

---
## Credits

This code was developed for purely academic purposes by Xiaoru Liu (github name: XiyunYue), Asrit Ganti(github name: asritganti), Reldean Williams(github name: Reldean-Williams), as part of the module EEP55C22-202223: COMPUTATIONAL METHODS.
Consultant: ChatGPT - https://openai.com/blog/chatgpt

https://github.com/XiyunYue/Harry-Potter-and-the-Matting-Muggles.git
