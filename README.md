# Moran's I calculation and visualization

Using Python to calculate Moran's I from TIFF-Images and visualizing the meaning of spatial autocorrelation.


[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/simon-donike/Morans_I/master)  
[![nbviewer](https://camo.githubusercontent.com/bfeb5472ee3df9b7c63ea3b260dc0c679be90b97/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f72656e6465722d6e627669657765722d6f72616e67652e7376673f636f6c6f72423d66333736323626636f6c6f72413d346434643464)](https://nbviewer.jupyter.org/github/simon-donike/Morans_I/blob/master/Morans_I.ipynb) 
 



**Moran's I Requirements:**


For the installation of the libraries and to avoid dependency issues, it is recommended that you:
1. Use Anaconda and the conda forge channel for the installation of all libraries
2. Set up an new environment and install the libraries within

Libraries used:
-numpy
-pandas
-scikit-image
-pysal
-libpysal
-geopandas
-pandana & urbanaccess (conda install -c udst pandana urbanaccess)
-conda install -c conda-forge esda
-conda install -c conda-forge splot



It is recommended to use Anaconda (+ conda-forge) for the installation of these libraries.
Alternatively, "pip install" can be used. It is not recommended to mix lib installations from
different channels.  
For more information, read the notes at the beginning of the Jupyter Notebook
