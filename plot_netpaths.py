# Wanted to see if there was a bias in the net path of cells in the June 2019 nutrient experiment
# Plots the change in cell's coordinates with respect to a centered origin
    # e.g., (1,-4) would mean that the cell hasn't moved 1 unit right and 4 units down
# In response to qualitative observations of convection

import pandas as pd
from glob import glob
import numpy as np
import matplotlib.pyplot as plt


def netpath(folderpath):
    """ Input: path for the _path.csv files from HSMIS ImageJ analysis
        Output: 0) numpy array of initial x coordinates
                1) numpy array of final x coordinates
                2) numpy array of initial y coordinates
                3) numpy array of final y coordinates
    """
    folder = glob(folderpath)
    xi = np.array([])
    xf = np.array([])
    yi = np.array([])
    yf = np.array([])
    for file in folder:
        path = pd.read_csv(file)
        y = path['Y'] * -1  # for some reason, ImageJ flips the path upside down
        xi = np.append(xi, path['X'].iloc[0])
        xf = np.append(xf, path['X'].iloc[-1])
        yi = np.append(yi, y.iloc[0])
        yf = np.append(yf, y.iloc[-1])
    return xi, xf, yi, yf


folders = ['/Volumes/GoogleDrive/My Drive/data/hsmis/nutrients/20190604/*/*_path.csv',
    '/Volumes/GoogleDrive/My Drive/data/hsmis/nutrients/20190606/*/*_path.csv',
    '/Volumes/GoogleDrive/My Drive/data/hsmis/nutrients/20190607/*/*_path.csv',
    '/Volumes/GoogleDrive/My Drive/data/hsmis/nutrients/20190610/*/*_path.csv',
    '/Volumes/GoogleDrive/My Drive/data/hsmis/nutrients/20190611/*/*_path.csv',
    '/Volumes/GoogleDrive/My Drive/data/hsmis/nutrients/20190612/*/*_path.csv',
    '/Volumes/GoogleDrive/My Drive/data/hsmis/nutrients/20190612dark/*/*_path.csv',
    '/Volumes/GoogleDrive/My Drive/data/hsmis/nutrients/20190613/*/*_path.csv',
    '/Volumes/GoogleDrive/My Drive/data/hsmis/nutrients/20190613dark/*/*_path.csv',
    '/Volumes/GoogleDrive/My Drive/data/hsmis/nutrients/20190614/*/*_path.csv',
    '/Volumes/GoogleDrive/My Drive/data/hsmis/nutrients/20190614dark/*/*_path.csv']
descr = ['day0 inoc', 'day2 f/40', 'day3 f/2', 'day6 f/40', 'day7 f/2', 'day8 f/40', 'day8 f/40 dark',
    'day9 f/2', 'day9 f/2 dark', 'day10 f/40', 'day10 f/40 dark']

coord = [netpath(x) for x in folders]


plt.figure()
for n in range(0,11):
    plt.subplot(3,4,n+1)
    ax = plt.gca()
    xdiff = coord[n][1] - coord[n][0]
    ydiff = coord[n][3] - coord[n][2]
    plt.scatter(xdiff, ydiff)
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')
    plt.title(descr[n])
    plt.xlim(-900, 900)
    plt.ylim(-900, 900)
    plt.xticks([])
    plt.yticks([])
plt.suptitle('Net cell movement')
plt.show()

