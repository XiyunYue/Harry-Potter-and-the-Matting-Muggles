# Copyright 2023 by Xiaoru Liu, Trinity College Dublin. All rights reserved.
#
# This file is the function for testing images color format and change them if there are not unit8
# ==================================================
"Create a function to test images color format"
import numpy as np


def change_SameColorform(image):
    '''
    input images, test the color format for it
    Args:
        image: numpy.ndarray
    Returns:
        outputs: numpy.ndarray
    '''
    b= cv2.imread('image16/background.jpg')

    # Get the original size of the image
    height, width = img_input.shape[:2]

    # Set the desired width and height for the resized image
    desired_width = 500
    aspect_ratio = desired_width / float(width)
    desired_height = int(height * aspect_ratio)

    # Resize the image
    resized_image = cv2.resize(b, (desired_width, desired_height))

    # Save the resized image
    cv2.imwrite('resized_image.jpg', resized_image)
    

    return image
