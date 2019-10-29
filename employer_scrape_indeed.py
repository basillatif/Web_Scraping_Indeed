from bs4 import BeautifulSoup
import urllib
import re
import pandas as pd
import requests
from urllib.request import urlopen

url = 'https://www.indeed.com/cmp?q=data+scientist+&l=los+angeles&from=discovery'
response = requests.get(url)
#page = urlopen(url)
page= response.text
soup = BeautifulSoup(page, 'lxml')

all_matches = soup.find_all('a', {'class':['cmp-CompanyWidget-name']})
company_name = []

#Append all company names to a list
for i in all_matches:
    review_url = 'http://www.indeed.com'+i['href']+'/reviews'
    for each in review_url:
        responses = requests.get(review_url)
        page = responses.text
        soup = BeautifulSoup(page, 'lxml')
        company = soup.find('div', {'itemprop':'name'}).text
        company_name.append(company)
        print(company_name)
        break

#Title of the reviewer
