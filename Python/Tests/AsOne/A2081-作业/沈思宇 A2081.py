# 定义一个作业类
class Job:

    def __init__(self, name, time):
        self.name = name
        self.time = time

# 定义一个调度方法类
class SJF:

    def __init__(self,job_list):
        self.job_list = job_list
        # 按照作业执行时间从小到大排序
        job_list.sort(key=lambda x: x.time)
        # 依次执行作业
        for job in job_list:
            print("Job {} is running for {} seconds.".format(job.name, job.time))

number = int(input("请输入创建作业的个数："))
job_list = []
for i in range(0, number):
    # 创建多个作业实例,并添加到列表中
    job_list.append(Job(str(input("请输入作业{}的名称：".format(i+1))), int(input("请输入作业{}运行的时间：".format(i+1)))))

# 执行 SJF 调度算法
SJF(job_list)
