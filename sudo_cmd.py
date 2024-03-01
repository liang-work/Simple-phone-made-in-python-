import os
import time
def root_cmd():
    print ("welcome!")
    while True:
        time.sleep(0.5)
        su_in = input("root$1000> ")
        if su_in == 'exit' or su_in == 'logout':
            exit()
        elif su_in == 'by':
            print ("by: liang_work/github.com")
        else:
            os.system(su_in)
root_cmd()