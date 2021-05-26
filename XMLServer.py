import http.client
from tkinter import INSERT
from xml.etree import ElementTree

DataList = []

CityList = ['가평군', '고양시', '과천시', '광명시', '광주시', '구리시', '군포시', '김포시',
            '남양주시', '동두천시', '부천시', '성남시', '수원시', '시흥시', '안산시', '안성시',
            '안양시', '양주시', '양평군', '여주시', '연천군', '오산시', '용인시', '의왕시',
            '의정부시', '이천시', '파주시', '평택시', '포천시', '하남시', '화성시']

def URLbuilder():
    global KEY

    KEY = "/CivilDefenseEvacuation?KEY=af4823136cc84043934e53c8e8ba1d66"

    # 총 데이터 수 5542개 - 1페이지에 1000개 씩, 6페이지
    URLrequest(KEY + str("&pIndex=1") + str("&pSize=1000") + str("&SIGUN_NM="))
    URLrequest(KEY + str("&pIndex=2") + str("&pSize=1000") + str("&SIGUN_NM="))
    URLrequest(KEY + str("&pIndex=3") + str("&pSize=1000") + str("&SIGUN_NM="))
    URLrequest(KEY + str("&pIndex=4") + str("&pSize=1000") + str("&SIGUN_NM="))
    URLrequest(KEY + str("&pIndex=5") + str("&pSize=1000") + str("&SIGUN_NM="))
    URLrequest(KEY + str("&pIndex=6") + str("&pSize=1000") + str("&SIGUN_NM="))


def URLrequest(KEY):
    con = http.client.HTTPSConnection("openapi.gg.go.kr")
    con.request("GET", KEY)
    req = con.getresponse()

    if req.status == 200:
        temp = req.read().decode('utf-8')
        print("Data Downloading Complete!")
        XmlToList(temp)
    else:
        print("OpenAPI request Failed!")

def XmlToList(temp):
    tree = ElementTree.fromstring(temp)

    for shelter in tree.findall('./row'):

        City = shelter.find('SIGUN_NM')                     # 시군명
        if City.text == None:
            City.text = '시군명 정보 없음'

        Shelter_Name = shelter.find('BIZPLC_NM')            # 대피시설명
        if Shelter_Name.text == None:
            Shelter_Name.text = '대피시설명 정보 없음'

        License_date = shelter.find('LICENSG_DE')           # 인허가 일자
        if License_date.text == None:
            License_date.text = '인허가 일자 정보 없음'

        Open = shelter.find('BSN_STATE_NM')                 # 운영상태
        if Open.text == None:
            Open.text = '운영상태 정보 없음'

        Area = shelter.find('LOCPLC_AR_INFO')               # 소재지 면적정보
        if Area.text == None:
            Area.text = '면적 정보 없음'

        RoadAddress = shelter.find('REFINE_ROADNM_ADDR')     # 소재지 도로명 주소
        if RoadAddress.text == None:
            RoadAddress.text = '도로명 주소 정보 없음'

        Address = shelter.find('REFINE_LOTNO_ADDR')         # 소재지 지번 주소
        if Address.text == None:
            Address.text = '지번 주소 정보 없음'

        Post = shelter.find('ROADNM_ZIP_CD')                # 소재지 우편 번호
        if Post.text == None:
            Post.text = '우편번호 정보 없음'

        Public_Private = shelter.find('FACLT_DIV_NM')       # 시설 구분명 (공공, 민간)
        if Public_Private.text == None:
            Public_Private.text = '시설 구분 정보 없음'

        Lat = shelter.find('REFINE_WGS84_LAT')              # 위도
        if Lat.text == None:
            Lat.text = '위도 정보 없음'

        Long = shelter.find('REFINE_WGS84_LOGT')            # 경도
        if Long.text == None:
            Long.text = '경도 정보 없음'

        DataList.append([City.text, Shelter_Name.text, License_date.text, Open.text, Area.text,
                         RoadAddress.text, Address.text, Post.text, Public_Private.text, Lat.text, Long.text])


#for i in DataList:
    #print(i)
