import json
import webbrowser
import schedule
import time

global fileformat
fileformat={
    "tasks": [
        
    ]
}

def clear_json(filename='Final Run\\task.json'):
    with open(filename,'w') as file:
        json.dump(fileformat, file, indent = 4)
        

task = input("whats do you want to open:")
timefortask = input("when do you want to do it: ")

def tasks():
  webbrowser.open(task)

while True:
  
  schedule.every().day.at(timefortask).do(tasks)
  schedule.every().day.at("00:00:00").do(clear_json)
  schedule.run_pending()
  time.sleep(1)




  # Today : Backend
  # Tomorrow : Frontend
  # Day next to tomorrow: Backend and Frontend LINKING