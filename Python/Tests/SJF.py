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
