import time
for i in range(10,0,-1):
    print(f"\r倒计时{i}秒",end='')
    time.sleep(1)
print('end')