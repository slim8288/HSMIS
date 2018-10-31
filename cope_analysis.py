# This is the analysis for the A. minutum copepodamide experiments that uses the generic functions defined in analyzepath.py

from analyzehsmis import analyzepath_folder, analyzecell_folder
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

# read in data and calculate basic parameters
# control
control3p = analyzepath_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/copepodamide/20181017/control*/*_path.csv')
control5p = analyzepath_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/copepodamide/20181019/control*/*_path.csv')
control3c = analyzecell_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/copepodamide/20181017/control*/*_focalcell.csv')
control5c = analyzecell_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/copepodamide/20181019/control*/*_focalcell.csv')

# single dose
sdmso2p = analyzepath_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/copepodamide/20181016/sdmso*/*_path.csv')
sdmsoxp = analyzepath_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/copepodamide/20181018/sdmso*/*_path.csv')
sdmsoyp = analyzepath_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/copepodamide/20181022/SDMSO*/*_path.csv')
sdmso2c = analyzecell_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/copepodamide/20181016/sdmso*/*_focalcell.csv')
sdmsoxc = analyzecell_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/copepodamide/20181018/sdmso*/*_focalcell.csv')
sdmsoyc = analyzecell_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/copepodamide/20181022/SDMSO*/*_focalcell.csv')

scope2p = analyzepath_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/copepodamide/20181016/scope*/*_path.csv')
scopexp = analyzepath_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/copepodamide/20181018/scope*/*_path.csv')
scopeyp = analyzepath_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/copepodamide/20181022/Scope*/*_path.csv')
scope2c = analyzecell_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/copepodamide/20181016/scope*/*_focalcell.csv')
scopexc = analyzecell_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/copepodamide/20181018/scope*/*_focalcell.csv')
scopeyc = analyzecell_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/copepodamide/20181022/Scope*/*_focalcell.csv')

# daily does
ddmso3p = analyzepath_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/copepodamide/20181017/ddmso*/*_path.csv')
ddmso5p = analyzepath_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/copepodamide/20181019/ddmso*/*_path.csv')
ddmso3c = analyzecell_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/copepodamide/20181017/ddmso*/*_focalcell.csv')
ddmso5c = analyzecell_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/copepodamide/20181019/ddmso*/*_focalcell.csv')

dcope3p = analyzepath_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/copepodamide/20181017/dcope*/*_path.csv')
dcope5p = analyzepath_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/copepodamide/20181019/dcope*/*_path.csv')
dcope3c = analyzecell_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/copepodamide/20181017/dcope*/*_focalcell.csv')
dcope5c = analyzecell_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/copepodamide/20181019/dcope*/*_focalcell.csv')


"""
Note that when I designed this experiment, the first day of exposure 10/15/18 was "Day 1" and that is reflected in the file naming.
Thursday 10/18 became X when I readid the single dose experiment, Monday 10/22 became Y from that same single dosing.
For the purposes of analysis, I will need to express in terms of days since exposure: all the numbered will become one less, X = 0, Y = 4.
I guess control is always day 0??
"""

# path analysis
paths = [control3p, control5p, sdmsoxp, sdmso2p, sdmsoyp, scopexp, scope2p, scopeyp, ddmso3p, ddmso5p, dcope3p, dcope5p]
treatment = ['control', 'control', 'S DMSO', 'S DMSO', 'S DMSO', 'S cope', 'S cope', 'S cope', 'D DMSO', 'D DMSO', 'D cope', 'D cope']
day = [0, 0, 0, 1, 4, 0, 1, 4, 2, 4, 2, 4]
absoluteday = [2, 4, 3, 1, 7, 3, 1, 7, 2, 4, 2, 4]
labels = []
for n in range(0, np.shape(treatment)[0]):
    labels.append(treatment[n] + ' ' + str(day[n]))

tswim_means = [np.mean(df['tswim']) for df in paths]
lswim_means = [np.mean(df['lswim']) for df in paths]
uave_means = [np.mean(df['uave']) for df in paths]
ngdr_means = [np.mean(df['ngdr']) for df in paths]

lswim_sem = [stats.sem(df['lswim']) for df in paths]
tswim_sem = [stats.sem(df['tswim']) for df in paths]
uave_sem = [stats.sem(df['uave']) for df in paths]
ngdr_sem = [stats.sem(df['ngdr']) for df in paths]


plt.barh(range(0,12), uave_means, tick_label=labels, xerr=uave_sem)
plt.xlabel('Uave (mm/s)')

plt.barh(range(0,12), ngdr_means, tick_label=labels, xerr=ngdr_sem)
plt.xlabel('NGDR')

plt.scatter(day[0:2], uave_means[0:2], label='control')
plt.scatter(day[2:5], uave_means[2:5], label='S DMSO')
plt.scatter(day[5:8], uave_means[5:8], label='S cope')
plt.scatter(day[8:10], uave_means[8:10], label='S DMSO')
plt.scatter(day[10:12], uave_means[10:12], label='D cope')
plt.legend()
plt.xlabel('Days since exposure')
plt.ylabel('Uave (mm/s)')

plt.scatter(day[0:2], ngdr_means[0:2], label='control')
plt.scatter(day[2:5], ngdr_means[2:5], label='S DMSO')
plt.scatter(day[5:8], ngdr_means[5:8], label='S cope')
plt.scatter(day[8:10], ngdr_means[8:10], label='S DMSO')
plt.scatter(day[10:12], ngdr_means[10:12], label='D cope')
plt.legend()
plt.xlabel('Days since exposure')
plt.ylabel('NGDR')


# cell size analysis
cells = [control3c, control5c, sdmsoxc, sdmso2c, sdmsoyc, scopexc, scope2c, scopeyc, ddmso3c, ddmso5c, dcope3c, dcope5c]

length_means = [np.mean(df['length']) for df in cells]
width_means = [np.mean(df['width']) for df in cells]

length_sem = [stats.sem(df['length']) for df in cells]
width_sem = [stats.sem(df['width']) for df in cells]

plt.barh(range(0,12), length_means, tick_label=labels, xerr=length_sem)
plt.xlabel('Cell length (mm)')