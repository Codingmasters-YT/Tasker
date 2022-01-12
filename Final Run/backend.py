import json
import webbrowser
from datetime import datetime
import schedule
import time




global tasklist
tasklist = []


def add_task(name, task, time1):  
  
  
 y = {
    "name": name,
    "task": task,
    "time": time1
  }
 tasklist.append(y)
    
    
    
    
def main():
  while True:
    for i in tasklist:
      time1=i['time']
      time2=time1
      task1=i['task']

      schedule.every().day.at(time1).do(lambda:webbrowser.open(task1))

      while True:
        schedule.run_pending()
        time.sleep(1)
        break
        
    pass
  



# def main():
#   while True:
#     for i in tasklist:
#       time1=i['time']
#       time2=time1
#       task1=i['task']

#       global date
#       date = datetime.now()

    
      
#       if date.strftime("%H:%M:%S") == time2:
#         webbrowser.open(task1)
#         break


#       elif date.strftime("%H:%M:%S") == "00:00:00":
#         clear_json()
#         break

#       break
#     break
