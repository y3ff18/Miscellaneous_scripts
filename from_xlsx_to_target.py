#注释:
#这个脚本是从文件夹中遍历xls或者xlsx文件,从中寻找特定的目标
import pandas
import sys
import os
import argparse

arg = argparse.ArgumentParser()
arg.add_argument("-p","--path",help="Set Start Path")
arg.add_argument("-t","--target",help="Set Find Target")
parse = arg.parse_args()
def read_file(file):
    print(f"读取 {file} 至内存中...")
    pd = pandas.read_excel(file,sheet_name="Sheet1")
    for i in pd.index:
        # print(pd.loc[i].values[6])
        if str(parse.target) in pd.loc[i]:
            print(f"找到了 {file}")
            sys.exit()


for paths,dirs,files in os.walk(parse.path):
    for file in files:
        print()
        if "xls" in file[-5:-1] or "xlsx" in file[-5:-1]:
            read_file(file=file)
