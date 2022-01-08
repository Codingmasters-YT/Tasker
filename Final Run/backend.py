import json
import webbrowser
from datetime import datetime
import schedule

global fileformat
fileformat={
    "tasks": [
        
    ]
}

def clear_json(filename='./Final Run/task.json'):
    with open(filename,'w') as file:
        json.dump(fileformat, file, indent = 4)


def write_json(new_data, filename='./Final Run/task.json'):
    with open(filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["tasks"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)
        

global tasklist
tasklist = []
  
def add_task(name, task, time1):  
  y={
      "name": name,
      "task": task,
      "time": time1
  }
  
  write_json(y)

  

  f=open('./Final Run/task.json',)
  data=json.load(f)  

  for i in data['tasks']:
    tasklist.append(i)

tasklist=tasklist



def main():
  while True:
    for i in tasklist:
      time1=i['time']
      time2=str(time1)
      task1=str(i['task'])

      global date
      date = datetime.now()

    
      
      if date.strftime("%H:%M:%S") == time2:
        webbrowser.open(task1)
        break


      elif date.strftime("%H:%M:%S") == "00:00:00":
        clear_json()
        break

      break
    break

      

    

add_task("","www.google.com","20:07:30")
main()