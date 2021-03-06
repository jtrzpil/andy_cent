import pandas as pd

def cloud_cover_0_10 (file_path, res_filename):

    master = pd.read_csv(file_path)
    master_cloud_0_10 = (master[(master['Scene Cloud Cover L1'] < 10)])

    master_cloud_0_10.to_csv(res_filename) 

cloud_cover_0_10('..\datasets\\filtered_data\master_OT.csv','..\datasets\\filtered_data\OT_ETM_TM_cloud_merge\master_OT_cloud_010.csv')
cloud_cover_0_10('..\datasets\\filtered_data\master_ETM.csv','..\datasets\\filtered_data\OT_ETM_TM_cloud_merge\master_ETM_cloud_010.csv')
cloud_cover_0_10('..\datasets\\filtered_data\master_TM.csv','..\datasets\\filtered_data\OT_ETM_TM_cloud_merge\master_TM_cloud_010.csv')
