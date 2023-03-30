# 定义一个进程类
class Process:

    def __init__(self, name, time):
        self.name = name
        self.time = time

# 定义一个调度方法类
class SJF:

    def __init__(self, process_list):
        self.process_list = process_list
        process_list.sort(key=lambda x: x.time)
        for process in process_list:
            print("process {} is running for {} seconds.".format(process.name, process.time))

number  = int(input("请输入创建进程的个数："))
process_list = []
for i in range(0, number):
    process_list.append(Process(str(input("请输入进程{}的名称：".format(i+1))), int(input("请输入进程{}运行的时间：".format(i+1)))))

# 执行 SJF 调度算法
SJF(process_list)