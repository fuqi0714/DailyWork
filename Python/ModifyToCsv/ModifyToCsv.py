# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 10:44:25 2022

@author: admin
读取文件并将前几列原样输出
个人成绩列按照空格进行拆分
拆分后以某种数据格式存入csv文件
附加列名
"""
import os,csv

import pandas as pd


data=[]
def readFromTxt():
    #txt获取文件内容，转化为列表嵌套列表的格式
    with open('jsj.txt','r',encoding='utf-8') as txtfile:
        for line in txtfile:
            #print(line)
            #newline=filter(deletblank, line)
            newline=filter(None,line.rstrip('\n').split(" "))
            data.append(list(newline))


def writeFromTxtToCSV():
    readFromTxt()
    with open('newjsj.csv','a+',encoding='utf-8',newline="") as csvfile:#newline决定写入的新空行
        writer=csv.writer(csvfile)

        for item in data:
            writer.writerow(item)#按照列表内的逗号分隔符依次写入单元格
#writeFromTxtToCSV()

def writeFromPandasToCSV():
    readFromTxt()
    #print(data)   
    df=pd.DataFrame(data,index=range(1,len(data)+1),columns=['姓名','状态','学号','模式','复试口语','复试笔试','复试面试','状态','政治','英语','数学','408','总分'],dtype=str)     
    print(df)
    df.to_csv('newjsj.csv')

writeFromPandasToCSV()   



