from tkinter import *
import math

PINK = '#e2979c'
RED = '#E7305B'
GREEN = '#9BDEAC'
YELLOW = '#f7f5dd'
FONT_NAME = "Courier"
WORK_MIN = 10
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
timer = None

def start_timer():
    global rep
    rep +=1
    work_sec = WORK_MIN #*60
    short_break_sec = SHORT_BREAK_MIN #*60
    long_break_sec = LONG_BREAK_MIN #*60

    if rep == 1 or rep == 3 or rep == 5 or rep == 7:
        count_down(work_sec)
        my_label.config(text="WORK", fg=RED)
    elif rep == 2 or rep == 4 or rep == 6:
        count_down(short_break_sec)
        my_label.config(text="BREAK", fg=PINK)
    else:
        count_down(long_break_sec)
        my_label.config(text="Long Break", fg=GREEN)

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text='00:00')
    my_label.config(text="Timer", fg=GREEN)
    global rep
    rep = 0

def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(rep/2)):
            mark +="✅"
        check_marks.config(text = mark)
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")



window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=YELLOW)

canvas = Canvas(width=360,height=434)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(180,217, image = tomato_img)
timer_text = canvas.create_text(180,217, text='00:00', fill='white',font=(FONT_NAME,35,"bold"))
canvas.grid(row=1, column=2)

my_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME,35,"bold"))
my_label.grid(row=0, column=2)

start = Button(text="Start",command=start_timer,bg=YELLOW,font=(FONT_NAME,12,"bold"))
start.grid(row=3, column=0)

reset = Button(text="Reset",bg=YELLOW,font=(FONT_NAME,12,"bold"),command=reset_timer)
reset.grid(row=3, column=3)

check_marks = Label(bg=YELLOW,fg=GREEN)
check_marks.grid(row=3,column=2)

window.mainloop()