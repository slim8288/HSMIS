import pandas as pd
import numpy as np

def analyzepath(file):
    """ Input: file with the X and Y coordinates from a cell's path
        Output: path-averaged speed and net to gross displacement ratio
    """
    path = pd.read_csv(file)
    #need unit conversion from pixels

    nframes = np.shape(path)[0]
    tswim = (nframes-1)/2000.0 #camera fps

    pathlist = []
    for n in range(0,nframes-1):
        x1 = path.iloc[n]['X']
        y1 = path.iloc[n]['Y']
        x2 = path.iloc[n+1]['X']
        y2 = path.iloc[n+1]['Y']
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