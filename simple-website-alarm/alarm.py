import time
import webbrowser

setAlarm = raw_input("Set Website alarm as H:M:S ")
url = raw_input("Website URL please ")
actualTime = time.strftime("%I:%M:%S")

while(actualTime != setAlarm):
    print("Time is : "+actualTime)
    actualTime = time.strftime("%I:%M:%S")
    time.sleep(1)

if(actualTime == setAlarm):
    print("Webpage should be seen...")
    webbrowser.open(url)