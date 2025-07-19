import requests
from bs4 import BeautifulSoup

def get_news():
    #url주소
    url="https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query=%EA%B5%B0%EB%8C%80"

    #url 접근해 정보 가져오기(requests)
    res= requests.get(url)

    soup=BeautifulSoup(res.content, 'html.parser')

    data=soup.find_all('span',class_="sds-comps-text-type-headline1")
    data_list=[]
    for i in data:
        data_list.append(i.text)
    return data_list

for i in get_news():
    print("*************")
    print(i)

