from tkinter import *
from random import randint

K, N, B = range(3)


class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.startUI()

    def startUI(self):
        btn = Button(root, text="камень", font=("Calibri", 15), command=lambda x=K: self.hod(x))
        btn1 = Button(root, text="ножницы", font=("Calibri", 15), command=lambda x=N: self.hod(x))
        btn2 = Button(root, text="бумага", font=("Calibri", 15), command=lambda x=B: self.hod(x))

        btn.place(x=10, y=50, width=100, height=20)
        btn1.place(x=130, y=50, width=100, height=20)
        btn2.place(x=244, y=50, width=100, height=20)

        self.label = Label(root, text="начать игру", bg="#FFF", font=("calibri", 20))
        self.label.place(x=10, y=10)

    def hod(self, button):
        homber =(randint,0,3)
        print("Button", button)



if __name__ == '__main__':
    root = Tk()
    root.geometry("500x500+200+200")
    root.title("камень,ножницы,бумага")
    root.resizable(False, False)
    root["bg"] = "#fff"
    app = Main(root)
    app.pack()
    root.mainloop()
