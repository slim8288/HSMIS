# This is the analysis for the June 2019 nutrient replete vs. limited experiment that uses the generic functions defined in analyzehsmis.py

# lens conversion: 964.019 pixels = 0.7 mm

from analyzehsmis import analyzepath_folder, analyzecell_folder
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt


# calculate path duration, path length, path-averaged speed, and net to gross displacement ratio
path4 = analyzepath_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/nutrients/20190604/*/*_path.csv', pixels=964.019, mm=0.7)
path6 = analyzepath_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/nutrients/20190606/*/*_path.csv', pixels=964.019, mm=0.7)
path7 = analyzepath_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/nutrients/20190607/*/*_path.csv', pixels=964.019, mm=0.7)
path10 = analyzepath_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/nutrients/20190610/*/*_path.csv', pixels=964.019, mm=0.7)
path11 = analyzepath_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/nutrients/20190611/*/*_path.csv', pixels=964.019, mm=0.7)
path12 = analyzepath_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/nutrients/20190612/*/*_path.csv', pixels=964.019, mm=0.7)
path12dark = analyzepath_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/nutrients/20190612dark/*/*_path.csv', pixels=964.019, mm=0.7)


# get cell length and width
cell4 = analyzecell_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/nutrients/20190604/*/*_focalcell.csv', pixels=964.019, mm=0.7)
cell6 = analyzecell_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/nutrients/20190606/*/*_focalcell.csv', pixels=964.019, mm=0.7)
cell7 = analyzecell_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/nutrients/20190607/*/*_focalcell.csv', pixels=964.019, mm=0.7)
cell10 = analyzecell_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/nutrients/20190610/*/*_focalcell.csv', pixels=964.019, mm=0.7)
cell11 = analyzecell_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/nutrients/20190611/*/*_focalcell.csv', pixels=964.019, mm=0.7)
cell12 = analyzecell_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/nutrients/20190612/*/*_focalcell.csv', pixels=964.019, mm=0.7)
cell12dark = analyzecell_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/nutrients/20190612dark/*/*_focalcell.csv', pixels=964.019, mm=0.7)


# take results from above and combine into lists so that the mean, std, and SEM can be quickly found for each day (because a day has many tracks)
paths = [path4, path6, path7, path10, path11, path12, path12dark]
cells = [cell4, cell6, cell7, cell10, cell11, cell12, cell12dark]
dates = ['day0 inoc', 'day2 f/40', 'day3 f/2', 'day6 f/40', 'day7 f/2', 'day8 f/40', 'day8 f/40 dark']

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
#hsmis.to_csv('/Volumes/GoogleDrive/My Drive/projects/HSMIS/nutrients/nut_summary.csv')


# plotting
plt.bar(range(0, np.shape(uave_means)[0]), uave_means, tick_label=dates, yerr=uave_sem)
plt.ylabel('Uave (mm/s)')
plt.show()

plt.bar(range(0, np.shape(length_means)[0]), length_means, tick_label=dates, yerr=length_sem)
plt.ylabel('NGDR')
