from tkinter import *
from random import randint
kamen = 0
nosnutsy = 1
bumaka = 0


K, N, B = range(3)


class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.startUI()

    def startUI(self):
        btn = Button(root, text="камень", font=("Calibri", 15), command=lambda x=K: self.hod(x), bg="#ff0000")
        btn1 = Button(root, text="ножницы", font=("Calibri", 15), command=lambda x=N: self.hod(x), bg="#00ff00")
        btn2 = Button(root, text="бумага", font=("Calibri", 15), command=lambda x=B: self.hod(x), bg="#0000ff")

        btn.place(x=23, y=50, width=120, height=34)
        btn1.place(x=23+120+23+23, y=50, width=120, height=34)
        btn2.place(x=23+120+23+23+120+23+23, y=50, width=120, height=34)

        self.label = Label(root, text="начать игру", bg="#00FF00", font=("calibri", 20))
        self.label.place(x=160, y=10)

    def hod(self, user):
        me =randint(0,2)

        if (me == kamen and user == bumaka) or (me == bumaka and user == nosnutsy) or (me == nosnutsy and user == kamen):
            print("winer")
            self.label.configure(text="winer")
        elif me == bumaka:
            print("nichya")
            self.label.configure(text="nichya")
        else:
            print("game over")
            self.label.configure(text="game over")



if __name__ == '__main__':
    root = Tk()
    root.geometry("500x150+200+200")
    root.title("камень,ножницы,бумага")
    root.resizable(False, False)
    root["bg"] = "#00FF00"
    app = Main(root)
    app.pack()
    root.mainloop()
