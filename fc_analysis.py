# This is the analysis for the Fiddler's Cove Cochlodinium bloom that uses the generic functions defined in analyzepath.py

from analyzehsmis import analyzepath_folder, analyzecell_folder
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt


# calculate path duration, path length, path-averaged speed, and net to gross displacement ratio for four days of data
path24 = analyzepath_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/fiddlerscove/Fiddlers_20180724/*/*_path.csv')
path26 = analyzepath_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/fiddlerscove/Fiddlers_20180726/*/*_path.csv')
path30 = analyzepath_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/fiddlerscove/Fiddlers_20180730/*/*_path.csv')
path31 = analyzepath_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/fiddlerscove/Fiddlers_20180731/*/*_path.csv')


# get cell length and width for four days of data
cell24 = analyzecell_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/fiddlerscove/Fiddlers_20180724/*/*_focalcell.csv')
cell26 = analyzecell_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/fiddlerscove/Fiddlers_20180726/*/*_focalcell.csv')
cell30 = analyzecell_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/fiddlerscove/Fiddlers_20180730/*/*_focalcell.csv')
cell31 = analyzecell_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/fiddlerscove/Fiddlers_20180731/*/*_focalcell.csv')


# take results from above and combine into lists so that the mean, std, and SEM can be quickly found for each day (because a day has many tracks)
paths = [path24, path26, path30, path31]
cells = [cell24, cell26, cell30, cell31]
dates = ['Jul 24', 'Jul 26', 'Jul 30', 'Jul 31']

tswim_means = [np.mean(df['tswim']) for df in paths]
lswim_means = [np.mean(df['lswim']) for df in paths]
uave_means = [np.mean(df['uave']) for df in paths]
ngdr_means = [np.mean(df['ngdr']) for df in paths]
length_means = [np.mean(df['length']) for df in cells]
width_means = [np.mean(df['width']) for df in cells]

tswim_stdev = [np.std(df['tswim']) for df in paths]
lswim_stdev = [np.std(df['lswim']) for df in paths]
uave_stdev = [np.std(df['uave']) for df in paths]
ngdr_stdev = [np.std(df['ngdr']) for df in paths]
length_stdev = [np.std(df['length']) for df in cells]
width_stdev = [np.std(df['width']) for df in cells]

lswim_sem = [stats.sem(df['lswim']) for df in paths]
tswim_sem = [stats.sem(df['tswim']) for df in paths]
uave_sem = [stats.sem(df['uave']) for df in paths]
ngdr_sem = [stats.sem(df['ngdr']) for df in paths]
length_sem = [stats.sem(df['length']) for df in cells]
width_sem = [stats.sem(df['width']) for df in cells]


# calculate number of tracks in a sample
ntracks = [np.shape(sample)[0] for sample in paths]


# create a summary dataframe ()
hsmis = np.transpose(pd.DataFrame([dates, ntracks,
    length_means, length_stdev, width_means, width_stdev,
    tswim_means, tswim_stdev, lswim_means, lswim_stdev,
    uave_means, uave_stdev, ngdr_means, ngdr_stdev]))
hsmis.columns = ['date', 'sample size',
    'cell length (mm)', 'cell length stdev', 'cell width (mm)', 'cell width stdev',
    'case duration (s)', 'case duration stdev', 'path length (mm)', 'path length stdev',
    'path averaged speed (mm/s)', 'path averaged speed stdev', 'NGDR', 'NGDR stdev']
hsmis.to_csv('/Volumes/GoogleDrive/My Drive/projects/HSMIS/fiddlerscove/FCsummary.csv')


# plotting
plt.bar(range(0,4), uave_means, tick_label=dates, yerr=uave_sem)
plt.ylabel('Uave (mm/s)')

plt.bar(range(0,4), ngdr_means, tick_label=dates, yerr=ngdr_sem)
plt.ylabel('NGDR')


# due to sample size, I think you can only do statistics with the first 2 days
stats.ttest_ind(path24['uave'], path26['uave'], equal_var=True)
stats.ttest_ind(path24['ngdr'], path26['ngdr'], equal_var=True)