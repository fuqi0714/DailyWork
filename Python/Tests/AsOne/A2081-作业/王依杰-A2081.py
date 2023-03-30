
class Job:
    def __init__(self, name, time):
        self.name = name
        self.time = time

class SJF:
    def SJF_test1(self,job_list):
       
        job_list.sort(key=lambda x: x.time)
       
        for job in job_list:
            print("Job {} is running for {} seconds.".format(job.name, job.time))
    def SJF_test2(self,job_list):
        number = int(input("作业个数："))
        for i in range(0, number):
            job_list.append(Job(str(input("作业{}名称：".format(i + 1))),
                                int(input("作业{}运行时长：".format(i + 1)))))
        job_list.sort(key=lambda x: x.time)
        for job in job_list:
            print("Job {} is running for {} seconds.".format(job.name, job.time))


if __name__ == '__main__':
    S = SJF()

    job_list = []
 

    while 1:
        number = int(input("请输入创建进程的方案（共两种） 0键退出"))
        if number==1:
            job1 = Job("A", 3)
            job2 = Job("B", 1)
            job3 = Job("C", 2)
            job_list = [job1, job2, job3]
            S.SJF_test1(job_list)
        elif number==2:
            print("只要进程不销毁就一直在")
            S.SJF_test2(job_list)
        elif number==0:
            print("退出")
            break
        else:
            print("输入错误")


