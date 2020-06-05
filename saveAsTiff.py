#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 18:34:53 2020

@author: simondonike
"""

"""
import pandas as pd
import numpy as np
import Image



image_matrix = pd.read_csv("data/ImageMtrx.csv",delimiter=";",index_col="index")
image_matrix_random =pd.read_csv("data/ImageMtrx_random.csv",delimiter=";",index_col="index")

image_matrix_np = np.asarray(image_matrix)
image_matrix_random_np = np.asarray(image_matrix_random)

data = image_matrix_np
im = Image.fromarray(data)
im.save('test.tif')

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


dpi = 100 # Arbitrary. The number of pixels in the image will always be identical
data = pd.read_csv("/Users/simondonike/Documents/GitHub/MoransI_tiff/data/ImageMtrx.csv",delimiter=";",index_col="index")
#data = np.random.randint(0,255,size=(10000,10000))
data = pd.DataFrame(data)

#data = np.random.random((10, 10))
height, width = np.array(data.shape, dtype=float) / dpi


fig = plt.figure(figsize=(width, height), dpi=dpi)
ax = fig.add_axes([0, 0, 1, 1])
ax.axis('off')

ax.imshow(data, interpolation='none', cmap="gray")
fig.savefig('ImageMtrx.tiff', dpi=dpi, edgecolor = "none")
print("DONE!")