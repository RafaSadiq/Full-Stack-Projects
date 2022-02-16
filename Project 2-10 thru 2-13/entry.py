from tkinter import *

root = Tk()


ent = Entry(root, width=30)
ent.pack()


def myClick():
    myLabel = Label(root, text="look!")
    myLabel.pack()



myButton1 = Button(root, text = 'SignUp', bd = '5', command = myClick)
myButton2 = Button(root, text = 'Login', bd = '5', command = root.destroy)

myButton1.pack(side = 'top')
myButton2.pack(side = 'top')

root.geometry('1000x800')
root.mainloop()


