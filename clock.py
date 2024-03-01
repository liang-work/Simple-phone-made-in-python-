import os
import time
os.system("clear")
while True:
    print("0 exit")
    print("1 look at now time")
    print("2 set alarm clock(not available)")
    pe_in = input ()
    if pe_in == '0':
        os.system("clear")
        os.system("python phone.py")
        exit()
    if pe_in == '1':
        os.system("python now_time.py")
        exit()