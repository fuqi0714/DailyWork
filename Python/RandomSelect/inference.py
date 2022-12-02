import argparse
import pandas as pd
import random


parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--file', type=str, default='src/41list.csv')
args = parser.parse_args()


class RandomID:
    RandomList = []

    def GetItemFromCSV(self):
        testDict = {'ID': '', 'Name': ''}
        table = pd.read_csv(args.file, names=["ID", "Name", "Sex"])
        # for 0 in
        df = pd.DataFrame(table)

        print()
        n = self.RandomNum(len(df))
        testDict['ID'] = df[n:n + 1][["ID"]].to_string(index=False, header=0)
        testDict['Name'] = df[n:n + 1][["Name"]].to_string(index=False, header=0)
        print(testDict)

    def RandomNum(self, x):
        n = random.randint(0, x - 1)
        return n



if __name__ == '__main__':
    RID = RandomID()
    RID.GetItemFromCSV()
