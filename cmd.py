import os
import time
print ("welcome!")
setting_1 = {
    'set_word':'new',
    'set_password':'abc123',
    'new_su_time':'0'
    }
while True:
    pe_in = input("/>")
    if pe_in =='back':
        os.system("python phone.py")
        os.system("clear")
        exit()
    elif pe_in =='exit' or pe_in =='logout':
        print("Invalid instruction(please input 'back')")
    elif pe_in == 'sudo':
        pe_in = input("do you use the 'sudo'? [y/n] ")
        if pe_in == 'y':
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
        elif pe_in == 'n':
            os.system('clear')
    elif pe_in == 'by':
        print ("by: liang_work/github.com")
    else:
        os.system(pe_in)