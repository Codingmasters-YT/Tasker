import tkinter.font as tkFont
import tkinter as tk
from tkinter import messagebox as msg
from tkinter import ttk
import backend as bk
import webbrowser
from datetime import datetime
        
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
        taskname = str(tk.StringVar())
        taskurl = str(tk.StringVar())
        tasktime = str(tk.StringVar())
        
        global InputTitle
        InputTitle=tk.Entry(root, textvariable=taskname)
        InputTitle["borderwidth"] = "1px"
        ft = tkFont.Font(family='Roboto',size=14)
        InputTitle["font"] = ft
        InputTitle["fg"] = "#5fb878"
        InputTitle["bg"] = "#3b4152"
        InputTitle["justify"] = "center"
        InputTitle.place(x=10,y=516,width=183,height=58)
        
        global InputUrl
        InputUrl=tk.Entry(root, textvariable=taskurl)
        InputUrl["borderwidth"] = "1px"
        ft = tkFont.Font(family='Roboto',size=14)
        InputUrl["font"] = ft
        InputUrl["fg"] = "#5fb878"
        InputUrl["bg"] = "#3b4152"
        InputUrl["justify"] = "center"
        InputUrl.place(x=200,y=516,width=493,height=58)


        global InputTime
        InputTime=tk.Entry(root, textvariable=tasktime)
        InputTime["borderwidth"] = "1px"
        ft = tkFont.Font(family='Roboto',size=14)
        InputTime["font"] = ft
        InputTime["fg"] = "#5fb878"
        InputTime["bg"] = "#3b4152"
        InputTime["justify"] = "center"
        InputTime.place(x=700,y=516,width=133,height=58)


        AddBtn=tk.Button(root)
        AddBtn["bg"] = "#5fb878"
        ft = tkFont.Font(family='Roboto',size=14)
        AddBtn["font"] = ft
        AddBtn["fg"] = "#303443"
        AddBtn["activebackground"] = "#5fb88e"
        AddBtn["activeforeground"] = "#303443"
        AddBtn["justify"] = "center"
        AddBtn["text"] = "Add"
        AddBtn.place(x=840,y=516,width=149,height=58)
        AddBtn["command"] = self.AddBtn_command

        TitleMsg=tk.Message(root)
        ft = tkFont.Font(family='Roboto',size=29)
        TitleMsg["font"] = ft
        TitleMsg["fg"] = "#5fb88e"
        TitleMsg["bg"] = "#303443"
        TitleMsg["justify"] = "center"
        TitleMsg["text"] = "Tasks"
        TitleMsg.place(x=340,y=10,width=289,height=29)

        NameLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        NameLabel["font"] = ft
        NameLabel["fg"] = "#5fb88e"
        NameLabel["bg"] = "#303443"
        NameLabel["justify"] = "center"
        NameLabel["text"] = "Task Name"
        NameLabel.place(x=10,y=480,width=182,height=46)

        UrlLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        UrlLabel["font"] = ft
        UrlLabel["fg"] = "#5fb88e"
        UrlLabel["bg"] = "#303443"
        UrlLabel["justify"] = "center"
        UrlLabel["text"] = "URL"
        UrlLabel.place(x=200,y=480,width=493,height=46)

        TimeLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        TimeLabel["font"] = ft
        TimeLabel["fg"] = "#5fb88e"
        TimeLabel["bg"] = "#303443"
        TimeLabel["justify"] = "center"
        TimeLabel["text"] = "Time\n(HH:MM:SS)"
        TimeLabel.place(x=700,y=480,width=133,height=46)

        task_display = tk.Text(root)
        task_display["borderwidth"] = "0px"
        ft = tkFont.Font(family='Times',size=14)
        task_display["font"] = ft
        task_display["fg"] = "#5fb88e"
        task_display["bg"] = "#303443"
        task_display.place(x=10,y=60,width=974,height=396)
        for i in bk.tasklist:
            display=f"{i['name'].upper()}   {i['time']}\n\n"
            task_display.insert(tk.END,display)

        task_display.config(state="disabled")


        

        
    
    def AddBtn_command(self):
        bk.add_task(taskname,taskurl,tasktime)
        InputTitle.delete(0,tk.END)
        InputUrl.delete(0,tk.END)
        InputTime.delete(0,tk.END)
    
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

    
    
bk.add_task("","","")
bk.main()


if __name__ == "__main__":
    
    root = tk.Tk()
    app = App(root)
    root.mainloop()  
    