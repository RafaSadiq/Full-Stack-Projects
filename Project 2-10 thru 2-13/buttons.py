from tkinter import *

root = Tk()



def myClick():
    myLabel = Label(root, text="look!")
    myLabel.pack()


root.geometry('1000x800')
myButton1 = Button(root, text = 'SignUp', bd = '5', command = myClick)
myButton2 = Button(root, text = 'Login', bd = '5', command = root.destroy)

myButton1.pack(side = 'top')
myButton2.pack(side = 'top')


root.mainloop()
