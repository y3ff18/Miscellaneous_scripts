import pandas
import sys
import os

def read_file(file):    
    print(f"读取 {file} 至内存中...")
    pd = pandas.read_excel(file,sheet_name="Sheet1")
    for i in pd.index:
        # print(pd.loc[i].values[6])
        if "33252519990618" in pd.loc[i].values[6]:
            print(f"找到了 {file}")
            sys.exit()


for paths,dirs,files in os.walk(r"C:\Users\Magic\Desktop\户籍数据1.03GB公安专用"):
    for file in files:
        read_file(file=file)