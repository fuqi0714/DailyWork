# 定义一个作业类
class Job:
    def __init__(self, name, time):
        self.name = name
        self.time = time

# 定义一个 SJF 调度函数
def sjf(job_list):
    # 按照作业执行时间从小到大排序
    job_list.sort(key=lambda x: x.time)
    # 依次执行作业
    for job in job_list:
        print("Job {} is running for {} seconds.".format(job.name, job.time))






# 创建三个作业实例
job1 = Job("A", 3)
job2 = Job("B", 1)
job3 = Job("C", 2)

# 将作业实例添加到列表中
job_list = [job1, job2, job3]

# 执行 SJF 调度算法
sjf(job_list)
/////////////////////////////////////////////////////////////////////////////////////////////////
import time
import argparse


parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--run', type=int,default=1)
args = parser.parse_args()



class Process:
    def __init__(self, pid, ArrivalTime, BurstTime):
        self.pid = pid
        self.ArrivalTime = ArrivalTime
        self.BurstTime = BurstTime

class FCFS:
    def FCFS_Scheduling(self,processes):
        print("Initial number of pros is {}".format(len(processes)))
        StartTime=time.time()
        CompletionTime = 0
        WaitingTime = 0
    
        for process in processes:
            # 计算每个进程的完成时间和等待时间
            CompletionTime = max(CompletionTime, process.ArrivalTime) + process.BurstTime
            
            WaitingTime += max(0, CompletionTime - process.ArrivalTime - process.BurstTime)
            print("Pid is {}  CompletionTime is {} ,WaitingTime is {}".format(process.pid,CompletionTime,WaitingTime))
            
        AvgWaitingTime = WaitingTime / len(processes)

    
        return AvgWaitingTime

    def InputFromOutside(self,n):
        processes=[]
        for i in range (n):
            print("Processes pid is {}".format(i+1))
            ArrivalTime=int(input("Input ArrivalTime: "))
            BurstTime=int(input("Input BurstTime: "))
            
            p=Process(i+1,ArrivalTime,BurstTime)
            processes.append(p)

        AvgWaitingTime = F.FCFS_Scheduling(processes)
        print("Generate process list over ")


    processes=[]#List for Recursion 

    def InputWithRecursion(self,n,index):
        
        if n==0:
            AvgWaitingTime = F.FCFS_Scheduling(F.processes)
            print("Generate process list over ")
            return
        else:
            index=index
            print("Processes pid is {}".format(index))
            ArrivalTime=int(input("Input ArrivalTime: "))
            BurstTime=int(input("Input BurstTime: "))
            
            p=Process(index,ArrivalTime,BurstTime)
            FCFS.processes.append(p)

            self.InputWithRecursion(n-1,index+1)



       
        



if __name__ == '__main__':

    F=FCFS()

    if args.run==1:
        processes = [
        Process(1, 0, 10),
        Process(2, 6, 20),
        Process(3, 8, 30),
        Process(4, 9, 5),
        Process(5, 15, 15),
        ]
        AvgWaitingTime = F.FCFS_Scheduling(processes)
        print("AvgWaitingTime is {}".format(AvgWaitingTime) )

    elif args.run==2:
        ProNum=input("Input Process num : ")
        F.InputFormOutside(int(ProNum))

    else:
        ProNum=input("Input Process num : ")
        F.InputWithRecursion(int(ProNum),1)

///////////////////////////////////////////////////////////////////
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--times', type=str,required=True)
args = parser.parse_args()

'''
递归算法(英语: recursion algorithm)在计算机科学中是指一种通过重复将问题分解为同类的子问题而解决问题的方法。
递归式方法可以被用于解决很多的计算机科学问题，因此它是计算机科学中十分重要的一个概念。绝大多数编程语言支持函数的
自调用，在这些语言中函数可以通过调用自身来进行递归。计算理论可以证明递归的作用可以完全取代循环,因此在很多函数编
程语言中习惯用递归来实现循环
'''
class Recursion:
    def RecursionFun(self, times):
        value = times
        if times < 2:
            return value
        else:
            value = value * self.RecursionFun(times - 1)

            return value


if __name__ == '__main__':
    R = Recursion()
    print(R.RecursionFun(args.times))