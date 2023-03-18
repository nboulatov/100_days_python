from tkinter import *

window = Tk()
window.geometry("700x350")

def on_click():
   canvas.itemconfig(line, fill="green")

canvas = Canvas(window, width=500, height=300)
canvas.pack()

line = canvas.create_line(100, 200, 200, 35, fill="yellow", width=5)

Button(window, text="Update the Color", command=on_click).pack()

window.mainloop()