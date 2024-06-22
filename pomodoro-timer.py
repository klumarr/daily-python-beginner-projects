import tkinter as tk
import time

def start_timer(duration, label):
    mins, secs = divmod(duration, 60)
    timeformat = '{:02d}:{:02d}'.format(mins, secs)
    label.config(text=timeformat)
    if duration > 0:
        label.after(1000, start_timer, duration-1, label)
    else:
        label.config(text="Time's up!")

root = tk.Tk()
root.title("Pomodoro Timer")

label = tk.Label(root, font=('Helvetica', 48), text="25:00")
label.pack()

start_button = tk.Button(root, text="Start", command=lambda: start_timer(1500, label))
start_button.pack()

root.mainloop()