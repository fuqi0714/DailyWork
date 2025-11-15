import argparse
import os
import random
import time as t

from icecream import ic
from datetime import datetime

import module.GetItemFromCSV as GIFC
import module.VisualizationModule as VLM
import pandas as pd


parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--file', type=str, required=True)
parser.add_argument('--target_path', type=str,default="")
parser.add_argument('--nums', type=int, default=3)
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
    def time_format(self):
        date_detail="{}".format(datetime.now())
        return f'{date_detail}|>'

    def Recursion(self,nums):
        self.ShowResult()
        if nums==1:
            ic()
            return
        else:
            ic()
            next=nums - 1
            self.Recursion(next)


    def ShowResult(self):
        ic("Starting RandomSelect")
        testDict = {'ID': '', 'Name': '', 'Times': '', 'PreviousDate': ''}
        pandas_table = GIFC.GetItemFromCSV(args.file)
        ic("Converting CSV file complete")
        n = self.RandomNum(len(pandas_table))

        testDict['ID'] = pandas_table[n:n + 1][["ID"]].to_string(index=False, header=0)
        testDict['Name'] = pandas_table[n:n + 1][["Name"]].to_string(index=False, header=0)
        times = pandas_table[n:n + 1][["Times"]] + 1
        testDict['Times'] = times.to_string(index=False, header=0)

        testDict['PreviousDate'] = pandas_table[n:n + 1][["PreviousDate"]].to_string(index=False, header=0)
        ic("Generating Detail of Result")
        currentDate=self.GetCurrentDate()
        ic(testDict)
        self.WriteBack(n, pandas_table, times,currentDate)

    def WriteDetails(self, id, currentDate, score):
        '''
        根据传来的id值，先判断是否存在以这个学号id命名的csv文件，如果存在则直接打开向里面更新一条时间属性值。
        如果不存在则先创建python语言自带的pandas表格数据类型（包含两列信息，点名时间和得分），然后将该类型结构的数据通过to_csv方法直接写入成以该学号id为名称的csv文件，
        然后打开文件追加更新的时间属性值
        '''
        ic("Writing Details")
        # if os.path.exists(id):
        #     file = open(os.path.join(id,".csv"),'a')
        #     file.write(currentDate,score)
        #     file.write('\n')
        #     file.close()
        # else:
        if os.path.exists(id):
            filename = id + '.csv'
            with open(os.path.join(id, filename), 'a', encoding='utf-8-sig') as filename:

                filename.write(f"{currentDate},{score}\n")
                '''
                new_record = pd.DataFrame({
                    '点名时间': [currentDate],
                    '得分': [score]
                })
                '''

            return
        else:
            os.makedirs(id)
            file = pd.DataFrame(columns=['点名时间', '得分'])
            filename = id + '.csv'
            with open(os.path.join(id, filename), 'a', encoding='utf-8-sig') as filename:

                filename.write(f"{currentDate},{score}\n")
            '''    new_record = pd.DataFrame({
                    '点名时间': [currentDate],
                    '得分': [score]
                })
            new_record.to_csv(os.path.join(id, filename), mode='a', header=False, index=False, encoding='utf-8-sig')'''
            # file.to_csv(id, index=False, encoding='utf-8-sig')
            return

    def WriteBack(self, number, pandas_table, times,currentDate):
        ic("Starting Rewrite")
        pandas_table.loc[number, 'Times'] = times.to_string(index=False, header=0)
        pandas_table.loc[number, 'PreviousDate'] = currentDate
        pandas_table.to_csv(args.file, header=None, index=None)
        file = os.path.split(args.file)[1]
        if len(args.target_path) != 0:
            ic("file+ ============" + file)
            front_path = os.path.join(os.getcwd(), 'src' + os.path.sep)
            ic("front_path+ ============" + front_path)
            dis_path = os.path.join(front_path, file)
            ic("dis_path+ ============" + dis_path)
            ic("change path")
            # args.target_path="E:\WeeklyLesson\week004\Pros\Myproject\Assets\OutsideExe\target"
            dis_path = os.path.join(args.target_path, file)
            ic("change path over")
        pandas_table.to_csv('src/' + file, header=None, index=None)
        ic("Writing back over and updating")
        '''
        mix path
        if os.path.exists(file_path):
            pandas_table.to_csv(args.file,header=None,index=None)
            #ic(os.path.join(file_path,args.file))
            
        '''

    def RelativePathUpdate(self, pandas_table):
        pandas_table.to_csv(args.file, header=None, index=None)

    def GetCurrentDate(self):
        time=t.strftime("%Y-%m-%d %H:%M:%S", t.localtime())
        return time

    def RandomNum(self, x):
        time = int(t.strftime("%S", t.localtime()))+ random.randint(0, x+1)
        if time < x:
            return time
        else:
            total_num = 7 * x
            n = random.randint(0, total_num - 1)
            result = n % x
            return result

    def GenerateDictObj(self):
        temptDict = {'': ''}
        return temptDict


if __name__ == '__main__':
    if args.RandomSelect:
        ic(" RandomSelect Becall")
        RID = RandomID()
        RID.Recursion(args.nums)
    elif args.Visualization:
        ic(" Visualization Becall")
        VLD=VLM.VisualizationDate()
        VLD.GetDate(args.file)
    else:
        ic("Select one of parser args")

