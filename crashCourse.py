import h5py
import matplotlib.pyplot as plt
import meep as mp
import numpy as np
import os

from matplotlib.colors import LinearSegmentedColormap

# set default resolution for images
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300

# set dark background color for all plots
plt.style.use('dark_background')

# set some custom color maps
cmap_alpha = LinearSegmentedColormap.from_list(
    'custom_alpha', [[1,1,1,0], [1,1,1,1]]
)
cmap_alpha = LinearSegmentedColormap.from_list(
    'custom_blue', [[0,0,0], [0,0.66,1], [1,1,1]]
)

