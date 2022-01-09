import backend as bk
import graphics as gr
import threading

def gui_thread():
    root = gr.tk.Tk()
    app = gr.App(root)
    root.mainloop()

def backend_thread():
    for i in bk.tasklist:
    
        time2=i['time']
        # time2=time1
        task1=i['task']
        bk.schedule.every().day.at(time2).do(lambda: bk.webbrowser.open(task1))
        
    while True:
        bk.schedule.run_pending()
        bk.time.sleep(1)
    

# use threading
if __name__ == "__main__":
    thread1 = threading.Thread(target=gui_thread)
    thread2 = threading.Thread(target=backend_thread)
    thread1.start()
    while True:
        thread2.start()