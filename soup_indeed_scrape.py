from bs4 import BeautifulSoup
import urllib
import re
import pandas as pd
import requests
from urllib.request import urlopen

url = "https://www.indeed.com/m/jobs?q=data+scientist&l=Los+Angeles%2C+CA"
response = requests.get(url)

#page = urlopen(url)
page= response.text
soup = BeautifulSoup(page, 'lxml')

all_matches = soup.find_all('a', attrs={'rel':['nofollow']})
for i in all_matches:
    print (i['href'])
    print (type(i['href']))
    print ("https://www.indeed.com/m/"+i['href'])

title = []
company = []
location = []
jd = []
i=0
sum_py=0
for each in all_matches:
    jd_url= 'http://www.indeed.com/m/'+each['href']
    #jd_page = urlopen(jd_url)
    response = requests.get(jd_url)
    jd_page= response.text
    jd_soup = BeautifulSoup(jd_page, 'lxml')
    jd_desc = jd_soup.findAll('div',attrs={'id':['desc']}) ## find the structure like: <div id="desc"></>
#    break
    title.append(jd_soup.body.p.b.font.text)
    company.append(jd_desc[0].span.text)
    location.append(jd_soup.body.p.span.text)
    jd.append(jd_desc[0].text)
    python = re.findall(r'[Pp]ython', str(jd_desc))
    print("Python references = " , len(python))
    sum_py += len(python)
print(sum_py)
