#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 18:32:44 2020

@author: simondonike
"""

import pysal
from skimage.io import imread
from libpysal.weights import lat2W
import numpy as np
import pandas as pd
from esda.moran import Moran
from skimage.color import rgb2gray
from splot.esda import moran_scatterplot
import matplotlib.pyplot as Mplt
#import matplotlib.image as mamag

# I started off with a tiff image, converted it to greyscale and
# then proceeded to Moran I value without converting it into shapefile.
# Because a shape file has a lot of info including tags lat, long. population and much more meant for geography

rasterImage = imread(r'data/ImageMtrx_random.tiff')

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

rasterImageGrey = rgb2gray(rasterImage)
col,row = rasterImageGrey.shape[:2]
df = pd.DataFrame(rasterImageGrey.flatten())
WeightMatrix= lat2W(row,col)
WeightMatrix = lat2W(rasterImageGrey.shape[0],rasterImageGrey.shape[1])
MoranM= Moran(rasterImageGrey,WeightMatrix)
fig, ax = moran_scatterplot(MoranM, aspect_equal=True)

#print("Raster Dimension:{}".format(rasterImageGrey.shape))
print("Moran's I Value:%f"%MoranM.I)
Mplt.show()