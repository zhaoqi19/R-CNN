# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 22:43:46 2020

@author: qizhao
"""
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

import os
import cv2
import tools
import random
import numpy as np
import matplotlib.pyplot as plt

def test(image):
    plt.figure()
    plt.imshow(image)
    plt.show()

def resize_image(img_in, img_shape, resize_mode = cv2.INTER_LINEAR):
    """resize input image
    

    Parameters
    ----------
        img_in : 3D array of shape [h, w, c] 
            input image.
        img_shape : tuple or list 
            DESCRIPTION.
        resize_mode : string, optional
            Interpolation algorithm. The default is cv2.INTER_CUBIC.

    Returns
    -------
        Resized image.

    """
    if not isinstance(img_in, np.ndarray):
        raise ValueError('Input must be an array.')
        
    if not isinstance(img_shape, list) or not isinstance(img_shape, tuple):
        img_shape = list(img_shape)

    resized_img = cv2.resize(img_in, (img_shape[0], img_shape[1]), interpolation=resize_mode)
    
    return resized_img

def crop_image(img_in, rect):
    """
    

    Parameters
    ----------
    img_in : TYPE
        DESCRIPTION.
    rect : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    
    img = img_in.copy()
    x = rect[0]
    y = rect[1]
    w = rect[2]
    h = rect[3]
    x_1 = x + w
    y_1 = y + h
    return img[y:y_1, x:x_1, :], [x, y, x_1, y_1, w, h]
    


















