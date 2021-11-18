import pandas as pd

df_table_PR = pd.read_csv(r'..\datasets\scenes_path_row.csv')
path_row_dict = {}

def extract_path_row (file_path, res_filename):
    df_landsat_masterdata = pd.read_csv(file_path)
    master_dataframe = pd.DataFrame(columns = df_landsat_masterdata.columns)
    print(len(master_dataframe))

    for row in df_table_PR.itertuples():
        path_row_dict[row[0]] = (row[1], row[2])

    for key, elem in path_row_dict.items():
        print("working on... " + str(elem))
        df_temp = ((df_landsat_masterdata[(df_landsat_masterdata["WRS Path"]==elem[0]) & (df_landsat_masterdata["WRS Row"]==elem[1])]))
        print(len(df_temp))
        master_dataframe = master_dataframe.append(df_temp)
        print(len(master_dataframe))
        master_dataframe.to_csv(res_filename)    



extract_path_row('..\datasets\master_data\LANDSAT_OT_C2_L2.csv', '..\datasets\\filtered_data\master_OT.csv')
extract_path_row('..\datasets\master_data\LANDSAT_TM_C2_L2.csv', '..\datasets\\filtered_data\master_TM.csv')
extract_path_row('..\datasets\master_data\LANDSAT_ETM_C2_L2.csv','..\datasets\\filtered_data\master_ETM.csv')