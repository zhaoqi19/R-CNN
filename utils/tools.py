# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 21:04:49 2020

@author: qizhao
"""
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

import sys
import cv2
import math
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


def progress_bar(message, filled_nums, filled_total):
    """progress bar when the script is working
        
    Parameters
    ----------
        message : string
            displayed mission name.
        filled_nums : number
            DESCRIPTION.
        filled_total : number
            DESCRIPTION.

    Returns
    -------
        A progress bar.

    """
    
    filled_rate = filled_nums / filled_total
    filled_length = int(filled_rate * 50)
    empty_length = 50 - filled_length
    _filled_rate = math.ceil(filled_rate * 100)
    
    result = '\r%s: [%s%s]%d%%\t%d/%d' %(message, "#"*filled_length, ' '*empty_length, _filled_rate, filled_nums, filled_total,)
    sys.stdout.write(result)
    sys.stdout.flush()



def display_rect(img_path, regions):
    """Display the rectangle of bounding box
    

    Parameters
    ----------
        img_path : string
            Input image path.
        regions : list
            coorbinate of bounding box.

    Returns
    -------
        image.

    """
    
    figure, axis = plt.subplots(nrows=1, ncols=1, figsize=(8, 6))
    try:
        bgr_img = cv2.imread(img_path)
        rgb_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2RGB)
    except:
        raise ValueError('Cannot read image, check input path!')
    axis.imshow(rgb_img)
    rect = mpatches.Rectangle((regions[0], regions[1]), width=regions[2], height=regions[3], 
                              fill=False, color='red', linewidth=1.25)
    axis.add_patch(rect)
    
    plt.show()
    
    
      