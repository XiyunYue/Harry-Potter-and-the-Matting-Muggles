# Copyright 2023 by Xiaoru Liu, Trinity College Dublin. All rights reserved.
#
# This file is the function for testing images color format and change them if there are not unit8
# ==================================================
"Create a function to design backgrounds for different pictures."
import cv2
import numpy as np


def change_background(image, background):
    '''
    input background images and change it to the same size with input image
    Args:
        image: numpy.ndarray
        background: numpy.ndarray
    Returns:
        outputs: numpy.ndarray
    '''
    i, j, k = image.shape

    # Get the original size of the image
    height, width = image.shape[:2]

    # # Set the desired width and height for the resized image
    # desired_width = 500
    # aspect_ratio = desired_width / float(width)
    # desired_height = int(height * aspect_ratio)

    # Resize the image
    resized_image = cv2.resize(background, (width, height))

    # Save the resized image
    # cv2.imwrite('background.jpg', resized_image)
    return resized_image
