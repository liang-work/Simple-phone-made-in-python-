from datetime import datetime
import os
a=0
while a == 0:

    now = datetime.now()

    current_hour = now.strftime("%I")

    current_minute = now.strftime("%M")

    current_seconds = now.strftime("%S")

    current_period = now.strftime("%P")
    
    print(str(current_hour),':',str(current_minute),':',str(current_seconds),':',str(current_period))
    
    tc = input('1 exit ; other is continue')
    
    if tc =='1':
        
        a = 1
        
        os.system('python clock.py')
        
        exit()