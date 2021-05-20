from tkinter import *
from tkinter import font

window = Tk()
window.title('Accident')
window['bg'] = 'old lace'
window.geometry("600x850")

# 프로그램 이름 UI
def InitLogo():
    TempFont_1 = font.Font(window, size=70, weight='bold', family='1훈떡볶이 Regular')
    MainText = Label(window, font=TempFont_1, text="Accident")
    MainText.pack()
    MainText['bg'] = 'old lace'
    MainText.place(x=10, y=10)

    TempFont_2 = font.Font(window, size=30, weight='bold', family='1훈떡볶이 Regular')
    SubText = Label(window, font=TempFont_2, text="민방위 대피시설 위치")
    SubText.pack()
    SubText['bg'] = 'old lace'
    SubText.place(x=15, y=90)

# 검색 창 UI
def InitInPutLabel():
    global InPutLabel
    TempFont = font.Font(window, size=20, weight='bold', family='1훈떡볶이 Regular')
    InPutEntry = Entry(window, font=TempFont, width=15, borderwidth=10, relief='ridge')

    InPutEntry.pack()
    InPutEntry.place(x=15, y=155)

# 검색 버튼 UI
def InitSearchButton():
    TempFont = font.Font(window, size=20, weight='bold', family='1훈떡볶이 Regular')
    SearchButton = Button(window, font=TempFont, text="검색", command=SearchButtonAction)
    SearchButton.pack()
    SearchButton.place(x=270, y=155)

def SearchButtonAction(self):
    pass

# 대피시설 도로명 주소 Text UI
def InitRoadAddressBox():
    global RoadAddressBox

    frame = Frame(window)

    RATScrollbar = Scrollbar(frame)
    RATScrollbar.pack(side = 'right', fill = 'y')
    #RATScrollbar.place(x=550, y=300)

    TempFont = font.Font(frame, size = 15, family='1훈떡볶이 Regular')
    RoadAddressBox = Listbox(frame, font = TempFont, width = 53, height = 7, borderwidth = 10,
                               relief='ridge',yscrollcommand=RATScrollbar.set)

    RoadAddressBox.pack(side = 'left')
    #RoadAddressBox.place(x = 15, y = 220)
    RATScrollbar["command"]=RoadAddressBox.yview

    RoadAddressBox.insert(1, "도서관")
    RoadAddressBox.insert(2, "도서관")
    RoadAddressBox.insert(3, "도서관")
    RoadAddressBox.insert(4, "도서관")
    RoadAddressBox.insert(5, "도서관")
    RoadAddressBox.insert(6, "도서관")
    RoadAddressBox.insert(7, "도서관")
    RoadAddressBox.insert(8, "씨발")
    RoadAddressBox.insert(9, "도서관")
    RoadAddressBox.insert(10, "도서관")
    RoadAddressBox.insert(11, "도서관")
    RoadAddressBox.insert(12, "도서관")

    frame.pack()
    frame.place(x = 14, y = 220)
    #RATScrollbar.config(command=RoadAddressBox.yview)

# 메일 서비스 버튼 UI
def MailButton():
    photo = PhotoImage(file="image/Gmail.png").subsample(11,11)
    SearchButton = Button(window, image=photo)
    SearchButton.image = photo
    SearchButton.pack()
    SearchButton.place(x=330, y=680)

# 지도 서비스 버튼 UI
def MapButton():
    photo = PhotoImage(file="image/지도.png").subsample(11,11)
    SearchButton = Button(window, image=photo)
    SearchButton.image = photo
    SearchButton.pack()
    SearchButton.place(x=460, y=680)


InitLogo()
InitInPutLabel()
InitSearchButton()
#InitImage()
MailButton()
MapButton()
InitRoadAddressBox()

window.mainloop()