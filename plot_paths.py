import pandas as pd
from glob import glob
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm


# modified from http://nbviewer.jupyter.org/github/dpsanders/matplotlib-examples/blob/master/colorline.ipynb
# Topics: line, color, LineCollection, cmap, colorline, codex
'''
Defines a function colorline that draws a (multi-)colored 2D line with coordinates x and y.
The color is taken from optional data in z, and creates a LineCollection.

z can be:
- empty, in which case a default coloring will be used based on the position along the input arrays
- a single number, for a uniform color [this can also be accomplished with the usual plt.plot]
- an array of the length of at least the same length as x, to color according to this data
- an array of a smaller length, in which case the colors are repeated along the curve

The function colorline returns the LineCollection created, which can be modified afterwards.

See also: plt.streamplot
'''


# Data manipulation:

def make_segments(x, y):
    '''
    Create list of line segments from x and y coordinates, in the correct format for LineCollection:
    an array of the form   numlines x (points per line) x 2 (x and y) array
    '''

    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    
    return segments


# Interface to LineCollection:

def colorline(x, y, z=None, cmap=plt.get_cmap('copper'), norm=plt.Normalize(0.0, 1.0), linewidth=3, alpha=1.0):
    '''
    Plot a colored line with coordinates x and y
    Optionally specify colors in the array z
    Optionally specify a colormap, a norm function and a line width
    '''
    
    # Default colors equally spaced on [0,1]:
    if z is None:
        z = np.linspace(0.0, 1.0, len(x))
           
    # Special case if a single number:
    if not hasattr(z, "__iter__"):  # to check for numerical input -- this is a hack
        z = np.array([z])
        
    z = np.asarray(z)
    
    segments = make_segments(x, y)
    lc = LineCollection(segments, array=z, cmap=cmap, norm=norm, linewidth=linewidth, alpha=alpha)
    
    ax = plt.gca()
    ax.add_collection(lc)
    
    return lc


########################


folder = glob('/Volumes/GoogleDrive/My Drive/data/hsmis/nutrients/20190612/*/*_path.csv')

# plot the entire path, moves pink to green
cmap = plt.get_cmap('PiYG')
for file in folder:
    path = pd.read_csv(file)
    y = path['Y'] * -1  # for some reason, the ImageJ analysis flips the track upside down
    colorline(path['X'], y, cmap=cmap)

plt.xlim(0, 500)
plt.ylim(-500, 0)


# plot the initial and final points
xi = []
yi = []
xf = []
yf = []
for file in folder:
    path = pd.read_csv(file)
    y = path['Y'] * -1 
    xi.append(path['X'].iloc[0])
    xf.append(path['X'].iloc[-1])
    yi.append(y.iloc[0])
    yf.append(y.iloc[-1])

plt.scatter(xi, yi, label='initial')
plt.scatter(xf, yf, label='final')
plt.legend()

