import os
import time
import pickle
print ("welcome!")
os.system('clear')
wj_lj = os.getcwd()
cd = "cd "
python = "python "
java = "java "
c = "c "
cc = "cc "
c_jj = "c++ "
st_app = ""
st_a_na = ""
setting_1 = {
    'set_word':'new',
    'set_password':'abc123',
    'new_su_time':'0'
    }
app_name = {
    "1":"minecraft.py"
}
lj_list = {
    "minecraft.py":"/storage/emulated/0/xmx/apps/"
}
def p_e():
    while True:
        pe_in = ''
        with open ('app_list.pkl','rb') as f:
            app_name = pickle.load(f)
        with open ('wjlj.pkl', 'rb') as f:
            lj_list = pickle.load(f)
        app_list = []
        print("1 start app")
        print("2 exit")
        pe_in = input()
        if pe_in =='1':
            pe_in = ''
            os.system("clear")
            print("app list")
            print("-1 setting")
            print("-2 cmd")
            print("-3 clock")
            print("-4 photo(not available)")
            print("-5 calculator")
            print("-6 install app")
            print("-7 uninstall app")
            print(f'{app_name}')
            pe_in = str(input())
            app_list = app_name.keys()
            if pe_in =='-1':
                os.system("clear")
                print("function list")
                print("1 about")
                pe_in = str(input())
                if pe_in =='1':
                    print("by:liang_work github.com")
                    time.sleep(0.5)
                    print("V: 0.998(test)")
                    time.sleep(0.5)
                    print("for more information, please refer to txt file")
                    pe_in = ''
            if pe_in =='-2':
                os.system('clear')
                os.system('python cmd.py')
                exit()
            if pe_in =='-3':
                os.system('clear')
                os.system('python clock.py')
                exit()
            if pe_in =='-5':
                os.system('clear')
                os.system('python calculator.py')
                exit()
            if pe_in == '-6':
                print("do you want to install a app? [y/n]")
                pe_in = input()
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
                            os.system("python install_app.py")
                            exit()
                        else:
                            print('Password wrong')
                    else:
                        print('Account wrong')
            if pe_in =='-7':
                print("do you want to uninstall app [y/n] ")
                pe_in = input()
                if pe_in =='y':
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
                            os.system("python uninstall_app.py")
                            exit()
                        else:
                            print('Password wrong')
                    else:
                        print('Account wrong')
            if pe_in in app_list:
                ls = ''
                ls = app_name[pe_in]
                st_app = lj_list[ls]
                os.system(st_app)
                st_a_na = app_name[pe_in]
                if '.py' in st_a_na :
                    st_a_na_1 =python + st_app + st_a_na
                if '.java' in st_a_na :
                    st_a_na_1 =java + st_app + st_a_na
                if '.c' in st_a_na:
                    st_a_na_1 =c + st_app + st_a_na
                if '.cc' in st_a_na_1:
                    st_a_na_1 =cc + st_app + st_a_na
                if '.c++' in st_a_na :
                    st_a_na_1 =c_jj + st_app + st_a_na
                print(st_a_na_1)
                os.system(st_a_na_1)
                exit()
        elif pe_in =='2':
            exit()
p_e()