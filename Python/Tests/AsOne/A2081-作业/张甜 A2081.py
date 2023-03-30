class Job:
    def __init__(self, name, time):
        self.name = name
        self.time = time
class SJF:
    def __init__(self,job_list):
        self.job_list = job_list
        job_list.sort(key=lambda x: x.time)
        for job in job_list:
            print("Job {} is running for {} seconds.".format(job.name, job.time))
number = int(input("请输入创建作业的个数："))
job_list = []
for i in range(0, number):
    job_list.append(Job(str(input("请输入作业{}的名称：".format(i+1))), int(input("请输入作业{}运行的时间：".format(i+1)))))

SJF(job_list)
