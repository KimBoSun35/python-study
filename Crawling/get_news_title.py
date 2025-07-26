from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://www.naver.com")
search_box = driver.find_element(By.CSS_SELECTOR, "input#query.search_input")
search_box.send_keys("청년취업률")
search_box.send_keys(Keys.ENTER)
news_tab=driver.find_element(By.LINK_TEXT, "뉴스")
news_tab.click()
time.sleep(2)
html=driver.page_source
html
html=driver.page_source
soup=BeautifulSoup(html,"lxml")#pip install lxml
title=soup.select("span.sds-comps-text-type-headline1")
for i in title:
    print(i.get_text(strip=True))

len(title)   