import time
import webbrowser
Alarm = input("Set the website alarm as H:M:S: ")
url = input("Enter the website you want to open: ")
Actual_Time = time.strftime("%I:%M:%S")
while Actual_Time != Alarm:
    print ("The time is " + Actual_Time)
    Actual_Time = time.strftime("%I:%M:%S")
    time.sleep(1)

if Actual_Time == Alarm:
        print ("You should see your webpage now :-)")
        webbrowser.open(url)
        