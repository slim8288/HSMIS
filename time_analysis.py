# Wanted to see whether there is a correlation between swimming speed and time of recording in the nutrient experiment
# Uses the generic functions defined in analyzehsmis.py

# lens conversion: 964.019 pixels = 0.7 mm

from analyzehsmis import analyzepath_folder, analyzecell_folder
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt


def hourbin(date):
    """ Input: date of recording
        Output: dataframe with analyzed path data for that day of recording,
        with each row as an hour.
    """
    # calculate path duration, path length, path-averaged speed, and net to gross displacement ratio
    path10 = analyzepath_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/nutrients/' + date + '/*_10*/*_path.csv', pixels=964.019, mm=0.7)
    path11 = analyzepath_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/nutrients/' + date + '/*_11*/*_path.csv', pixels=964.019, mm=0.7)
    path12 = analyzepath_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/nutrients/' + date + '/*_12*/*_path.csv', pixels=964.019, mm=0.7)
    path13 = analyzepath_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/nutrients/' + date + '/*_13*/*_path.csv', pixels=964.019, mm=0.7)
    path14 = analyzepath_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/nutrients/' + date + '/*_14*/*_path.csv', pixels=964.019, mm=0.7)
    path15 = analyzepath_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/nutrients/' + date + '/*_15*/*_path.csv', pixels=964.019, mm=0.7)
    path16 = analyzepath_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/nutrients/' + date + '/*_16*/*_path.csv', pixels=964.019, mm=0.7)

    # take results from above and combine into lists so that the mean, std, and SEM can be quickly found for each day (because a day has many tracks)
    paths = [path10, path11, path12, path13, path14, path15, path16]
    hours = [10, 11, 12, 13, 14, 15, 16]

    tswim_means = [np.mean(df['tswim']) for df in paths]
    lswim_means = [np.mean(df['lswim']) for df in paths]
    uave_means = [np.mean(df['uave']) for df in paths]
    ngdr_means = [np.mean(df['ngdr']) for df in paths]

    tswim_stdev = [np.std(df['tswim']) for df in paths]
    lswim_stdev = [np.std(df['lswim']) for df in paths]
    uave_stdev = [np.std(df['uave']) for df in paths]
    ngdr_stdev = [np.std(df['ngdr']) for df in paths]

    lswim_sem = [stats.sem(df['lswim']) for df in paths]
    tswim_sem = [stats.sem(df['tswim']) for df in paths]
    uave_sem = [stats.sem(df['uave']) for df in paths]
    ngdr_sem = [stats.sem(df['ngdr']) for df in paths]


    # calculate number of tracks in a sample
    ntracks = [np.shape(sample)[0] for sample in paths]

    hsmis = np.transpose(pd.DataFrame([hours, ntracks,
        tswim_means, tswim_stdev, lswim_means, lswim_stdev,
        uave_means, uave_stdev, ngdr_means, ngdr_stdev]))
    hsmis.columns = ['hour', 'sample size',
        'case duration (s)', 'case duration stdev', 'path length (mm)', 'path length stdev',
        'path averaged speed (mm/s)', 'path averaged speed stdev', 'NGDR', 'NGDR stdev']

    return hsmis


dates = ['20190225','20190226', '20190227', '20190228', '20190301',
    '20190302', '20190304', '20190305', '20190306', '20190307']
descr = ['day 0 inoculum', 'day 1 f/40', 'day 2 f/40', 'day 3 f/2', 'day 4 f/40',
    'day 5 f/2', 'day 7 f/40', 'day 8 f/2', 'day 9 f/2', 'day 10 f/40']
alldata = [hourbin(x) for x in dates]


# plotting speed for each day
plt.figure()
for n in range(0,10):
    plt.subplot(3,4,n+1)
    plt.bar(alldata[n]['hour'], alldata[n]['path averaged speed (mm/s)'], tick_label=alldata[n]['hour'], yerr=alldata[n]['path averaged speed stdev'])
    plt.ylabel('Uave (mm/s)')
    plt.title(descr[n])
plt.show()


# plotting number of tracks for each day
plt.figure()
for n in range(0,10):
    plt.subplot(3,4,n+1)
    plt.bar(alldata[n]['hour'], alldata[n]['sample size'], tick_label=alldata[n]['hour'])
    plt.ylabel('# tracks')
    plt.title(descr[n])
plt.show()

