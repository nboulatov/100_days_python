from tkinter import *

def button_clicked():
    miles=float(input.get())
    km = miles*1.609344
    my_label.config(text=f"is equal to %.2f Km" % (km))

window = Tk()
window.title("Miles to kilometers converter")
window.minsize(width=500,height=300)
window.config(padx=50,pady=50)

input = Entry(width=10)
input.pack()

my_label = Label(text=f"is equal to 0 Km",font=("Arial",24,"bold"))
my_label.pack()

Button(text="Calculate", command=button_clicked).pack()

window.mainloop()