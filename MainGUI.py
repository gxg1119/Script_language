from tkinter import *
from tkinter import font

class MainGUI:
    def __init__(self):
        self.window = Tk()
        self.window.title('Accident')
        self.window['bg'] = 'old lace'
        self.window.geometry("600x850")
        
        self.InitLogo()
        self.window.mainloop()

    def InitLogo(self):
        TempFont_1 = font.Font(self.window, size=70, weight='bold', family='1훈떡볶이 Regular')
        MainText = Label(self.window, font=TempFont_1, text="Accident")
        MainText.pack()
        MainText.place(x=10, y=10)

        TempFont_2 = font.Font(self.window, size=30, weight='bold', family='1훈떡볶이 Regular')
        SubText = Label(self.window, font=TempFont_2, text="민방위 대피시설 위치")
        SubText.pack()
        SubText.place(x=15, y=90)

MainGUI()