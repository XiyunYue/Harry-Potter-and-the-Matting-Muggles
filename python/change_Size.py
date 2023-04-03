# Copyright 2023 by Xiaoru Liu, Trinity College Dublin. All rights reserved.
#
# This file is the function for change alpha colour matrix become to one channel format
# ==================================================
"Create a function to change colour to one channel format"

def change_Size(image):
    '''
    input images, test the color format for it and change three channel to one channel format
    Args:
        image: numpy.ndarray
    Returns:
        outputs: numpy.ndarray
    '''
    ndim = image.ndim
    if ndim == 3:
        image = image[:, :, 0]

    return image
