import time
import argparse
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--run', type=int,default=1)
args = parser.parse_args()
                         
# 定义一个作业类
class Job:
    def __init__(self, name, time):
        self.name = name    
        self.time = time       

# 定义一个 SJF 调度函数
class SJF:
def sjf(self，job_list):
        print("Initial number of pros is {}".format(len(job_list)))
        StartTime=time.time()
        CompletionTime = 0
        WaitingTime = 0

         # 按照作业执行时间从小到大排序
        time=CompletionTime -StartTime
         job_list.sort(key=lambda x: x.time)

    # 依次执行作业
    for job in job_list:
        print("Job {} is running for {} seconds.".format(job.name, job.time))

number = int(input("请输入创建作业的个数："))
job_list = []
for i in range(0, number):
job_list.append(Job(str(input("请输入作业{}的名称：".format(i+1))), int(input("请输入作业{}运行的时间：".format(i+1)))))

# 执行 SJF 调度算法
sjf(job_list)