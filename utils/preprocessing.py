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



def resize_image(img_in, img_shape, resize_mode = cv2.INTER_LINEAR):
    """resize input image
    

    Parameters
    ----------
    img_in : 3D array of shape [h, w, c] 
        input image.
    img_shape : tuple or list 
        DESCRIPTION.
    resize_mode : TYPE, optional
        DESCRIPTION. The default is cv2.INTER_CUBIC.

    Returns
    -------
    None.

    """
    if not isinstance(img_in, np.ndarray):
        raise ValueError('Input must be an array.')
        
    if not isinstance(img_shape, list) or not isinstance(img_shape, tuple):
        img_shape = list(img_shape)

    resized_img = cv2.resize(img_in, (img_shape[0], img_shape[1]), interpolation=resize_mode)
    
    return resized_img


















