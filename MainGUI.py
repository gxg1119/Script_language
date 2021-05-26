from tkinter import *
from tkinter import font
import XMLServer
import mimetypes
import smtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
import folium
import webbrowser

#from XMLServer import *
window = Tk()
window.title('Accident')
color = 'medium purple'
window['bg'] = color
window.geometry("600x850")
tempList = []
Public_num, Private_num = 0, 0

# 프로그램 이름 UI
def InitLogo():
    TempFont_1 = font.Font(window, size=75, weight='bold', family='Hans CalliPunch')
    MainText = Label(window, font=TempFont_1, text="AccIdenT", fg='gray99')
    MainText.pack()
    MainText['bg'] = color
    MainText.place(x=10, y=5)

    TempFont_2 = font.Font(window, size=30, weight='bold', family='Hans CalliPunch')
    SubText = Label(window, font=TempFont_2, text="민방위 대피시설 위치", fg='gray99')
    SubText.pack()
    SubText['bg'] = color
    SubText.place(x=15, y=95)

# 검색 창 UI
def InitInPutLabel():
    global InPutEntry
    TempFont = font.Font(window, size=20, weight='bold', family='1훈떡볶이 Regular')
    InPutEntry = Entry(window, font=TempFont, width=15, borderwidth=10, relief='ridge')

    InPutEntry.pack()
    InPutEntry.place(x=15, y=170)

# 검색 버튼 UI
def InitSearchButton():
    TempFont = font.Font(window, size=20, weight='bold', family='1훈떡볶이 Regular')
    SearchButton = Button(window, font=TempFont, text="검색", command=SearchButtonAction)
    SearchButton.pack()
    SearchButton.place(x=270, y=170)

# 검색 버튼을 눌렀을 때 지명 주소 정보들이 바로 밑 박스들에 나열
def SearchButtonAction():
    idx = 0
    global tempList, Public_num, Private_num
    tempList.clear()
    Public_num, Private_num = 0, 0

    InputImage()
    RoadAddressBox.configure(state='normal')
    RoadAddressBox.delete(0,RoadAddressBox.size()-1)

    for i in XMLServer.DataList:
        if InPutEntry.get() == i[0]:
            tempList.append(i)
            RoadAddressBox.insert(idx, i[6])
            idx += 1

            if i[8] == '공공시설':
                Public_num += 1
            else :
                Private_num += 1
    Graph_logo()
    Graph()
    print(idx, Public_num, Private_num)

# 각 경기도 시 마다의 로고 이미지 UI
def InputImage():
    Image_name = InPutEntry.get()
    image = PhotoImage(file="res/"+Image_name+".png").subsample(4,4)
    imageLabel= Label(window,image=image, width = 200, height = 200)
    imageLabel.image = image
    imageLabel.pack()
    imageLabel.place(x=380, y = 8)

def InitImage():
    image = PhotoImage(file="res/대피소 로고.png").subsample(2,2)
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

    TempFont = font.Font(frame, size = 11, family='맑은 고딕')
    RoadAddressBox = Listbox(frame, font = TempFont, width = 66, height = 6, borderwidth = 10,
                               relief='ridge',yscrollcommand=RATScrollbar.set, selectmode = 'browse')

    RoadAddressBox.bind('<Button-1>',CurSelect)
    RoadAddressBox.pack(side = 'left')
    RATScrollbar["command"]=RoadAddressBox.yview

    frame.pack()
    frame.place(x = 14, y = 230)

def CurSelect(evt):
    global Contentdata
    global latitude
    global longitude
    global Shelter_Name
    Rendertext.configure(state='normal')
    Rendertext.delete(0.0,END)
    index = RoadAddressBox.index(RoadAddressBox.curselection())
    Contentdata = ""

    Rendertext.insert(INSERT, "[1] 시군명 : ")
    Rendertext.insert(INSERT, tempList[index][0])       # 시군명
    Contentdata += str("[1] 시군명 : " + tempList[index][0]) + str("\n\n")
    Rendertext.insert(INSERT, '\n\n')
    Rendertext.insert(INSERT, "[2] 대피시설명 : ")
    Rendertext.insert(INSERT, tempList[index][1])       # 대피 시설명
    Contentdata += str("[2] 대피시설명 : " + tempList[index][1]) + str("\n\n")
    Shelter_Name = tempList[index][1]
    Rendertext.insert(INSERT, '\n\n')
    Rendertext.insert(INSERT, "[3] 인허가 일자 : ")
    Rendertext.insert(INSERT, tempList[index][2])       # 인허가 일자
    Contentdata += str("[3] 인허가 일자 : " + tempList[index][2]) + str("\n\n")
    Rendertext.insert(INSERT, '\n\n')
    Rendertext.insert(INSERT, "[4] 운영상태 : ")
    Rendertext.insert(INSERT, tempList[index][3])       # 운영상태명
    Contentdata += str("[4] 운영상태 : " + tempList[index][3]) + str("\n\n")
    Rendertext.insert(INSERT, '\n\n')
    Rendertext.insert(INSERT, "[5] 면적 : ")
    Rendertext.insert(INSERT, tempList[index][4])       # 소재지 면적 정보
    Contentdata += str("[5] 면적 : " + tempList[index][4]) + str("\n\n")
    Rendertext.insert(INSERT, " m^2")
    Rendertext.insert(INSERT, '\n\n')
    Rendertext.insert(INSERT, "[6] 도로명 주소 : ")
    Rendertext.insert(INSERT, tempList[index][5])       # 소재지 도로명 주소
    Contentdata += str("[6] 도로명 주소 : " + tempList[index][5]) + str("\n\n")
    Rendertext.insert(INSERT, '\n\n')
    Rendertext.insert(INSERT, "[7] 지번 주소 : ")
    Rendertext.insert(INSERT, tempList[index][6])       # 소재지 지번 주소
    Contentdata += str("[7] 지번 주소 : " + tempList[index][6]) + str("\n\n")
    Rendertext.insert(INSERT, '\n\n')
    Rendertext.insert(INSERT, "[8] 우편번호 : ")
    Rendertext.insert(INSERT, tempList[index][7])       # 소재지 우편번호
    Contentdata += str("[8] 우편번호 : " + tempList[index][7]) + str("\n\n")
    Rendertext.insert(INSERT, '\n\n')
    Rendertext.insert(INSERT, "[9] 시설 구분 : ")
    Rendertext.insert(INSERT, tempList[index][8])       # 시설 구분명 (공공 or 민간)
    Contentdata += str("[9] 시설 구분 : " + tempList[index][8]) + str("\n\n")
    latitude = tempList[index][9]
    longitude = tempList[index][10]
