import os
import pathlib
from tkinter import *
import sqlite3


class Window(Frame):
    """setup for the window"""

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        self.initialize()

        self.score = "0"
        self.first_time = True

        self.remaining = 0

        self.pack(fill=BOTH, expand=1)

        self.exit_button = Button(self, text="exit", command=self.exit_tester)
        self.exit_button.place(x=445, y=0)

        self.clicking_button = Button(
            self, text="click", command=self.start_test)
        self.clicking_button.place(x=125, y=200)
        self.clicking_button.configure(width=30, height=10)

        self.timer = Label(self, text="0 seconds")
        self.timer.place(x=225, y=25)

    def initialize(self):
        """start the program"""
        self.dbpath = os.path.join(pathlib.Path.home(), "cpstester.db")
        self.con = sqlite3.connect(self.dbpath)
        self.cursor = self.con.cursor()

        self.cursor.execute("""
        create table if not exists highscore([highscore] integer)
        """)

        length_of_highscore = self.cursor.execute(
            """
            select count (*) from highscore
            """
        )

        length_of_highscore = length_of_highscore.fetchall()[0][0]

        if length_of_highscore == 0:
            self.cursor.execute(
                """
                insert into highscore (highscore) values (0);
                """
            )

        self.con.commit()

    def start_test(self):
        """start the test"""
        self.clicking_button.configure(state="disabled")
        self.clicking_button.pack()
        self.clicking_button.place(x=125, y=200)
        self.wait_5_sec()
        self.clicking_button.configure(state="active")

    def countdown(self, remaining=None):
        """create a countdown"""
        if remaining is not None:
            self.remaining = remaining

        if self.remaining <= 0:
            self.timer.configure(text="0 seconds")
        else:
            self.timer.configure(text="%d seconds" % self.remaining)
            self.remaining = self.remaining - 1
            self.after(1000, self.countdown)

    def wait_5_sec(self):
        if self.first_time is True:
            self.first_time = False
            self.after(5000, self.reset_score)
            self.countdown(5)
        else:
            self.score = int(self.score) + 1

    def reset_score(self):
        """reset the score"""
        self.create_score_window()
        highscore = self.cursor.execute("""select * from highscore""")
        highscore = highscore.fetchall()[0][0]
        if highscore < self.score:
            self.cursor.execute(
                """update highscore set highscore = :newhighscore where highscore = :currenthighscore""",
                {
                    "newhighscore": self.score,
                    "currenthighscore": highscore
                }
            )
            self.con.commit()

        self.score = 0
        self.first_time = True

    def create_score_window(self):
        self.score = int(self.score) + 1
        self.score_window = Toplevel()
        self.clicking_button.configure(state="disabled")
        self.ok_button = Button(
            self.score_window, text="ok", command=self.close_second_window)
        self.ok_button.place(x=75, y=100)
        score_label = Label(self.score_window,
                            text="you got " + str(self.score))
        score_label.place(x=35, y=25)
        self.cps = self.score//5
        cps_label = Label(self.score_window,
                          text="with a cps of " + str(self.cps) + "!")
        cps_label.place(x=35, y=45)
        ranking_label = Label(
            self.score_window, text="ranking: " + self.get_ranking())
        ranking_label.place(x=35, y=65)

    def get_ranking(self):
        if self.cps == 4 or self.cps < 4:
            return "noob"

        if self.cps == 5 or self.cps == 6:
            return "normal"

        if self.cps == 7 or self.cps == 8:
            return "rookie"

        if self.cps == 9 or self.cps == 10:
            return "iron"

        if self.cps == 11 or self.cps == 12:
            return "gold"

        if self.cps == 13 or self.cps == 14:
            return "diamond"

        if self.cps == 15 or self.cps == 16:
            return "master"

        if self.cps == 17 or self.cps == 18:
            return "legend"

        if self.cps == 19 or self.cps == 20:
            return "grandmaster"

        if self.cps == 21 or self.cps > 21:
            return "godlike"

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
