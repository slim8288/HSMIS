# This is the analysis for the Fiddler's Cove Cochlodinium bloom that uses the generic functions defined in analyzepath.py
# written for python 3

# define functions
exec(open('./analyzepath.py').read())

# calculate speed and net to gross displacement for four days of data
Uave24, NGDR24 = analyzepath_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/fiddlerscove/Fiddlers_20180724/*/*_path.csv')
Uave26, NGDR26 = analyzepath_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/fiddlerscove/Fiddlers_20180726/*/*_path.csv')
Uave30, NGDR30 = analyzepath_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/fiddlerscove/Fiddlers_20180730/*/*_path.csv')
Uave31, NGDR31 = analyzepath_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/fiddlerscove/Fiddlers_20180731/*/*_path.csv')

# take results from above and combine into lists so that the mean and SEM can be found for each day (because a day has many tracks)
Uaves = [Uave24, Uave26, Uave30, Uave31]
NGDRs = [NGDR24, NGDR26, NGDR30, NGDR31]
Uave_means = [np.mean(list) for list in Uaves]
NGDR_means = [np.mean(list) for list in NGDRs]
Uave_sem = [stats.sem(list) for list in Uaves]
NGDR_sem = [stats.sem(list) for list in NGDRs]

# plotting
labels = ['Jul 24', 'Jul 26', 'Jul 30', 'Jul 31']
plt.bar(range(0,4), Uave_means, tick_label=labels, yerr=Uave_sem)
plt.ylabel('Uave (mm/s)')

plt.bar(range(0,4), NGDR_means, tick_label=labels, yerr=NGDR_sem)
plt.ylabel('NGDR')

# due to sample size, I think you can only do statistics with the first 2 days
stats.ttest_ind(Uave24, Uave26, equal_var=True)
stats.ttest_ind(NGDR24, NGDR26, equal_var=True)