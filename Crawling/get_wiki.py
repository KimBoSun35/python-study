import requests
from bs4 import BeautifulSoup
import sys

input=sys.argv[1]

#url주소
url="https://ko.wikipedia.org/wiki/"+input

#url 접근해 정보 가져오기(requests)
res= requests.get(url)

soup=BeautifulSoup(res.content, 'html.parser')
data=soup.find_all('p')

print(data[0].text)#정보내 필요한 데이터 파싱(BeautifulSoup)

