import argparse
import os,sys
import random
import time as t
import module.GetItemFromCSV as GIFC
import module.VisualizationModule as VLM
import pandas as pd

# 方法文档https://blog.csdn.net/houyanhua1/article/details/87809185
# 进度条文档https://blog.csdn.net/weixin_46089319/article/details/107406269
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--file', type=str, default='/src/list.csv')
parser.add_argument('--target_path', type=str)
args = parser.parse_args()

class Traversal:
    def ShowResult(self):
        testDict = {'ID': '', 'Name': '', 'Times': '', 'PreviousDate': ''}
        pandas_table = GIFC.GetItemFromCSV(args.file)


        for i in pandas_table[['Name']].itertuples():
            print(i.code, i.stock_url)





if __name__ == '__main__':

    print(" Traversal Becall")
    T = Traversal()
    T.ShowResult()
