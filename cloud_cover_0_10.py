import pandas as pd

master_OT = pd.read_csv('E:\master_OT.csv')
master_OT_cloud_010 = (master_OT[(master_OT['Scene Cloud Cover L1'] < 10)])
master_OT_cloud_010.to_csv(r'E:\master_OT_cloud_010.csv')

def cloud_cover_0_10 (file_path, res_filename):

    master = pd.read_csv(file_path)
    master_cloud_0_10 = (master[(master['Scene Cloud Cover L1'] < 10)])
   
    master_cloud_0_10.to_csv(res_filename) 


cloud_cover_0_10('E:\master_OT.csv','E:\master_OT_cloud_010.csv')
cloud_cover_0_10('E:\master_ETM.csv','E:\master_ETM_cloud_010.csv')
cloud_cover_0_10('E:\master_TM.csv','E:\master_TM_cloud_010.csv')