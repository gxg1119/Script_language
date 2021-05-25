from tkinter import *
from tkinter import font
import XMLServer

window = Tk()
window.title('Accident')
color = 'SkyBlue1'
window['bg'] = color
window.geometry("600x850")

# 프로그램 이름 UI
def InitLogo():
    TempFont_1 = font.Font(window, size=75, weight='bold', family='Hans CalliPunch')
    MainText = Label(window, font=TempFont_1, text="AccIdenT")
    MainText.pack()
    MainText['bg'] = color
    MainText.place(x=10, y=5)

    TempFont_2 = font.Font(window, size=30, weight='bold', family='Hans CalliPunch')
    SubText = Label(window, font=TempFont_2, text="민방위 대피시설 위치")
    SubText.pack()
    SubText['bg'] = color
    SubText.place(x=15, y=95)

# 검색 창 UI
def InitInPutLabel():
    global InPutEntry
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

# 검색 버튼을 눌렀을 때 지명 주소 정보들이 바로 밑 박스들에 나열
def SearchButtonAction():
    idx = 0

    InputImage()
    RoadAddressBox.configure(state='normal')
    RoadAddressBox.delete(0,RoadAddressBox.size()-1)

    for i in XMLServer.DataList:
        tempList = i

        if InPutEntry.get() == tempList[0]:
            RoadAddressBox.insert(idx, i[6])
            idx += 1

# 각 경기도 시 마다의 로고 이미지 UI
def InputImage():
    Image_name = InPutEntry.get()
    image = PhotoImage(file="logo/"+Image_name+".png").subsample(4,4)
    imageLabel= Label(window,image=image, width = 200, height = 200)
    imageLabel.image = image
    imageLabel.pack()
    imageLabel.place(x=380, y = 8)

def InitImage():
    image = PhotoImage(file="logo/대피소 그림.png").subsample(2,2)
    imageLabel= Label(window,image=image, width = 200, height = 200, bg = color)
    imageLabel.image = image
    imageLabel.pack()
    imageLabel.place(x=380, y = 8)

# 대피시설 도로명 주소 ListBox UI
def RoadAddressBox():
    global RoadAddressBox

    frame = Frame(window)

    RATScrollbar = Scrollbar(frame)
    RATScrollbar.pack(side = 'right', fill = 'y')

    TempFont = font.Font(frame, size = 13, family='1훈떡볶이 Regular')
    RoadAddressBox = Listbox(frame, font = TempFont, width = 59, height = 7, borderwidth = 10,
                               relief='ridge',yscrollcommand=RATScrollbar.set)

    RoadAddressBox.pack(side = 'left')
    RATScrollbar["command"]=RoadAddressBox.yview

    frame.pack()
    frame.place(x = 14, y = 220)

# 대피시설 정보 Text UI
def Info_Shelter():
    global Rendertext
    TempFont = font.Font(window, size=15, family='1훈떡볶이 Regular')
    Rendertext = Text(window, font= TempFont, width=30, height=20, borderwidth = 10,
                relief = 'ridge')
    Rendertext.pack()
    Rendertext.place(x=15, y=400)

# 메일 서비스 버튼 UI
def MailButton():
    photo = PhotoImage(file="image/Gmail1.png").subsample(4,5)
    SearchButton = Button(window, image=photo)
    SearchButton.image = photo
    SearchButton['bg'] = 'old lace'
    SearchButton.pack()
    SearchButton.place(x=330, y=680)

# 지도 서비스 버튼 UI
def MapButton():
    photo = PhotoImage(file="image/gmap.png").subsample(5,5)
    SearchButton = Button(window, image=photo)
    SearchButton.image = photo
    SearchButton['bg'] = 'old lace'
    SearchButton.pack()
    SearchButton.place(x=470, y=680)

XMLServer.URLbuilder()

InitLogo()
InitInPutLabel()
InitSearchButton()
InitImage()

RoadAddressBox()
Info_Shelter()

MailButton()
MapButton()

window.mainloop()