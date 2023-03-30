# 定义一个作业类
class Job:
    def __init__(self, name, time):
        self.name = name
        self.time = time


# 定义一个 SJF 调度函数
class SJF:
    
    def SJF_test(self,job_list):
        number = int(input("请输入作业的个数："))
        for i in range(0, number):
            # 创建多个作业实例,并添加到列表中
            job_list.append(Job(str(input("请输入作业{}的名称：".format(i + 1))),
                                int(input("请输入作业{}运行的时间：".format(i + 1)))))
        job_list.sort(key=lambda x: x.time)
        # 依次执行作业
        for job in job_list:
            print("Job {} is running for {} seconds.".format(job.name, job.time))


if __name__ == '__main__':
    S = SJF()

    job_list = []
    # 创建三个作业实例

   
    S.SJF_test(job_list)

