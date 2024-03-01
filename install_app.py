import os
import pickle
app_name = {
    "1":"minecraft.py"
}
lj_list = {
    "minecraft.py":"/storage/emulated/0/xmx/app"
}
with open ('app_list.pkl','rb') as f:
    app_name = pickle.load(f)
with open ('wjlj.pkl', 'rb') as f:
    lj_list = pickle.load(f)
os.system("clear")
print(app_name)
print(lj_list)
print ("Kind reminder: Currently, only. java. c. cc. c++. py and other files can be added")
print("now,please input install app'name such as 'xxx.py'")
pe_in = input()
ap = lj_list.keys()
if pe_in not in ap:
    print("ok, now please input the file full path such as '/storage/emulated/0/xmx/'")
    print("Caution: Do not include file names")
    pe_in_2 = input()
    ap_1 = lj_list.values()
    ap_2 = app_name.keys()
    print("installing app…")
    lj_list[pe_in] = pe_in_2
    for i in range(1,100):
        i_1 = str(i)
        if i_1 not in ap_2:
            app_name[str(i)] = pe_in
            print(app_name)
            print(lj_list)
            with open ('wjlj.pkl','wb') as f:
                pickle.dump(lj_list,f)
                f.close()
            with open ('app_list.pkl','wb') as f1:
                pickle.dump(app_name,f1)
                f1.close()
            os.system('python phone.py')
            break
            exit()
        print("Warning! More than 100 apps added! There are no assignable keys")
else:
    print("This app has already been added")