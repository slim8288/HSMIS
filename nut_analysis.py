# This is the analysis for the nutrient replete vs. limited experiment that uses the generic functions defined in analyzepath.py

from analyzehsmis import analyzepath_folder, analyzecell_folder
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt


# calculate path duration, path length, path-averaged speed, and net to gross displacement ratio for four days of data
path25 = analyzepath_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/nutrients/20190225/*/*_path.csv')
path26 = analyzepath_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/nutrients/20190226/*/*_path.csv')
path27 = analyzepath_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/nutrients/20190227/*/*_path.csv')
path28 = analyzepath_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/nutrients/20190228/*/*_path.csv')
path1 = analyzepath_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/nutrients/20190301/*/*_path.csv')
path2 = analyzepath_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/nutrients/20190302/*/*_path.csv')
path4 = analyzepath_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/nutrients/20190304/*/*_path.csv')
path5 = analyzepath_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/nutrients/20190305/*/*_path.csv')
path6 = analyzepath_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/nutrients/20190306/*/*_path.csv')
path7 = analyzepath_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/nutrients/20190307/*/*_path.csv')
path8 = analyzepath_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/nutrients/20190308/*/*_path.csv')



# get cell length and width for four days of data
cell25 = analyzecell_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/nutrients/20190225/*/*_focalcell.csv')
cell26 = analyzecell_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/nutrients/20190226/*/*_focalcell.csv')
cell27 = analyzecell_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/nutrients/20190227/*/*_focalcell.csv')
cell28 = analyzecell_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/nutrients/20190228/*/*_focalcell.csv')
cell1 = analyzecell_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/nutrients/20190301/*/*_focalcell.csv')
cell2 = analyzecell_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/nutrients/20190302/*/*_focalcell.csv')
cell4 = analyzecell_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/nutrients/20190304/*/*_focalcell.csv')
cell5 = analyzecell_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/nutrients/20190305/*/*_focalcell.csv')
cell6 = analyzecell_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/nutrients/20190306/*/*_focalcell.csv')
cell7 = analyzecell_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/nutrients/20190307/*/*_focalcell.csv')
cell8 = analyzecell_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/nutrients/20190308/*/*_focalcell.csv')


# take results from above and combine into lists so that the mean, std, and SEM can be quickly found for each day (because a day has many tracks)
paths = [path25, path26, path27, path28, path1, path2, path4, path5, path6, path7, path8]
cells = [cell25, cell26, cell27, cell28, cell1, cell2, cell4, cell5, cell6, cell7, cell8]
dates = ['innoculum', 'f/40', 'f/40', 'f/2', 'f/40', 'f/2', 'f/40', 'f/2', 'f/40', 'f/2', 'f/40']

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





################# end




plt.bar(range(0, np.shape(ngdr_means)[0]), ngdr_means, tick_label=dates, yerr=ngdr_sem)
plt.ylabel('NGDR')


# statistics
stats.ttest_ind(path24['uave'], path26['uave'], equal_var=True)
stats.ttest_ind(path24['ngdr'], path26['ngdr'], equal_var=True)