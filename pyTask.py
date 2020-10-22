import psutil
import time
import os
import sys
import clint

def list_tasks():
    for proc in psutil.process_iter():
        print (str(proc.pid) +"    "+  str(proc.name()))

def end_task():
    pid = input("input a pid task \n") 
    os.system("taskkill /PID "+(str(pid)))
    print ("process terminated")

def main_process():
    print ("pyTask started")
    while True:
        print (" select 1 to show process")
        print (" select 2 to terminate a process")
        choice = int(input("\n"))
        if choice == 1 :
            list_tasks()
        elif choice == 2:
            end_task()
        else:
            pass
    
main_process()
