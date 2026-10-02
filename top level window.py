from tkinter import *

root=Tk()
root.geometry("400x300")
root.title("main")

def topwin():
    top=Toplevel()
    top.geometry("200x200")
    top.title("toplevel")

    l2=Label(top, text="oops your computer got a virus XD")
    l2.pack()

    top.mainloop()

l=Label(root, text="this is root window")
btn=Button(root, text="click here(very safe)", command=topwin)

l.pack()
btn.pack()

root.mainloop()