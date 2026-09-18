from tkinter import *
from datetime import date

window=Tk()
window.title('window 1')
window.geometry('400x300')

lbl=Label(text="hey there!", fg="white", bg="#072F5F", height=1, width=300)

name_lbl=Label(text="full name", bg="#3895D3")
name_entry=Entry()
hobby_lbl=Label(text="whats ur hobby", bg="#3895D3")
hobby_entry=Entry()

def display():
    name=name_entry.get()
    hobby=hobby_entry.get()

    global message
    message = "welcome to my application \n today's date is : "
    greet = "hello "+name+"\n"
    hobbies = "i also like "+hobby+"\n"
    text_box.insert(END, greet)
    text_box.insert(END, hobbies)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

text_box=Text(height=999)

btn=Button(text="Begin", command=display, height=1, bg="#1261A0", fg='white')

lbl.pack()
name_lbl.pack()
name_entry.pack()
hobby_lbl.pack()
hobby_entry.pack()
btn.pack()
text_box.pack()

window.mainloop()