from os import lseek
import pandas as pd

path_row = pd.read_csv('..\datasets\scenes_path_row.csv')
cloud_0_10 = pd.read_csv('..\datasets\\filtered_data\cloud_010_OT_ETM_TM.csv')

path_row_dict = {}
for index, columns in path_row.iterrows():
    print("done for index: " + str(index))
    path_row_dict[index] = (columns['WRS Path'], columns['WRS Row'])

for pr_tuple in path_row_dict.values():
    print(pr_tuple)
    currentScene = (cloud_0_10[(cloud_0_10["WRS Path"] == pr_tuple[0]) & (cloud_0_10["WRS Row"] == pr_tuple[1])])
    currentScene.to_csv(r'..\datasets\\filtered_data\scenes\\pr_{}_{}.csv'.format(pr_tuple[0], pr_tuple[1]))
    df_currentView = currentScene[['Browse Link','Date Acquired','Scene Cloud Cover L1','Sun Azimuth L0RA','Sun Azimuth L1','Sun Elevation L0RA','Sun Elevation L1']]
    df_currentView.to_csv(r'..\datasets\\filtered_data\scenes_df\df_{}_{}.csv'.format(pr_tuple[0], pr_tuple[1]))



