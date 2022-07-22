"""
this is a cps tester to track how fast you can click
"""
import os
import pathlib
from tkinter import Frame, BOTH, Button, Label, Toplevel, Tk
import sqlite3


class Window(Frame):
    """setup for the window"""

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        self.initialize()

        self.score = "0"
        self.cps = None
        self.first_time = True
        self.score_window = None

        self.remaining = 0

        self.pack(fill=BOTH, expand=1)

        self.history_button = Button(self, text="history")
        self.history_button.place(x=0, y=0)

        self.exit_button = Button(self, text="exit", command=self.exit_tester)
        self.exit_button.place(x=445, y=0)

        self.clicking_button = Button(
            self, text="click", command=self.start_test)
        self.clicking_button.place(x=125, y=200)
        self.clicking_button.configure(width=30, height=10)

        self.timer = Label(self, text="0 seconds")
        self.timer.place(x=225, y=25)

        self.highscore = None
        self.current_highscore = self.cursor.execute(
            """select * from highscore""")
        self.current_highscore = str(self.current_highscore.fetchall()[0][0])
        self.highscore_label = Label(
            self, text="highscore: " + self.current_highscore +
            " clicks in 5 seconds")
        self.highscore_label.place(x=280, y=475)

        self.ok_button = None

    def initialize(self):
        """start the sql"""
        self.dbpath = os.path.join(pathlib.Path.home(), "cpstester.db")
        self.con = sqlite3.connect(self.dbpath)
        self.cursor = self.con.cursor()

        self.cursor.execute("""
        create table if not exists highscore([highscore] integer)
        """)

        self.cursor.execute("""
        create table if not exists history(
        [score] integer,
        [cps] integer,
        [date] string,
        [time] string)
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
            self.timer.configure(text=str(self.remaining) + " seconds")
            self.remaining = self.remaining - 1
            self.after(1000, self.countdown)

    def wait_5_sec(self):
        """create a timer for 5 seconds"""""
        if self.first_time is True:
            self.first_time = False
            self.after(5000, self.reset_score)
            self.countdown(5)
        else:
            self.score = int(self.score) + 1

    def reset_score(self):
        """reset the score"""
        self.create_score_window()
        self.score_window.overrideredirect(1)
        self.highscore = self.cursor.execute("""select * from highscore""")
        self.highscore = self.highscore.fetchall()[0][0]
        if self.highscore < self.score:
            self.cursor.execute(
                """update highscore set highscore = :newhighscore where
                highscore = :currenthighscore""",
                {
                    "newhighscore": self.score,
                    "currenthighscore": self.highscore
                }
            )
            self.con.commit()
            self.highscore_label.configure(
                text="highscore: " + str(self.score) + " clicks in 5 seconds")
            new_highscore = Label(self.score_window, text="new highscore!")
            new_highscore.place(x=75, y=85)

        self.score = 0
        self.first_time = True

    def create_score_window(self):
        """create the score window"""
        self.score = int(self.score) + 1
        self.score_window = Toplevel()
        self.score_window.geometry("250x200")
        self.clicking_button.configure(state="disabled")
        self.ok_button = Button(
            self.score_window, text="ok", command=self.close_second_window)
        self.ok_button.place(x=110, y=120)
        score_label = Label(self.score_window,
                            text="you got " + str(self.score) + " clicks in 5 seconds")
        score_label.place(x=40, y=25)
        self.cps = self.score//5
        cps_label = Label(self.score_window,
                          text="with a cps of " + str(self.cps) + "!")
        cps_label.place(x=75, y=45)
        ranking_label = Label(
            self.score_window, text="ranking: " + self.get_ranking())
        ranking_label.place(x=75, y=65)

    def get_ranking(self):
        """get the ranking of from the cps"""
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
        """close the score window"""
        self.score_window.destroy()
        self.clicking_button.configure(state="active")

    def exit_tester(self):
        """exit out of the cps tester and stop the program"""
        exit()


root = Tk()
app = Window(root)
root.wm_geometry("500x500")
root.wm_title("cps tester")
root.mainloop()
