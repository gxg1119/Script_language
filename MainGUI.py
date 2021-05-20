from tkinter import *
from tkinter import font

class MainGUI:
    def __init__(self):
        self.window = Tk()
        self.window.title('Accident')
        self.window['bg'] = 'old lace'
        self.window.geometry("600x850")

        self.InitLogo()
        self.InitInPutLabel()
        self.InitSearchButton()
        self.InitImage()
        self.InitMailButton()

        self.window.mainloop()

    # 프로그램 이름 UI
    def InitLogo(self):
        TempFont_1 = font.Font(self.window, size=70, weight='bold', family='1훈떡볶이 Regular')
        MainText = Label(self.window, font=TempFont_1, text="Accident")
        MainText.pack()
        MainText['bg'] = 'old lace'
        MainText.place(x=10, y=10)

        TempFont_2 = font.Font(self.window, size=30, weight='bold', family='1훈떡볶이 Regular')
        SubText = Label(self.window, font=TempFont_2, text="민방위 대피시설 위치")
        SubText.pack()
        SubText['bg'] = 'old lace'
        SubText.place(x=15, y=90)

    # 검색 창 UI
    def InitInPutLabel(self):
        global InPutLabel
        TempFont = font.Font(self.window, size=20, weight='bold', family='1훈떡볶이 Regular')
        InPutLabel = Entry(self.window, font=TempFont, width=15, borderwidth=10, relief='ridge')

        InPutLabel.pack()
        InPutLabel.place(x=15, y=155)

    # 검색 버튼 UI
    def InitSearchButton(self):
        TempFont = font.Font(self.window, size=20, weight='bold', family='1훈떡볶이 Regular')
        SearchButton = Button(self.window, font=TempFont, text="검색", command=self.SearchButtonAction)
        SearchButton.pack()
        SearchButton.place(x=270, y=155)

    def SearchButtonAction(self):
        pass

    # 메일 서비스 버튼 UI
    def InitMailButton(self):
        photo = PhotoImage(file="image/Gmail.png").subsample(11,11)
        SearchButton = Button(self.window, image=photo)
        SearchButton.image = photo
        SearchButton.pack()
        SearchButton.place(x=330, y=680)

MainGUI()