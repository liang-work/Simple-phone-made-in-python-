import pickle
import random
import os
import time
air = {}
print("warning!Do you clear your disk?[y/n]")
a = input()
if a =="y":
    print("Please confirm for the last time!Do you clear your disk?[y/n]")
    a = input()
    if a =="y":
        print("please input you need clear disk'name")
        cp = input("file name ")
        lj = input("Please enter the complete absolute path of the file")
        print("now,we will clear your disk…")
        os.system(f'cd {lj}')
        for i in range(0,101,1):
            print(f"\r{i}%",end='')
            sj = random.uniform(0.1,0.75)
            time.sleep(sj)
        with open(cp + '.pkl', 'wb') as f:
            pickle.dump(air, f)
        time.sleep(1)
        print("ok! now your disk is air.")
        exit()