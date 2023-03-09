from tkinter import *
import random
from tkinter import messagebox

colors = ["Red", "Blue", "Green", "Pink", "Black", "Yellow", "Orange", "White", "Purple", "Brown", "Cyan"]

Score = 0
Time_left = 20


def startGame(event):
    if Time_left == 20:
        Countdown()

    Next_Color()


def Countdown():
    global Time_left
    if Time_left == 0:
        messagebox.showinfo("Time_Left", "Time is over and Your score is "+str(Score))
    if Time_left > 0:
        Time_left -= 1
        timeLabel.config(text="Time Left : " + str(Time_left))
        timeLabel.after(1000, Countdown)


def Next_Color():
    global Score
    global Time_left

    if Time_left > 0:
        e.focus_set()
        if e.get().lower() == colors[1].lower():  # red = red
            Score += 1

        e.delete(0, END)
        random.shuffle(colors)

        label.config(fg=str(colors[1]), text=str(colors[0]))  # red --> black
        ScoreLabel.config(text="Score: " + str(Score))


root = Tk()
root.title("My Color Game")
root.geometry("375x200")
root.resizable(0,0)
root.config(background="Pink")
instructions = Label(root, text="Type the color of the words, and not the word text!", font=("Times New Roman", 12),background="Pink")
instructions.pack()

ScoreLabel = Label(root, text="Press Enter to Start", font=("Times New Roman", 12),background="Pink")
ScoreLabel.pack()

timeLabel = Label(root, text="Time Left: " + str(Time_left), font=("Times New Roman", 12),background="Pink")
timeLabel.pack()

label = Label(root, font=("Times New Roman", 12),background="Pink")
label.pack()

e = Entry(root)
root.bind("<Return>", startGame)
e.pack()
e.focus_set()

root.mainloop()
