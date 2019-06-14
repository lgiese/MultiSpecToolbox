# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 21:21:28 2019

@author: RobindeVriesTheOcean
"""

import os
import cv2
import numpy as np
#from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import csv
import gdal
import PIL



imin        = 'test.tif'   # Specify the imput file name
# fixme: develop this into automatic dir/subdir reading


im = PIL.Image.open(imin)


# Load the separate bands and save them as image files
for i, page in enumerate(PIL.ImageSequence.Iterator(im)):
    page.save("page%d.png" % i)


# fixme: develop into automatic image page alignment?
