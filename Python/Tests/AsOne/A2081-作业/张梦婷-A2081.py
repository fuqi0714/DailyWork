# 定义一个作业类
class Job:
    def __init__(self, name, time):
        self.name = name
        self.time = time


# 定义一个 SJF 调度函数
class SJF:
    def SJF_test1(self,job_list):
        # 按照作业执行时间从小到大排序
        job_list.sort(key=lambda x: x.time)
        # 依次执行作业
        for job in job_list:
            print("Job {} is running for {} seconds.".format(job.name, job.time))
    def SJF_test2(self,job_list):
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

    while 1:
        number = int(input("请输入创建进程的方案："))
        if number==1:
            job1 = Job("A", 3)
            job2 = Job("B", 1)
            job3 = Job("C", 2)
            job_list = [job1, job2, job3]
            S.SJF_test1(job_list)
        elif number==2:
            print("只要进程不销毁就一直在")
            S.SJF_test2(job_list)
        elif number==9:
            print("退出测试！")
            break
        else:
            print("输入有误")


