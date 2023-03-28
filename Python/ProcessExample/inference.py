import subprocess,os,argparse,signal
import time
from multiprocessing import Process

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--cmds', type=str, default='C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe')
parser.add_argument('--pid_kill', type=str,default='')
args = parser.parse_args()


def task():
    task=subprocess.Popen(args.cmds,shell=True)
    print(task.pid)
    time.sleep(3)
    #end = ("taskkill  /F /IM msedge.exe")
    #os.system(end)
    '''
    
    #os.popen('taskkill.exe /F /pid {pid}'.format(pid=str(task.pid)))
    #os.popen('taskkill.exe /pid:'+str(task.pid))
    if args.pid_kill!="":
        subprocess.Popen("taskkill /F /T /PID " + str(task.pid), shell=True)
    '''
    subprocess.Popen("taskkill /F /T /PID " + str(task.pid), shell=True)

task()