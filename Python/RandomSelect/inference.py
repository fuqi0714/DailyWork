import argparse
import pandas as pd
import random,os

# 方法文档https://blog.csdn.net/houyanhua1/article/details/87809185
# 进度条文档https://blog.csdn.net/weixin_46089319/article/details/107406269
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--file', type=str,required=True)
args = parser.parse_args()


class RandomID:
    RandomList = []
    
    def GetItemFromCSV(self):
        testDict = {'ID': '', 'Name': '','Times': ''}
        table = pd.read_csv(args.file, names=["ID", "Name", "Sex", "Times"])
        # for 0 in
        df = pd.DataFrame(table)
        self.ShowResult(df, testDict)
        
        # print(df[2:3][["ID","Name"]])
    def ShowResult(self,pandas_table,testDict):
        print()
        n = self.RandomNum(len(pandas_table))
        testDict['ID'] = pandas_table[n:n + 1][["ID"]].to_string(index=False, header=0)
        testDict['Name'] = pandas_table[n:n + 1][["Name"]].to_string(index=False, header=0)
        times=pandas_table[n:n + 1][["Times"]]+1
        testDict['Times'] =times.to_string(index=False, header=0)
        print(testDict)
        self.WriteBack(n,pandas_table,times)

    def WriteBack(self,number,pandas_table,times):
        pandas_table.loc[number,'Times']=times.to_string(index=False, header=0)
        
        pandas_table.to_csv(args.file,header=None,index=None)
        file=os.path.split(args.file)[1]
        pandas_table.to_csv('src/'+file,header=None,index=None)
        print("Write back over and update")
        '''
        mix path
        if os.path.exists(file_path):
            pandas_table.to_csv(args.file,header=None,index=None)
            #print(os.path.join(file_path,args.file))
            
        '''
    def RelativePathUpdate(self,pandas_table):
        pandas_table.to_csv(args.file,header=None,index=None)
    def RandomNum(self, x):
        n = random.randint(0, x - 1)
        return n

    def GenerateDictObj(self):
        temptDict = {'': ''}
        return temptDict


if __name__ == '__main__':
    RID = RandomID()
    RID.GetItemFromCSV()
