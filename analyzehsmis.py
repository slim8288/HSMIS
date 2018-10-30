import pandas as pd
import numpy as np
from glob import glob
from scipy import signal, stats

def analyzepath(file):
    """ Input: file with the X and Y coordinates from a cell's path (_path.csv)
        Output: path duration in s, path length in pixels, path-averaged speed in pixels/s,and net to gross displacement ratio
    """
    path = pd.read_csv(file)

    nframes = np.shape(path)[0]
    tswim = (nframes-1)/2000.0  # path duration  # camera fps = 2000

    # smooth X and Y coordinates with Savitzky-Golay filter; got window length and polynomial order from Houshuo
    # keeps same number of data points so nframes is still relevant
    smoothx = signal.savgol_filter(path['X'], 27, 4)
    smoothy = signal.savgol_filter(path['Y'], 27, 4)

    # creates a list with point to point distances
    pathlist = []
    for n in range(0,nframes-1):
        x1 = smoothx[n]
        y1 = smoothy[n]
        x2 = smoothx[n+1]
        y2 = smoothy[n+1]
        xsqd = (x2-x1)**2
        ysqd = (y2-y1)**2
        pathlist.append(np.sqrt(xsqd + ysqd))

    lswim = sum(pathlist)  # aka gross displacement or path length

    Uave = lswim/tswim  # path-averaged speed

    xi = path.iloc[0]['X']
    yi = path.iloc[0]['Y']
    xf = path.iloc[-1]['X']
    yf = path.iloc[-1]['Y']
    xsqd = (xf-xi)**2
    ysqd = (yf-yi)**2
    ND = np.sqrt(xsqd + ysqd)  # net displacement
    NGDR = ND/lswim

    return tswim, lswim, Uave, NGDR


def analyzepath_folder(directory):
    """ Input: folder with several files of the X and Y coordinates from a cell's path (_path.csv)
        Output: pandas dataframe with path duration in s, path length in mm, path-averaged speed in mm/s and of net to gross displacement ratio
    """
    folder = sorted(glob(directory))  # glob does not order, so if we want entries to match up between analyzepath_folder and analyzecell_folder, needs to be sorted
    tswim = []
    lswim = []
    Uave = []
    NGDR = []
    for file in folder:
        results = analyzepath(file)
        tswim.append(results[0])
        lswim.append(results[1] *0.7/912.020)  # conversion from pixels to mm for 20x lens
        Uave.append(results[2] *0.7/912.020)
        NGDR.append(results[3])
    summary = np.transpose(pd.DataFrame([tswim, lswim, Uave, NGDR]))
    summary.columns = ['tswim', 'lswim', 'uave', 'ngdr']
    return summary


def analyzecell_folder(directory):
    """ Input: folder with several files of cells' dimensions (_focalcell.csv)
        Output: pandas dataframe with cell length and width in mm
    """
    folder = sorted(glob(directory))  # glob does not order, so if we want entries to match up between analyzepath_folder and analyzecell_folder, needs to be sorted
    length = []
    width = []
    for file in folder:
        celldata = pd.read_csv(file)
        if 'L' in celldata:  # this first part is only necessary because of the csv formatting that I had done manually at the beginning of the FC analysis
            length.append(celldata['L'][0] *0.7/912.020)  # conversion from pixels to mm for 20x lens
            width.append(celldata['W'][0] *0.7/912.020)
        else:  # once I started using the macro, this is sufficient
            length.append(celldata['Roi_Length'][0] *0.7/912.020)
            width.append(celldata['Roi_Width'][0] *0.7/912.020)
    summary = np.transpose(pd.DataFrame([length, width]))
    summary.columns = ['length', 'width']
    return summary