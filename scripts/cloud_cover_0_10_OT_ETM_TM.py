import os, glob
import pandas as pd

path = '..\datasets\\filtered_data\OT_ETM_TM_cloud_merge'
all_files = glob.glob(os.path.join(path,"*.csv"))

all_df = []
for f in all_files:
    df = pd.read_csv(f,sep=',')
    df['file'] = f.split('/')[-1]
    all_df.append(df)
    
merged_df = pd.concat(all_df, ignore_index = True, sort = True)

merged_df.to_csv(r'..\datasets\\filtered_data\\cloud_010_OT_ETM_TM.csv')

