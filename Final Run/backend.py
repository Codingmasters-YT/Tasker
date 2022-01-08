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


def write_json(new_data, filename='Final Run\\task.json'):
    with open(filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["tasks"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)
        

def add_task(name, task, time1):  
  y={
      "name": name,
      "task": task,
      "time": time1
  }
  
  write_json(y)

  global tasklist
  tasklist = []
  f=open('Final Run\\task.json',)
  data=json.load(f)
  for i in data['tasks']:
    tasklist.append(i)


def tasks():
  task=tasklist[0]['task']
  webbrowser.open(task)

def main():
  while True:

    schedule.every().day.at(tasklist[0]['time']).do(tasks)
    schedule.every().day.at("00:00:00").do(clear_json)
    schedule.run_pending()
    time.sleep(1)




  # Today : Backend
  # Tomorrow : Frontend
  # Day next to tomorrow: Backend and Frontend LINKING
