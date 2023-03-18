from tkinter import *
import turtle

def button_clicked():
    print("Got clicked console")
    #my_label.config(text="Got clicked")
    my_label.config(text=input.get())

window = Tk()
window.title("My first GUI program")
window.minsize(width=500,height=300)
window.config(padx=20,pady=20)

my_label = Label(text="I am a label", font=("Arial",24,"bold"))
my_label.pack()
my_label.grid(row=0, column=0)
my_label.config(padx=50,pady=50)
#my_label.place(x=100,y=0)
#my_label["text"] = "hi"

button = Button(text="Click me", command=button_clicked)
button.grid(row=1, column=1)
#button.pack()

new_button = Button(text="New Button")
new_button.grid(row=0, column=3)

input = Entry(width=10)
input.grid(row=3, column=4)
#input.pack()
window.mainloop()