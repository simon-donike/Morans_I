#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 20:43:07 2020

@author: simondonike
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dpi = 100 # Arbitrary. The number of pixels in the image will always be identical


"""
#Read csv File
data = pd.read_csv("linc_seg.csv",delimiter=";",index_col="index")
"""



def random(size): #RANDOM
    data = np.random.randint(0,255,size=(size,size))
    print("Numpy array created")
    return data

def chessboard_style(size): #CHESS
    x = np.ones((3,3))
    x = np.zeros((size,size),dtype=int)
    x[1::2,::2] = 1
    x[::2,1::2] = 1
    data = np.where(x==1, 255, x)
    print("Numpy array created")
    return data


def half_half(size):
    a = np.full((int(size/2),size),255)
    b = np.full((int(size/2),size),0)
    data = np.concatenate((a, b))
    return data
    

size = 100
output_file = "chess.tif"

"""Coose which style here"""
data = pd.DataFrame(chessboard_style(size)) 
print("Numpy converted to dataframe")




#data = np.random.random((10, 10))
height, width = np.array(data.shape, dtype=float) / dpi


fig = plt.figure(figsize=(width, height), dpi=dpi)
ax = fig.add_axes([0, 0, 1, 1])
ax.axis('off')

ax.imshow(data, interpolation='none', cmap="gray")
fig.savefig(output_file, dpi=dpi, edgecolor = "none")
print("DONE!")


