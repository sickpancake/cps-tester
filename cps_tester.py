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
        self.clicking_button.place(x=220, y=200)

    def start_test(self):
        self.clicking_button.configure(state="disabled")
        self.clicking_button.pack()
        self.clicking_button.place(x=220, y=200)
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
        print("you got " + str(self.score) + " clicks per 5 second")
        self.score = 0
        self.first_time = True
    
    def exit_tester(self):
        exit()


root = Tk()
app = Window(root)
root.wm_geometry("500x500")
root.wm_title("cps tester")
root.mainloop()
