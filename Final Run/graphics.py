from _typeshed import HasFileno, StrOrBytesPath
from tkinter import *
import tkinter as tk
from tkinter import messagebox as msg


root = tk.Tk()
root.geometry("600x300")
root.maxsize(600,300)
root.minsize(600,300)
root.title("Tasker")
# root.wm_iconbitmap("covid.ico")
def contact():
    msg.showinfo("Contact Us", "Contact us at: 98XXXXXXXX")

def mail():
    msg.showinfo("Mail Us", "Mail us at: xxxxxx.gmail.com")
def rate():
    ratev = msg.askquestion("Rate us", "Was your experience at our Application good?")
    if ratev == "yes":  
        msg.showinfo("Thank you for your Feeback","Great!! Please rate us at AppStore - PyTkDevelopers")
    else:
        msg.showinfo("Thank you for your Feeback", "Please tell what went wrong, we will contact you soon - PyTkDevelopers")

def quit_():
    exit()


menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)

filemenu.add_command(label="New", command=contact)
filemenu.add_command(label="Open", command=contact)
filemenu.add_command(label="Save", command=contact)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

# create a submenu
submenu = Menu(filemenu, tearoff=0)
submenu.add_command(label="Dark Mode", command=contact)
submenu.add_command(label="Light Mode", command=mail)
filemenu.add_cascade(label="Theme", menu=submenu)


helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=contact)
helpmenu.add_command(label="About...", command=contact)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)

#make a beatiful button




submit = Button(root, text="Submit", bg="#20C20E", fg="white", relief="raised")
# flat, groove, raised, ridge, solid, or sunken

submit.grid()
root.mainloop()