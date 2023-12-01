import argparse,random
import pandas as pd
import numpy as np

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--file', type=str, default='src/list.csv')
parser.add_argument('--average', type=int,required=True)
parser.add_argument('--times', type=int,required=True)
parser.add_argument('--min', type=int,required=True)
parser.add_argument('--max', type=int,required=True)
parser.add_argument('--out', type=str, default='src/score.csv')
args = parser.parse_args()
'''
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

#GetFromCSV()

'''
class ArithmeticProgression:
    numList=[]
    def test(self):
        print("f")

    def GenerationList(self,average,times,min,max):
        total=average*times
        print("数列和为：")
        print(total)
        num=times-1
        d=(2*total/times-2*min)/(num)
        print("方差为：")
        print(d)
        #
        self.GenerationValueList(min, d, times)

        for i in self.numList:
            print(i)
            print("")
        print("均值为：")
        print(np.mean(self.numList))

    def GenerationValueList(self,first_value,d,next_index):

        if next_index>0:
            next_value = first_value + d*(args.times-next_index)
            self.numList.append(next_value)
            print("")
            self.GenerationValueList(first_value,d,next_index-1)

        else:
            return



if __name__=='__main__':
    print("run")
    AP=ArithmeticProgression()
    AP.GenerationList(args.average,args.times,args.min,args.max)
