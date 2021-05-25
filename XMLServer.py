import http.client
from tkinter import INSERT
from xml.etree import ElementTree

DataList = []

CityList = ['가평군', '고양시', '과천시', '광명시', '광주시', '구리시', '군포시', '김포시',
            '남양주시', '동두천시', '부천시', '성남시', '수원시', '시흥시', '안산시', '안성시',
            '안양시', '양주시', '양평군', '여주시', '연천군', '오산시', '용인시', '의왕시',
            '의정부시', '이천시', '파주시', '평택시', '포천시', '하남시', '화성시']


def URLbuilder(CategoryNum):   #카테고리별 URL
    global KEY
    global NAME
    idx = 0
    if CategoryNum == 0:
        KEY = "/CivilDefenseEvacuation?KEY=af4823136cc84043934e53c8e8ba1d66"

    URLrequest(CategoryNum, KEY + str("&pIndex=1") + str("&pSize=1000") + str("&SIGUN_NM="))
    URLrequest(CategoryNum, KEY + str("&pIndex=2") + str("&pSize=1000") + str("&SIGUN_NM="))
    URLrequest(CategoryNum, KEY + str("&pIndex=3") + str("&pSize=1000") + str("&SIGUN_NM="))
    URLrequest(CategoryNum, KEY + str("&pIndex=4") + str("&pSize=1000") + str("&SIGUN_NM="))
    URLrequest(CategoryNum, KEY + str("&pIndex=5") + str("&pSize=1000") + str("&SIGUN_NM="))
    URLrequest(CategoryNum, KEY + str("&pIndex=6") + str("&pSize=1000") + str("&SIGUN_NM="))


def URLrequest(CategoryNum, KEY):  # 카테고리별 파싱
    con = http.client.HTTPSConnection("openapi.gg.go.kr")
    con.request("GET", KEY)
    req = con.getresponse()

    if req.status == 200:
        temp = req.read().decode('utf-8')
        print("Data Downloading Complete!")
        XmlToList1(0, temp)
    else:
        print("OpenAPI request Failed!")

def XmlToList1(CategoryNum,temp):  # xml → 카테고리별(맛집 외) 리스트로
    tree = ElementTree.fromstring(temp)
    for restaurant in tree.findall('./row'):
        City = restaurant.find('SIGUN_NM')                  # 시군명(1)
        Name = restaurant.find('BIZPLC_NM')                 # 대피시설명 (2)
        RoadAddress = restaurant.find('REFINE_ROADNM_ADDR') # 도로명 주소(19)
        Address = restaurant.find('REFINE_LOTNO_ADDR')      # 지번 주소(20)
        Post = restaurant.find('ROADNM_ZIP_CD')             # 우편 번호(21)
        Lat = restaurant.find('REFINE_WGS84_LAT')           # 위도(22)
        Long = restaurant.find('REFINE_WGS84_LOGT')         # 경도(23)
        Open = restaurant.find('BSN_STATE_NM')                # 운영상태

        #print(Name)
        DataList.append([City.text, Name.text, RoadAddress.text, Address.text, Post.text, Lat.text, Long.text, Open.text])
        #print(City.text)


def getList(CategoryNum):
    if CategoryNum == 0:
        return DataList

for i in DataList:
    print(i)
