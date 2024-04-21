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
        CompletionTime = 0
        WaitingTime = 0
        CyclingTime=0

        for process in processes:
            # 计算每个进程的完成时间和周转时间
            CompletionTime = max(CompletionTime, process.ArrivalTime) + process.BurstTime
            CyclingTime=CompletionTime- process.ArrivalTime
            # WaitingTime += max(0, CompletionTime - process.ArrivalTime - process.BurstTime)
            print("Pid is {}  CompletionTime is {} ,CyclingTime is {}".format(process.pid,CompletionTime,CyclingTime))
            
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

        F.FCFS_Scheduling(processes)
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
        F.InputFromOutside(int(ProNum))

    else:
        ProNum=input("Input Process num : ")
        F.InputWithRecursion(int(ProNum),1)