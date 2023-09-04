import random
import datetime
import time as t
'''
https://juejin.cn/post/7002158716267003941
def RandomList( pandas_table):
    RandomListValue = []
    for i in range(5):
        n = RandomNum(pandas_table)
        print(n)
        for j in RandomListValue:
            if j != n:
                RandomListValue.append(n)
            else:
                return

    return RandomListValue

def RandomNum(x):
    n = random.randint(0, x - 1)
    return n

print(RandomList(60))

'''

def RateList():
    print("fs")

def RandomNum( x):
    time = int(t.strftime("%S", t.localtime()))
    oneof = random.randint(0,  2)
    if time<x:
        return time
    else:
        total_num = 7 * x
        n = random.randint(0, total_num - 1)
        print(n)
        result = n % x
        return result



def GetCurrentDate():
    #time=int(t.strftime("%MS", t.localtime()))
    time=datetime.datetime.now()
    print(time)
    print(time.millisecond)
    return time

#print(type(GetCurrentDate()))
for i in range(200):
    GetCurrentDate()
    t.sleep(0.121)
    #print(RandomNum(43))    print("--------------------------------")