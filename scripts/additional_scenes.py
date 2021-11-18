import pandas as pd

#lista_wybrane_sceny = pd.read_csv('..\datasets\user_data\\additional_scenes\\additional_scenes_list.csv')

import csv
tablica_linkow=[]

with open('..\\datasets\\user_data\\additional_scenes\\additional_scenes_list.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        tablica_linkow.append(row['Browse Link'])


master_ETM = pd.read_csv('..\\datasets\\filtered_data\\master_ETM.csv')
dataframe_ETM = pd.DataFrame(columns = master_ETM.columns)

for link in tablica_linkow:
    df_temp= ((master_ETM[(master_ETM['Browse Link'] == link)]))
    if len(df_temp) != 0: 
        dataframe_ETM=dataframe_ETM.append(df_temp)
        print(len(dataframe_ETM))

dataframe_ETM.to_csv(r'..\\datasets\\user_data\\additional_scenes\\additional_scenes_merge\\additional_scenes_ETM.csv')   


master_TM = pd.read_csv('..\datasets\\filtered_data\master_TM.csv')
dataframe_TM = pd.DataFrame(columns = master_TM.columns)

for link in tablica_linkow:
    df_temp= ((master_TM[(master_TM['Browse Link'] == link)]))
    if len(df_temp) != 0: 
        dataframe_TM=dataframe_TM.append(df_temp)
        print(len(dataframe_TM))

dataframe_TM.to_csv(r'..\\datasets\\user_data\\additional_scenes\\additional_scenes_merge\\additional_scenes_TM.csv')


master_OT = pd.read_csv('..\\datasets\\filtered_data\\master_OT.csv')
dataframe_OT = pd.DataFrame(columns = master_OT.columns)

for link in tablica_linkow:
    df_temp= ((master_OT[(master_OT['Browse Link'] == link)]))
    if len(df_temp) != 0: 
        dataframe_OT=dataframe_OT.append(df_temp)
        print(len(dataframe_OT))

dataframe_OT.to_csv(r'..\\datasets\\user_data\\additional_scenes\\additional_scenes_merge\\additional_scenes_OT.csv')


import os, glob
path = ('..\\datasets\\user_data\\additional_scenes\\additional_scenes_merge')
all_files = glob.glob(os.path.join(path,"*.csv"))

all_df = []
for f in all_files:
    df = pd.read_csv(f,sep=',')
    df['file'] = f.split('/')[-1]
    all_df.append(df)
    
merged_df = pd.concat(all_df, ignore_index = True, sort = True)
merged_df.to_csv(r'..\\datasets\\user_data\\additional_scenes\\additional_secenes_OT_ETM_TM.csv')

