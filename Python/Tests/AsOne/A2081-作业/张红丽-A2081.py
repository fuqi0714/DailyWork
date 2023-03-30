class Process:
    def __init__(self, name, time):
        self.name = name
        self.time = time

def sjf(processes):
    processes.sort(key=lambda x: x.time) # ����ʱ����������

    current_time = 0
    total_time = 0

    for process in processes:
        current_time += process.time
        total_time += current_time

    return total_time / len(processes)

if __name__ == '__main__':
    n = int(input("���������������"))
    processes = []
    for i in range(n):
        name = input("�������������")
        time = int(input("�������������ʱ�䣺"))
        processes.append(Process(name, time))
    avg_time = sjf(processes)
    print("ƽ���ȴ�ʱ��Ϊ��", avg_time)