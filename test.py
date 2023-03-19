import requests
from bs4 import BeautifulSoup
import copy
import googletrans
from googletrans import Translator
from selenium import webdriver
import urllib.request
from urllib.request import Request
import time
import codecs


# Creating translator object
translator = Translator()
# Checking supporting languages
langs = googletrans.LANGCODES
# testing translator
#result = translator.translate("Hello World",src="en",dest="hi")
# test result:
#print(result)


url = "https://www.classcentral.com/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}


# Method - 2 Using Selenium:
driver = webdriver.Chrome("C:/Users/D4rkS/Desktop/chromedriver_win32/chromedriver.exe")
time.sleep(1)
driver.get("https://www.classcentral.com/")
time.sleep(5)
with codecs.open("selen2_index.html","w","utf-8") as f:
    f.write(driver.page_source)
soup_2 = BeautifulSoup(driver.page_source,"html.parser")


print(soup_2.find_all("p",{"class":"row vert-align-top horz-align-left text-2 medium-up-text-1 margin-top-xsmall padding-horz-xxsmall"})[0].replace_with(translator.translate(soup_2.find_all("p",{"class":"row vert-align-top horz-align-left text-2 medium-up-text-1 margin-top-xsmall padding-horz-xxsmall"})[0].text,dest="hi")))

print(print(soup_2.find_all("p",{"class":"row vert-align-top horz-align-left text-2 medium-up-text-1 margin-top-xsmall padding-horz-xxsmall"})[0].text))

driver.close()

 