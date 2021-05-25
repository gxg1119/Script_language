import http.client
from tkinter import INSERT
from xml.etree import ElementTree

KoreaList = []
ChinaList = []
JapanList = []
ItalyList = []
CafeList = []
FamousList = []

CityList = ['가평군', '고양시', '과천시', '광명시', '광주시', '구리시', '군포시', '김포시',
            '남양주시', '동두천시', '부천시', '성남시', '수원시', '시흥시', '안산시', '안성시',
            '안양시', '양주시', '양평군', '여주시', '연천군', '오산시', '용인시', '의왕시',
            '의정부시', '이천시', '파주시', '평택시', '포천시', '하남시', '화성시']


def URLbuilder(CategoryNum):   #카테고리별 URL
    global KEY
    if CategoryNum == 0:
        KEY = "/CivilDefenseEvacuation?KEY=af4823136cc84043934e53c8e8ba1d66"

    URLrequest(CategoryNum, KEY + str("&pSize=5000"))

def URLrequest(CategoryNum, KEY):  # 카테고리별 파싱
    con = http.client.HTTPSConnection("openapi.gg.go.kr")
    con.request("GET", KEY)
    req = con.getresponse()

    if req.status == 200:
        temp = req.read().decode('utf-8')
        #print(temp)
        print("Data Downloading Complete!")
    else:
        print("OpenAPI request Failed!")

def XmlToList1(CategoryNum, xml):  # xml → 카테고리별(맛집 외) 리스트로
    tree = ElementTree.fromstring(xml)

    for restaurant in tree.findall('./row'):
        City = restaurant.find('SIGUN_NM')                  # 시군명(1)
        Name = restaurant.find('BIZPLC_NM')                 # 사업장명(3)
        RoadAddress = restaurant.find('REFINE_ROADNM_ADDR') # 도로명 주소(19)
        Address = restaurant.find('REFINE_LOTNO_ADDR')      # 지번 주소(20)
        Post = restaurant.find('REFINE_ZIP_CD')             # 우편 번호(21)
        Lat = restaurant.find('REFINE_WGS84_LAT')           # 위도(22)
        Long = restaurant.find('REFINE_WGS84_LOGT')         # 경도(23)
        Open = restaurant.find('LICENSG_DE')                # 인허가일자(4)

        if CategoryNum == 0:
            KoreaList.append([City.text, Name.text, RoadAddress.text, Address.text, Post.text, Lat.text, Long.text, Open.text])

def getList(CategoryNum):
    if CategoryNum == 0:
        return KoreaList



URLbuilder(0)
