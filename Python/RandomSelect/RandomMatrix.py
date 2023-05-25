import argparse,random
import pandas as pd
import numpy as np

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--file', type=str, default='src/list.csv')
parser.add_argument('--times', type=int,required=True)
parser.add_argument('--min', type=int,required=True)
parser.add_argument('--max', type=int,required=True)
parser.add_argument('--out', type=str, default='src/score.csv')
args = parser.parse_args()

def GetFromCSV():
    table = pd.read_csv(args.file, names=["ID", "Name", "Sex"])
    df = pd.DataFrame(table)
    Concat(df,MultiRandomScore(len(df),args.times))
    #Concat(df,RandomScore(len(df)))


def RandomScore(length):
    ScoreList=[]
    for i in range (length):
        score = random.randint(args.min, args.max)
        ScoreList.append(score)
    ScoreData=pd.DataFrame(ScoreList,columns=["Score"])
    return ScoreData


def MultiRandomScore(length,cloumn):
    nparray=np.random.default_rng()
    nparrayList=nparray.integers(args.min, args.max,size=(length,cloumn))
    ScoreData = pd.DataFrame(nparrayList.reshape(length,cloumn), columns=GenerateCloumnInof(cloumn))
    return ScoreData


def GenerateCloumnInof(length):
    CloumnInfo=[]
    for i in range(length):
        CloumnInfo.append(str(i))

    return CloumnInfo


def Concat(df,ScoreData):
    result = pd.concat([df, ScoreData], axis=1)
    WriteToCSV(result)

def WriteToCSV(table):
    table.to_csv("{}".format(args.out))

GetFromCSV()