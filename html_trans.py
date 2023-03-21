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

"""
Note:
"The translate.googleapis.com site use is very limited.
It only allows about 100 requests per one hour period and there after returns a 429 error (Too many requests). 
On the other hand, the Google Translate Api has a default billable limit of 5 requests/second/user and 200,000 requests/day."
"""

# test result:
#print(result)

# Method - 1 Using BeautifulSoup for web screping:

url = "https://www.classcentral.com/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}

response = requests.get(url,headers=headers)
time.sleep(5)
html_content = response.content

soup = BeautifulSoup(html_content,"html.parser")

# Method - 2 Using Selenium:
driver = webdriver.Chrome("C:/Users/D4rkS/Desktop/chromedriver_win32/chromedriver.exe")
time.sleep(1)
driver.get("https://www.classcentral.com/")
time.sleep(5)
with codecs.open("selen_index.html","w","utf-8") as f:
    f.write(driver.page_source)
soup_2 = BeautifulSoup(driver.page_source,"html.parser")


# Method - 3 Using Urllib:
def copy_page(url):
    req = Request(url,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"})
    res = urllib.request.urlopen(req)
    time.sleep(5)
    index_html = res.read()
    time.sleep(5)
    index_html = index_html.decode()
    time.sleep(5)

    return BeautifulSoup(index_html,"html.parser")


# list of all tags that contain any text
tags = ["section","div","header",'h2','h3',"aside","ul","li",'button','a','p','span','strong',"svg"]
tags_2 = ["h2","h3","p","a","span"]

"""
testing of tags
print("******************************************")
print("")
print(soup.find_all("p")[0].text)
"""

"""
testing of translating of text inside of the html tag
soup.find("title").string.replace_with(translator.translate(soup.find("title").text,src="en",dest="hi").text)
print(soup.find("title").text)
"""

# creating text-traslator function:
def html_text_translator(soup):
    #copying original content
    soup_copy = copy.copy(soup)
    #find and translate all texts via going through all tags
    for tag in tags:
        for content in soup_copy.find_all(tag):
            try :
                content.string.replace_with(translator.translate(content.text,dest="hi").text)
            except:
                pass
    #Translate page title                    
    soup_copy.find("title").string.replace_with(translator.translate(soup_copy.find("title").text,dest="hi").text)

    for tag in tags_2:
        for content in soup_copy.find_all(tag):
            try :
                content.string.replace_with(translator.translate(content.text,dest="hi").text)
            except:
                pass

    return soup_copy

soup_3 = copy_page(url)

translated_soup = html_text_translator(soup)
translated_soup_2 = html_text_translator(soup_2)
translated_soup_3 = html_text_translator(soup_3)

soup_list = [translated_soup,translated_soup_2,translated_soup_3]

for index,soup in enumerate(soup_list):
    with open(f"translated_index{index}.html","w",encoding="utf-8") as f:
        f.write(str(soup))





"""
    #after translated all page (accordingly to all tags) still there was a few tags that contain untranslated text. I finished them manually =>
    soup_copy.findAll("h2",{"class":"head-2 medium-up-head-1 row horz-align-center vert-align-middle text-center margin-bottom-xsmall"})[0].string.replace_with(translator.translate(soup_copy.findAll("h2",{"class":"head-2 medium-up-head-1 row horz-align-center vert-align-middle text-center margin-bottom-xsmall"})[0].text,dest="hi").text)
    soup_copy.findAll("h2",{"class":"head-2 medium-up-head-1 color-white margin-bottom-medium large-up-margin-bottom-xxlarge"})[0].string.replace_with(translator.translate(soup_copy.findAll("h2",{"class":"head-2 medium-up-head-1 color-white margin-bottom-medium large-up-margin-bottom-xxlarge"})[0].text,dest="hi").text)    
    soup_copy.findAll("p",{"class":"text-1 color-white relative padding-left-xlarge"})[0].string.replace_with(translator.translate(soup_copy.findAll("p",{"class":"text-1 color-white relative padding-left-xlarge"})[0].text,dest="hi").text)
    soup_copy.findAll("p",{"class":"text-1 color-white relative padding-left-xlarge"})[1].string.replace_with(translator.translate(soup_copy.findAll("p",{"class":"text-1 color-white relative padding-left-xlarge"})[1].text,dest="hi").text)
    soup_copy.findAll("p",{"class":"text-1 color-white relative padding-left-xlarge"})[2].string.replace_with(translator.translate(soup_copy.findAll("p",{"class":"text-1 color-white relative padding-left-xlarge"})[2].text,dest="hi").text)
    soup_copy.findAll("h2",{"class":"head-2 medium-up-head-1 margin-bottom-xsmall color-charcoal"})[0].string.replace_with(translator.translate(soup_copy.findAll("h2",{"class":"head-2 medium-up-head-1 margin-bottom-xsmall color-charcoal"})[0].text,dest="hi").text)
    soup_copy.findAll("h3",{"class":"text-2 weight-semi upper padding-bottom-xxsmall border-bottom border-gray margin-bottom-medium"})[0].string.replace_with(translator.translate(soup_copy.findAll("h3",{"class":"text-2 weight-semi upper padding-bottom-xxsmall border-bottom border-gray margin-bottom-medium"})[0].text,dest="hi").text)     
    soup_copy.findAll("p",{"head-2 weight-semi color-white margin-bottom-xxlarge relative padding-left-xlarge"})[0].string.replace_with(translator.translate(soup_copy.findAll("p",{"class":"head-2 weight-semi color-white margin-bottom-xxlarge relative padding-left-xlarge"})[0].text,dest="hi").text)                 
    soup_copy.findAll("h2",{"class":"head-2 medium-up-head-1 margin-bottom-xsmall color-charcoal"})[1].string.replace_with(translator.translate(soup_copy.findAll("h2",{"class":"head-2 medium-up-head-1 margin-bottom-xsmall color-charcoal"})[1].text,dest="hi").text)
    soup_copy.findAll("span",{"class":"text-1 weight-semi icon-chevron-right-charcoal icon-right-small color-charcoal"})[0].string.replace_with(translator.translate(soup_copy.findAll("p",{"class":"text-1 weight-semi icon-chevron-right-charcoal icon-right-small color-charcoal"})[0].text,dest="hi").text)
"""