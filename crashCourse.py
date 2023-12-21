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

def label_plot(ax, title=None, xlabel=None, ylabel=None, elapsed=None):
    """
    Add a title and x/y labels to the plot.
    """
    if title:
        ax.set_title(title)
    elif elapsed is not None:
        ax.set_title(f'{elapsed:0.1f} fs')
    if xlabel is not False:
        ax.set_xlabel('x (μm)'if ylabel is None else xlabel)
    if ylabel is not False:
        ax.set_ylabel('y (μm)'if ylabel is None else ylabel)
