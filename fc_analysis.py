# This is the analysis for the Fiddler's Cove Cochlodinium bloom that uses the generic functions defined in analyzepath.py
# written for python 3

# define functions
exec(open('./analyzepath.py').read())

# calculate path duration, path length, path-averaged speed, and net to gross displacement ratio for four days of data
path24 = analyzepath_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/fiddlerscove/Fiddlers_20180724/*/*_path.csv')
path26 = analyzepath_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/fiddlerscove/Fiddlers_20180726/*/*_path.csv')
path30 = analyzepath_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/fiddlerscove/Fiddlers_20180730/*/*_path.csv')
path31 = analyzepath_folder('/Volumes/GoogleDrive/My Drive/data/hsmis/fiddlerscove/Fiddlers_20180731/*/*_path.csv')

# take results from above and combine into a single list so that the mean, std, and SEM can be quickly found for each day (because a day has many tracks)
paths = [path24, path26, path30, path31]
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

# plotting
labels = ['Jul 24', 'Jul 26', 'Jul 30', 'Jul 31']
plt.bar(range(0,4), uave_means, tick_label=labels, yerr=uave_sem)
plt.ylabel('Uave (mm/s)')

plt.bar(range(0,4), ngdr_means, tick_label=labels, yerr=ngdr_sem)
plt.ylabel('NGDR')

# due to sample size, I think you can only do statistics with the first 2 days
stats.ttest_ind(uave24, uave26, equal_var=True)
stats.ttest_ind(ngdr24, ngdr26, equal_var=True)