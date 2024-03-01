## made in python 3.11
import time
import random
import os
setting_1 = {
    'set_word':'new',
    'set_password':'abc123',
    'new_su_time':'0'
    }
word = ["a"]
password = {"a":"123456"}
while True:
    hd = input("Have you got a account? [y/n]")
    if hd == 'y':
        print ('ok,now loading…')
        sj = random.randint(0,4)
        time.sleep(sj)
        playerword = input("please input account  ")
        time.sleep(1)
        playerpassword = input("please input password  ")
        if playerword in word:
            pppass = ''.join(password[playerword])
            if pppass in playerpassword:
                os.system('clear')
                print('hello')
                for i in range(0,101,1):
                    print(f"\rload…{i}%",end='')
                    sj = random.uniform(0.1,0.75)
                    time.sleep(sj)
                os.system("python phone.py")
                exit()
            else:
                print('Password wrong')
        else:
            print('Account wrong')
    elif hd =='n':
        print ("ok,now we going to make a new account")
        print ("so, we need load…")
        sj =random.randint(0,4)
        time.sleep(sj)
        new_word = input("please input new account  ")
        time.sleep(0.5)
        new_password = input("please input new account's password  ")
        if new_word in word:
            print ("sorry, you do not apply this account, because it used")
        else:
            word.append(new_word)
            password[new_word] = new_password
            print ("ok, now we back…")
            for i in range (10,0,-1):
                print(i)
                time.sleep(1)
            os.system("clear")
    elif hd =='setting':
        set_hd =input ("do you inside setting?[y/n]")
        if set_hd =='y':
            print ("loading…")
            time.sleep(1)
            print("1 exit")
            print("2 use 'sudo'")
            print("3 more")
            set_hd = input()
            if set_hd == '1':
                exit()
            elif set_hd == '2':
                jc_user = setting_1['new_su_time']
                if jc_user =='0':
                    s_w = input("please input the user's name ")
                    time.sleep(1)
                    s_p = input('please input password ')
                    zq_w = setting_1 ['set_word']
                    zq_p = setting_1 ['set_password']
                    if s_w in zq_w:
                        if s_p in zq_p:
                            print("ok!")
                            time.sleep(2)
                            setting_1['new_su_time'] = '1'
                            os.system("clear")
                            os.system("python sudo_cmd.py")
                        else:
                            print('Password wrong')
                    else:
                        print('Account wrong')
                elif jc_user =='1':
                    os.system("clear")
                    os.system("python sudo_cmd.py")
        if set_hd == 'n':
            print('back')
    else:
        print('warning!you enter have got a error!')
        time.sleep(0.5)
        print('now,exiting…')
        exit()