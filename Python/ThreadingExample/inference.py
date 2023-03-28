import argparse
import time

import pandas as pd
import random, os, threading

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--file1', type=str, default='src/2161MaleList.csv')
parser.add_argument('--file2', type=str, default='src/2161FemaleList.csv')
args = parser.parse_args()


class ThreadingExample(threading.Thread):
    InstantiateTime = time.time()
    print('InstantiateTime:' + str(InstantiateTime))

    def GetItemFromMaleCSV(self):
        print('t1:Get male item awake time:' + str(time.time()) + '\n')
        testDict = {'ID': '', 'Name': '', 'Sex': '', 'Times': ''}
        table = pd.read_csv(args.file1, names=["ID", "Name", "Sex", "Times"])

        df = pd.DataFrame(table)
        print('t1:Get male item end time:' + str(time.time()) + '\n')
        t1_2 = threading.Thread(target=ThreadingExample().ShowMaleResult, args=(df, testDict))
        t1_2.start()

    def GetItemFromFemaleCSV(self):
        print('t2:Get female item awake time:' + str(time.time()) + '\n')
        testDict = {'ID': '', 'Name': '', 'Sex': '', 'Times': ''}
        table = pd.read_csv(args.file2, names=["ID", "Name", "Sex", "Times"])

        df = pd.DataFrame(table)
        print('t2:Get female item End time:' + str(time.time()) + '\n')
        t2_2 = threading.Thread(target=ThreadingExample().ShowFemaleResult, args=(df, testDict))
        t2_2.start()

    def ShowMaleResult(self, pandas_table, testDict):
        StartTIme=time.time()
        DelayTime=0.0
        print('t1_2:Show male item awake time:' + str(StartTIme) + '\n')
        for n in range(len(pandas_table)):
            DelayTime += 0.1
            print(self.GenerateValue(n, pandas_table, testDict))

        print('t1_2: Cost time '+str(time.time()-StartTIme)+' DelayTime is '+str(DelayTime))
    def ShowFemaleResult(self, pandas_table, testDict):
        StartTIme = time.time()
        DelayTime = 0.0
        print('t2_2:Show female item awake time:' + str(time.time()) + '\n')
        for n in range(len(pandas_table)):
            DelayTime += 0.1
            print(self.GenerateValue(n, pandas_table, testDict))
        print('t2_2: total cost time ' + str(time.time() - StartTIme)+' DelayTime is '+str(DelayTime))
    def GenerateValue(self,n,pandas_table, testDict):
        time.sleep(0.1)
        testDict['ID'] = pandas_table[n:n + 1][["ID"]].to_string(index=False, header=0)
        testDict['Name'] = pandas_table[n:n + 1][["Name"]].to_string(index=False, header=0)
        testDict['Sex'] = pandas_table[n:n + 1][["Sex"]].to_string(index=False, header=0)
        times = pandas_table[n:n + 1][["Times"]] + 1
        testDict['Times'] = times.to_string(index=False, header=0)
        return testDict

if __name__ == '__main__':
    ProcessTime = time.time()
    print('ProcessID:' + str(os.getpid()))
    print('ProcessTime:' + str(ProcessTime) + ', Main thread name :' + threading.current_thread().name)

    TE = ThreadingExample()

    t1 = threading.Thread(target=ThreadingExample().GetItemFromMaleCSV)
    t2 = threading.Thread(target=ThreadingExample().GetItemFromFemaleCSV)

    t1.start()
    t2.start()
