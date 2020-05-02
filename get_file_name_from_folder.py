import os
import csv
import pandas as pd

os.chdir("C:\\ZZZ\\CCC\\VVV") ## paste your folder path here from which you want to extract file names.

folder_name = "C:\\ZZZ\\CCC\\VVV"   ## paste a folder path where you want to download the data.
file_ = "file_output_data.csv"
file_path_name = folder_name + '\\' + file_ 

col = ['file_name', 'file_name_without_ext', 'file_ext']
df = pd.DataFrame(columns=col)

for i, f in enumerate(os.listdir()):
    f_name, f_ext = os.path.splitext(f)
    df.loc[i+1] = f, f_name, f_ext

df.to_csv(file_path_name)
print(f'Check you data here :{file_path_name}')
