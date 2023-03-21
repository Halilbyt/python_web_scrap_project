import requests
from bs4 import BeautifulSoup as bs
import copy
import googletrans
from googletrans import Translator
from selenium import webdriver
import urllib.request
from urllib.request import Request
import time
import codecs

translator = Translator()

# myOptions = webdriver.ChromeOptions()

# prefs = {
#     "translate_whitelists":{"en":"hi"},
#     "translate":{"enabled":"true"}
# }

#myOptions.add_experimental_option("prefs",prefs)

driver = webdriver.Chrome()

url = "https://www.classcentral.com/"

driver.get(url)
time.sleep(1)

soup = bs(driver.page_source,"html.parser")


driver.close()


time.sleep(1)


translated_text = soup.find_all("p")[18]

# for tags in soup.find_all(text=True):
#      tags.replace_with(translator.translate(tags.text,dest="hi").text)

# with open("index_translated.html","w",encoding="utf-8") as f:
#      f.write(str(soup))

print(len(soup.find_all("p")))
print(translated_text.find_all(text=True)[1])
print("**********************************")
print(translated_text.find_all(text=True))
for innerText in translated_text.find_all(text=True):
    if(innerText.text != '\n'):
        innerText.replace_with(translator.translate(innerText.text,dest="hi").text)
    else:
        pass

print(translated_text.find_all(text=True))
    

# for i in soup.find_all('p'):
#     print(i.text)

"""
if not re.match(r'<[^>]+>',str(t))
['\n', '12,437', ' lists created in the past 7 days\n            ']
"""
