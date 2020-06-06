# Moran's I calculation and visualization

Using Python to calculate Moran's I from TIFF-Images and visualizing the meaning of spatial autocorrelation.


[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/simon-donike/Morans_I/master)  
 
[![https://www.google.com/url?sa=i&url=https%3A%2F%2Fgithub.com%2Fjupyter%2Fnbviewer%2Fissues%2F714&psig=AOvVaw0UpwsrwSI22VWfHbXoAFb5&ust=1591560398633000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCMDzz9T-7ekCFQAAAAAdAAAAABAD](https://nbviewer.jupyter.org/github/simon-donike/Morans_I/blob/master/Morans_I.ipynb)


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
