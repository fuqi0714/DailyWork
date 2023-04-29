import argparse
import os
import random
import time as t
import module.GetItemFromCSV as GIFC
import module.VisualizationModule as VLM
import pandas as pd

# 方法文档https://blog.csdn.net/houyanhua1/article/details/87809185
# 进度条文档https://blog.csdn.net/weixin_46089319/article/details/107406269
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--file', type=str, required=True)
parser.add_argument('--nums', type=int, default=1)
parser.add_argument('--RandomSelect', action='store_true')
parser.add_argument('--Visualization', action='store_true')
args = parser.parse_args()


class RandomID:

    '''
        def RandomList(self,pandas_table):
            RandomListValue=[]
            for i in range ( args.nums):
                n = self.RandomNum(len(pandas_table))
                for j in RandomListValue:
                    if j!=n:
                        RandomListValue.append(n)
                    else:
                        return

            return RandomListValue
    '''

    def ShowResult(self):
        testDict = {'ID': '', 'Name': '', 'Times': '', 'PreviousDate': ''}
        pandas_table = GIFC.GetItemFromCSV(args.file)
        n = self.RandomNum(len(pandas_table))
        testDict['ID'] = pandas_table[n:n + 1][["ID"]].to_string(index=False, header=0)
        testDict['Name'] = pandas_table[n:n + 1][["Name"]].to_string(index=False, header=0)
        times = pandas_table[n:n + 1][["Times"]] + 1
        testDict['Times'] = times.to_string(index=False, header=0)

        testDict['PreviousDate'] = pandas_table[n:n + 1][["PreviousDate"]].to_string(index=False, header=0)
        currentDate=self.GetCurrentDate()
        print(testDict)
        self.WriteBack(n, pandas_table, times,currentDate)

    def WriteBack(self, number, pandas_table, times,currentDate):
        pandas_table.loc[number, 'Times'] = times.to_string(index=False, header=0)
        pandas_table.loc[number, 'PreviousDate'] = currentDate
        pandas_table.to_csv(args.file, header=None, index=None)
        file = os.path.split(args.file)[1]
        pandas_table.to_csv('src/' + file, header=None, index=None)
        print("Write back over and update")
        '''
        mix path
        if os.path.exists(file_path):
            pandas_table.to_csv(args.file,header=None,index=None)
            #print(os.path.join(file_path,args.file))
            
        '''

    def RelativePathUpdate(self, pandas_table):
        pandas_table.to_csv(args.file, header=None, index=None)

    def GetCurrentDate(self):
        time=t.strftime("%Y-%m-%d %H:%M:%S", t.localtime())
        return time

    def RandomNum(self, x):
        n = random.randint(0, x - 1)
        return n

    def GenerateDictObj(self):
        temptDict = {'': ''}
        return temptDict


if __name__ == '__main__':
    if args.RandomSelect:
        RID = RandomID()
        RID.ShowResult()
    elif args.Visualization:
        VLD=VLM.VisualizationDate()
        VLD.GetDate(args.file)
    else:
        print("Select one of parser args")

