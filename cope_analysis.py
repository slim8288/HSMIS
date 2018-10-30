# This is the analysis for the A. minutum copepodamide experiments that uses the generic functions defined in analyzepath.py

from analyzehsmis import analyzepath_folder, analyzecell_folder
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt


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