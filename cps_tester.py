from tkinter import *

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        
        self.score = "0"
        self.first_time = True

        self.pack(fill=BOTH, expand=1)

        self.exit_button = Button(self, text="exit", command=self.exit_tester)
        self.exit_button.place(x=445, y=0)

        self.clicking_button = Button(
            self, text="click", command=self.start_test)
        self.clicking_button.place(x=125, y=200)
        self.clicking_button.configure(width=30, height=10)

    def start_test(self):
        self.clicking_button.configure(state="disabled")
        self.clicking_button.pack()
        self.clicking_button.place(x=125, y=200)
        self.wait_5_sec()
        self.clicking_button.configure(state="active")

    def wait_5_sec(self):
        if self.first_time is True:
            self.first_time = False
            self.clicking_button.after(5000, self.reset_score)
        else:
            self.score = int(self.score) + 1
    
    def reset_score(self):
        self.score = int(self.score) + 1
        self.score_window = Toplevel()
        self.clicking_button.configure(state="disabled")
        self.ok_button = Button(self.score_window, text="ok", command=self.close_second_window)
        self.ok_button.place(x=75, y=100)
        score_label = Label(self.score_window, text="you got " + str(self.score))
        score_label.place(x=35, y=25)
        cps = self.score//5
        cps_label = Label(self.score_window, text="with a cps of " + str(cps) + "!")
        cps_label.place(x=35, y=45)
        self.score = 0
        self.first_time = True

    def close_second_window(self):
        self.score_window.destroy()
        self.clicking_button.configure(state="active")
    
    def exit_tester(self):
        exit()


root = Tk()
app = Window(root)
root.wm_geometry("500x500")
root.wm_title("cps tester")
root.mainloop()
