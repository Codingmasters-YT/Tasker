from re import U
import tkinter.font as tkFont
import tkinter as tk
from tkinter import messagebox as msg
from tkinter import ttk
import json
import webbrowser
import schedule
import time

# storage variables


class App:
    def __init__(self, root):
        width=1000
        height=600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.title("Tasker")
        root.config(bg="#303443")
        root.wm_iconbitmap("./Final Run/to-do.ico")

        # Menubar code
        menubar = tk.Menu(root, background='#303443', fg='#5fb878')
        about_us = tk.Menu(root, tearoff=0)
        contact = tk.Menu(root, tearoff=0)
        rate = tk.Menu(root, tearoff=0)
        quit = tk.Menu(root, tearoff=0)

        about_us.add_command(label = "About Us", command=self.about)
        contact.add_command(label="Contact Us", command=self.contact)
        contact.add_command(label="Mail to Us", command=self.mail)
        rate.add_command(label="Rate Us", command=self.rate)
        quit.add_command(label="Quit", command=self.quit_)

        menubar.add_cascade(label="About", menu=about_us)
        menubar.add_cascade(label="Help", menu=contact)
        menubar.add_cascade(label="Rate", menu=rate)
        menubar.add_cascade(label="Quit", menu=quit)

        root.configure(menu=menubar)

        # Storage variables
        global taskname
        global taskurl
        global tasktime
        taskname = tk.StringVar()
        taskurl = tk.StringVar()
        tasktime = tk.StringVar()
        
        
        InputTitle=tk.Entry(root)
        InputTitle["borderwidth"] = "1px"
        ft = tkFont.Font(family='Roboto',size=14)
        InputTitle["font"] = ft
        InputTitle["fg"] = "#5fb878"
        InputTitle["bg"] = "#3b4152"
        InputTitle["justify"] = "center"
        InputTitle["text"] = "Name For the Task"
        InputTitle["textvariable"] = taskname
        InputTitle.place(x=10,y=516,width=183,height=58)
        InputTitle.insert(0,"Name For the Task")

        InputUrl=tk.Entry(root)
        InputUrl["borderwidth"] = "1px"
        ft = tkFont.Font(family='Roboto',size=14)
        InputUrl["font"] = ft
        InputUrl["fg"] = "#5fb878"
        InputUrl["bg"] = "#3b4152"
        InputUrl["justify"] = "center"
        InputUrl["text"] = "URL of the Website"
        InputUrl["textvariable"] = taskurl
        InputUrl.place(x=200,y=516,width=493,height=58)
        InputUrl.insert(0, "URL for the website")

        InputTime=tk.Entry(root)
        InputTime["borderwidth"] = "1px"
        ft = tkFont.Font(family='Roboto',size=14)
        InputTime["font"] = ft
        InputTime["fg"] = "#5fb878"
        InputTime["bg"] = "#3b4152"
        InputTime["justify"] = "center"
        InputTime["text"] = "HH/MM/SS"
        InputTime["textvariable"] = tasktime
        InputTime.place(x=700,y=516,width=133,height=58)
        InputTime.insert(0, "HH:MM:SS")

        AddBtn=tk.Button(root)
        AddBtn["bg"] = "#5fb878"
        # AddBtn["cursor"] = "Arrow"
        ft = tkFont.Font(family='Roboto',size=14)
        AddBtn["font"] = ft
        AddBtn["fg"] = "#303443"
        AddBtn["activebackground"] = "#5fb88e"
        AddBtn["activeforeground"] = "#303443"
        AddBtn["justify"] = "center"
        AddBtn["text"] = "Add"
        AddBtn.place(x=840,y=516,width=149,height=58)
        # AddBtn["command"] = self.GButton_294_command

        TitleMsg=tk.Message(root)
        ft = tkFont.Font(family='Roboto',size=29)
        TitleMsg["font"] = ft
        TitleMsg["fg"] = "#5fb88e"
        TitleMsg["bg"] = "#303443"
        TitleMsg["justify"] = "center"
        TitleMsg["text"] = "Tasks"
        TitleMsg.place(x=340,y=10,width=289,height=29)

    

    # def GButton_294_command(self):
    #     task = taskname.get()
    #     url = taskurl.get()
    #     time = tasktime.get()
        

    #     global fileformat
    #     fileformat={
    #         "tasks": [
        
    #         ]
    #     }
    #     with open("./File Run/tasks.json", "r") as f:
    #         fileformat = json.load(f)
    #         fileformat["tasks"].append({"task": task, "url": url, "time": time})

    #     while True:
    #         schedule.every().day.at(time).do(webbrowser.open(url))
    #         schedule.run_pending()
    #         time.sleep(1)
    
    def about(self):
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

    def contact(self):
        msg.showinfo("Contact Us", "Contact us at: 98XXXXXXXX")

    def mail(self):
        msg.showinfo("Mail Us", "Mail us at: xxxxxx.gmail.com")
    def rate(self):
        ratev = msg.askquestion("Rate us", "Was your experience at our Application good?")
        if ratev == "yes":  
            msg.showinfo("Thank you for your Feeback","Great!! Please rate us at AppStore - PyTkDevelopers")
        else:
            msg.showinfo("Thank you for your Feeback", "Please tell what went wrong, we will contact you soon - PyTkDevelopers")
    def quit_(self):
        exit()

    # def clear_json(filename='Final Run\\task.json'):
    #         with open(filename,'w') as file:
    #             json.dump(fileformat, file, indent = 4)

    # while True:
    #     schedule.every().day.at("00:00:00").do(clear_json)
    #     schedule.run_pending()
    #     time.sleep(1)




if __name__ == "__main__":
    root = tk.Tk()

    app = App(root)
    root.mainloop()