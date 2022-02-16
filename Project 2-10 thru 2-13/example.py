import tkinter as tk

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class LogIn(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="LogIn")
       label.pack(side="top", fill="both", expand=True)

class SignUp(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="SignUp")
       label.pack(side="top", fill="both", expand=True)

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = LogIn(self)
        p2 = SignUp(self)
        

        buttonframe = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)       

        b1 = tk.Button(buttonframe, text="LogIn", command=root.mainloop)
        b2 = tk.Button(buttonframe, text="SignUp", command=root)

        b1.pack(side="left")
        b2.pack(side="right")

if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.geometry("400x400")
    root.mainloop()