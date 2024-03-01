import os
import pickle
import time
app_name = {
    "1":"minecraft.py"
}
lj_list = {
    "minecraft.py":"/storage/emulated/0/xmx/app"
}
app_list = []
with open ('app_list.pkl','rb') as f:
    app_name = pickle.load(f)
with open ('wjlj.pkl', 'rb') as f:
    lj_list = pickle.load(f)
app_list = app_name.keys()
os.system("clear")
print("Please enter the complete file name.")
print(app_name)
pe_in = str(input())
if pe_in in app_list:
    print("Do you really want to clear this app? [y/n]")
    pe_in_1 = input()
    if pe_in_1 == 'y':
        print("Is this the app you need to clear? [y/n]")
        time.sleep(0.5)
        pe_in_1 = input()
        if pe_in_1 == 'y':
            app_del = app_name[pe_in]
            app_name.pop(pe_in)
            lj_list.pop(app_del)
            print("ok")
            print(app_name)
            print(lj_list)
            with open ('wjlj.pkl','wb') as f:
                pickle.dump(lj_list,f)
                f.close()
            with open ('app_list.pkl','wb') as f1:
                pickle.dump(app_name,f1)
                f1.close()
            os.system('python phone.py')