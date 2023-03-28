from inference import RandomID as RID
import argparse,random
import pandas as pd

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--file', type=str, default='src/42list.csv')
parser.add_argument('--out', type=str, default='src/score.csv')
args = parser.parse_args()

def GetFromCSV():
    table = pd.read_csv(args.file, names=["ID", "Name", "Sex"])
    df = pd.DataFrame(table)
    print(len(df))
    Concat(df,RandomScore(len(df)))

def RandomScore(length):
    ScoreList=[]
    for i in range (length):
        score = random.randint(40, 70)
        ScoreList.append(score)
    ScoreData=pd.DataFrame(ScoreList,columns=["Score"])
    return ScoreData

def Concat(df,ScoreData):
    result = pd.concat([df, ScoreData], axis=1)
    WriteToCSV(result)

def WriteToCSV(table):
    table.to_csv("{}".format(args.out))

GetFromCSV()