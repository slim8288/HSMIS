import pandas as pd
import numpy as np
from glob import glob
from scipy import signal, stats


def analyzepath(file):
    """ Input: file with the X and Y coordinates from a cell's path (_path.csv)
        Output: path-averaged speed in pixels/s and net to gross displacement ratio
    """
    path = pd.read_csv(file)

    nframes = np.shape(path)[0]
    tswim = (nframes-1)/2000.0 #camera fps

    #smooth X and Y coordinates with Savitzky-Golay filter; got window length and polynomial order from Houshuo
    #keeps same number of data points so nframes is still relevant
    smoothx = signal.savgol_filter(path['X'], 27, 4)
    smoothy = signal.savgol_filter(path['Y'], 27, 4)

    #creates a list with point to point distances
    pathlist = []
    for n in range(0,nframes-1):
        x1 = smoothx[n]
        y1 = smoothy[n]
        x2 = smoothx[n+1]
        y2 = smoothy[n+1]
        xsqd = (x2-x1)**2
        ysqd = (y2-y1)**2
        pathlist.append(np.sqrt(xsqd + ysqd))

    lswim = sum(pathlist) #aka gross displacement

    Uave = lswim/tswim

    xi = path.iloc[0]['X']
    yi = path.iloc[0]['Y']
    xf = path.iloc[-1]['X']
    yf = path.iloc[-1]['Y']
    xsqd = (xf-xi)**2
    ysqd = (yf-yi)**2
    ND = np.sqrt(xsqd + ysqd) #net displacement
    NGDR = ND/lswim

    return Uave, NGDR


def analyzepath_folder(directory):
    """ Input: folder with several files of the X and Y coordinates from a cell's path (_path.csv)
        Output: pandas series of path-averaged speed in mm/s and of net to gross displacement ratio
    """
    folder = glob(directory)
    Uave = []
    NGDR = []
    for file in folder:
        uave, ngdr = analyzepath(file)
        Uave.append(uave)
        NGDR.append(ngdr)
    Uave_series = pd.Series(Uave)*0.7/912.020 #912.020 pixels = 0.7 mm with lens used for Cochlodinium and Alexandrium
    NGDR_series = pd.Series(NGDR)
    return Uave_series, NGDR_series


Uave24, NGDR24 = analyzepath_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/fiddlerscove/Fiddlers_20180724/*/*_path.csv')
Uave26, NGDR26 = analyzepath_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/fiddlerscove/Fiddlers_20180726/*/*_path.csv')
Uave30, NGDR30 = analyzepath_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/fiddlerscove/Fiddlers_20180730/*/*_path.csv')
Uave31, NGDR31 = analyzepath_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/fiddlerscove/Fiddlers_20180731/*/*_path.csv')

Uaves = [Uave24, Uave26, Uave30, Uave31]
NGDRs = [NGDR24, NGDR26, NGDR30, NGDR31]
Uave_means = [np.mean(list) for list in Uaves]
NGDR_means = [np.mean(list) for list in NGDRs]
Uave_sem = [stats.sem(list) for list in Uaves]
NGDR_sem = [stats.sem(list) for list in NGDRs]

#plotting
labels = ['Jul 24', 'Jul 26', 'Jul 30', 'Jul 31']
plt.bar(range(0,4), Uave_means, tick_label=labels, yerr=Uave_sem)
plt.ylabel('Uave (mm/s)')

plt.bar(range(0,4), NGDR_means, tick_label=labels, yerr=NGDR_sem)
plt.ylabel('NGDR')

#due to sample size, I think you can only do statistics with the first 2 days
stats.ttest_ind(Uave24, Uave26, equal_var=True)
stats.ttest_ind(NGDR24, NGDR26, equal_var=True)
