import pandas as pd

lista_wybrane_sceny = pd.read_csv('E:\wybrane_sceny1.csv')

import csv
tablica_linkow=[]

with open('E:\wybrane_sceny.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        tablica_linkow.append(row['Browse Link'])


master_ETM = pd.read_csv('E:\master_ETM.csv')
dataframe_ETM = pd.DataFrame(columns = master_ETM.columns)

for link in tablica_linkow:
    df_temp= ((master_ETM[(master_ETM['Browse Link'] == link)]))
    if len(df_temp) != 0: 
        dataframe_ETM=dataframe_ETM.append(df_temp)
        print(len(dataframe_ETM))

dataframe_ETM.to_csv(r'E:\wybrane_sceny_ETM.csv')   


master_TM = pd.read_csv('E:\master_TM.csv')
dataframe_TM = pd.DataFrame(columns = master_TM.columns)

for link in tablica_linkow:
    df_temp= ((master_TM[(master_TM['Browse Link'] == link)]))
    if len(df_temp) != 0: 
        dataframe_TM=dataframe_TM.append(df_temp)
        print(len(dataframe_TM))

dataframe_TM.to_csv(r'E:\wybrane_sceny_TM.csv')


master_OT = pd.read_csv('E:\master_OT.csv')
dataframe_OT = pd.DataFrame(columns = master_OT.columns)

for link in tablica_linkow:
    df_temp= ((master_OT[(master_OT['Browse Link'] == link)]))
    if len(df_temp) != 0: 
        dataframe_OT=dataframe_OT.append(df_temp)
        print(len(dataframe_OT))

dataframe_OT.to_csv(r'E:\wybrane_sceny_OT.csv')


import os, glob
path = ('E:\wybrane_sceny')
all_files = glob.glob(os.path.join(path,"*.csv"))

all_df = []
for f in all_files:
    df = pd.read_csv(f,sep=',')
    df['file'] = f.split('/')[-1]
    all_df.append(df)
    
merged_df = pd.concat(all_df, ignore_index = True, sort = True)
merged_df.to_csv(r'E:\wybrane_sceny\wybr_sceny_OT_ETM_TM.csv')