# 대피시설 정보 Text UI
def Info_Shelter():
    global Rendertext
    TempFont = font.Font(window, size=10, family='맑은 고딕')
    Rendertext = Text(window, font= TempFont, width=40, height=25, borderwidth = 10,
                relief = 'ridge')
    Rendertext.pack()
    Rendertext.place(x=15, y=390)
    Rendertext.configure(state='disabled')

# 메일 서비스 버튼 UI
#def InitSendEmailLabel():
#    global EmailLabel
#    TempFont = font.Font(window, size=10, weight='bold', family='Consolas')
#    EmailLabel = Entry(window, font=TempFont, width=26, borderwidth=12, relief='ridge')
#    EmailLabel.pack()
#    EmailLabel.place(x=80, y=105)

def MailButton():
    photo = PhotoImage(file="res/Gmail.png").subsample(4,4)
    SearchButton = Button(window, image=photo,command = SendEmailButtonAction)
    SearchButton.image = photo
    SearchButton['bg'] = color
    SearchButton.pack()
    SearchButton.place(x=320, y=680)

def SendEmailButtonAction():
    global EmailLabel
    global SearchListBox
    global myLocationBoxData
    global Contentdata
    Mailadd = "gxg1119@naver.com"
    Rendertext.configure(state='normal')
    Rendertext.delete(0.0, END)
    # iSearchIndex = SearchListBox.curselection()[0]
    # iSearchIndex = SearchListBox.curselection()[0]
    # SearchLibrary()
    sendMail(Mailadd, "민방위 대피시설 정보", Contentdata)
    Rendertext.configure(state='disabled')


def sendMail(ReviceMail, Subject, Content):
    s = smtplib.SMTP("smtp.gmail.com",587) #SMTP 서버 설정
    s.starttls() #STARTTLS 시작
    senderAddr ="zndtldy12@gmail.com"
    s.login("zndtldy12@gmail.com","mirio4155@")
    contents = Content
    msg = MIMEText(contents, _charset='euc-kr')
    msg['Subject'] = Subject
    msg['From'] = senderAddr
    msg['To'] = ReviceMail
    s.sendmail(senderAddr, ReviceMail, msg.as_string())

# 지도 서비스 버튼 UI
def MapButton():
    photo = PhotoImage(file="res/map.png").subsample(4,4)
    SearchButton = Button(window, image=photo, command = Pressed)
    SearchButton.image = photo
    SearchButton['bg'] = color
    SearchButton.pack()
    SearchButton.place(x=460, y=680)
def Pressed():
    # 위도 경도 지정
    map_osm = folium.Map(location=[latitude,longitude], zoom_start=13)
    # 마커 지정
    folium.Marker([latitude,longitude], popup=Shelter_Name).add_to(map_osm)
    # html 파일로 저장
    map_osm.save('osm.html')
    webbrowser.open_new('osm.html')

# 그래프 UI
def Graph_logo():
    city = InPutEntry.get()
    Font = font.Font(window, size=20, weight='bold', family='1훈떡볶이 Regular')
    Text = Label(window, font=Font, text=city+"\n공공시설 민간시설 수", fg='gray99')
    Text.pack()
    Text['bg'] = color
    Text.place(x=345, y=385)

def Graph():
    data = [Public_num, Private_num]
    c_width = 200
    c_height = 200
    c = Canvas(window, width=c_width, height=c_height, bg='white')
    c.pack()
    c.place(x= 357, y=450)

    y_stretch = 0.25
    y_gap = 20
    x_stretch = 20
    x_width = 70
    x_gap = 20
    for x, y in enumerate(data):
        x0 = x * x_stretch + x * x_width + x_gap
        y0 = c_height - (y * y_stretch + y_gap)
        x1 = x * x_stretch + x * x_width + x_width + x_gap
        y1 = c_height - y_gap
        # Here we draw the bar
        c.create_rectangle(x0, y0, x1, y1, fill=color)
        c.create_text(x0 + 25, y0, anchor=SW, text=str(y))
    c.create_text(100, 192, text="공공시설           민간시설")

XMLServer.URLbuilder()

InitLogo()
InitInPutLabel()
InitSearchButton()
InitImage()

RoadAddressBox()
Info_Shelter()

MailButton()
#InitSendEmailLabel()
MapButton()
Graph()
Graph_logo()

window.mainloop()