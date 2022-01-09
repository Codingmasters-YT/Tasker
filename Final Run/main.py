import backend as bk
import graphics as gr
import threading


def gui_thread():
    root = gr.tk.Tk()
    app = gr.App(root)
    root.mainloop()

def backend_thread():
    bk.main()
    

# use threading
if __name__ == "__main__":
    thread1 = threading.Thread(target=gui_thread)
    thread2 = threading.Thread(target=backend_thread)
    thread1.start()
    thread2.start()