import os
ca_lan = 'English'
with open('cal_val.txt','r') as f:
    ca_lan = f.read()
os.system("clear")
while True:
    pe_in = ''
    if ca_lan == 'English':
        print("-1 exit")
        print("0 setting and about")
        print("1 + ")
        print("2 - ")
        print("3 × ")
        print("4 ÷ ")
        print("5 ^2 ")
        pe_in = input()
        if pe_in == '-1':
            pe_in = ''
            print("back…")
            os.system("python phone.py")
            exit()
        if pe_in == '0':
            pe_in = ''
            os.system("clear")
            print("1 language")
            print("2 about")
            pe_in = input()
            if pe_in == "1":
                pe_in = ''
                print("1 Chinese")
                print("2 English")
                print("now you use language is English")
                pe_in = input()
                if pe_in =='1':
                    pe_in = ''
                    ca_lan = 'Chinese'
                    with open('cal_val.txt','w') as f1:
                        f1.write(ca_lan)
                    print('ok, you need reload the app')
                    time.sleep(3)
                    os.system("clear")
                elif pe_in =='2':
                    pe_in = ''
                    print('now you use language is English')
            if pe_in == "2":
                pe_in = ''
                print("calculator app")
                print("made in python")
                print("by liang_work github.com")
                print("V1.0")
        if (pe_in=='1'):#加
            a = int(input("number 1  "))
            b = int(input("number 2  "))
            c=a+b
            print ("output number" + str(c))
        if (pe_in=='2'):#减
            a = int(input("number 1  "))
            b = int(input("number 2  "))
            c=a-b
            print ("output number" + str(c))
        if (pe_in=='3'):#乘
            a = int(input("number 1  "))
            b = int(input("number 2  "))
            c=a*b
            print ("output number" + str(c))
        if (pe_in=='4'):#除
            a = int(input("number 1  "))
            b = int(input("number 2  "))
            c=a/b
            print ("output number" + str(c))
        
        if (pe_in=='5'):#^2
            a = int(input("number  "))
            c=a*a
            print ("output number" +str(c))
    elif ca_lan =='Chinese':
        print("-1 退出")
        print("0 设置/关于")
        print("1 + ")
        print("2 - ")
        print("3 × ")
        print("4 ÷ ")
        print("5 ^2 ")
        pe_in = input()
        if pe_in == '-1':
            print("返回中…")
            os.system("python phone.py")
            exit()
        if pe_in == '0':
            os.system("clear")
            print("1 语言")
            print("2 关于")
            pe_in = input()
            if pe_in == "1":
                pe_in = ''
                print("1 中文")
                print("2 英文")
                print("现在你是用的是中文")
                pe_in = input()
                if pe_in =='2':
                    pe_in = ''
                    ca_lan = 'English'
                    with open('cal_val.txt','w') as f1:
                        f1.write(ca_lan)
                    print('好了，现在你需要重启应用')
                    time.sleep(3)
                    os.system("clear")
                elif pe_in =='1':
                    pe_in = ''
                    print('现在你是用的是中文')
            if pe_in == "2":
                pe_in = ''
                print("计算器app")
                print("使用python制作")
                print("由 liang_work 在github.com发布")
                print("版本1.0")
        if (pe_in=='1'):#加
            a = int(input("数字 1  "))
            b = int(input("数字 2  "))
            c=a+b
            print ("输出数字" + str(c))
        if (pe_in=='2'):#减
            a = int(input("数字 1  "))
            b = int(input("数字 2  "))
            c=a-b
            print ("输出数字" + str(c))
        if (pe_in=='3'):#乘
            a = int(input("数字 1  "))
            b = int(input("数字 2  "))
            c=a*b
            print ("输出数字" + str(c))
        if (pe_in=='4'):#除
            a = int(input("数字 1  "))
            b = int(input("数字 2  "))
            c=a/b
            print ("输出数字" + str(c))
        
        if (pe_in=='5'):#^2
            a = int(input("数字  "))
            c=a*a
            print ("输出数字" +str(c))