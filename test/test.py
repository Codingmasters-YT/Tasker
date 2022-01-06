import json

global fileformat
fileformat={
    "tasks": [
        
    ]
}

#clear task.json
def clear_json(filename='task.json'):
    with open(filename,'w') as file:
        json.dump(fileformat, file, indent = 4)

        

 
# function to add to JSON
def write_json(new_data, filename='task.json'):
    with open(filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["tasks"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)
 
    # python object to be appended
#make dictionary wuth keys task, time and values task and time
# while True:
#     task=input("Enter task: ")
#     time=input("Enter time: ")
#     y = {
#         "task": task,
#         "time": time
#     }
     
#     write_json(y)

clear_json()