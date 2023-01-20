from tkinter import *
from time import time

start = time()
end = time() + 5


def five_seconds_passed():
    global start, end, first_text
    if start == end:
        second_text = entry.get()
        if first_text == second_text:
            entry.delete(0, END)
        start = time()
        end = time() + 5
        first_text = second_text

    window.after(1000, five_seconds_passed)
    start += 1


def close():
    window.destroy()


def delete_entry():
    entry.delete(0, END)


window = Tk()
window.title("Disappearing Text Writing App")
window.minsize(width=500, height=450)

entry = Entry(window)
entry.insert(0, "Type here")
entry.place(x=130, y=60, width=250, height=350)

close_app = Button(text="Close App", command=close)
close_app.place(x=0, y=0)

delete = Button(text="Delete Entry", command=delete_entry)
delete.place(x=100, y=0)

window.after(1000, five_seconds_passed)

first_text = entry.get()

window.mainloop()
