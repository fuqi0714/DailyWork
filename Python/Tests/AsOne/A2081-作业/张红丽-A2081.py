class Process:
    def __init__(self, name, time):
        self.name = name
        self.time = time

def sjf(processes):
    processes.sort(key=lambda x: x.time) # 按照时间升序排序

    current_time = 0
    total_time = 0

    for process in processes:
        current_time += process.time
        total_time += current_time

    return total_time / len(processes)

if __name__ == '__main__':
    n = int(input("请输入进程数量："))
    processes = []
    for i in range(n):
        name = input("请输入进程名：")
        time = int(input("请输入进程运行时间："))
        processes.append(Process(name, time))
    avg_time = sjf(processes)
    print("平均等待时间为：", avg_time)