import os
import pandas as pd

df = pd.read_csv('file path') ## uploaded csv file path. csv in which their will 
                              ## be only two columns 1st old file name and 2nd modified or changed file name
                              ## column should be exact "old_name" and "new_file_name"

os.chdir("C:\\CCCC\\PPP\\UUUU")  ## folder path where you want to change file name

old_file_name = df['old_name'].tolist()
new_name_list = df['new_file_name'].tolist()

for f in os.listdir():
    if f in old_file_name:
        i = old_file_name.index(f)
        os.rename(f,new_name_list[i])
    else:
        pass

print("File name is changed....")
