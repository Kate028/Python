# Importing libraries

import datetime

alarmHour = int(input("What hour do you wanna wake up?"))
alarmMinute = int(input("What minute do you wanna wake up?"))

amPm= str(input("am or pm"))

if(amPm == "pm"):
    alarmHour = alarmHour + 12

while(1 == 1):
    if(alarmHour == datetime.datetime.now().hour and 
    alarmMinute == datetime.datetime.now().minute):
     print("Wake Up")
     break   

print('exited')