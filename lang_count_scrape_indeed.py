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
title_of_reviewer = []

#Append all company names to a list
for i in all_matches:
    review_url = 'http://www.indeed.com'+i['href']+'/reviews'
    print(review_url)
    for each in review_url:
        responses = requests.get(review_url)
        page = responses.text
        soup = BeautifulSoup(page, 'lxml')
        company = soup.find('div', {'itemprop':'name'}).text
        company_name.append(company)
        possible_titles = ['cmp-reviewer', 'cmp-reviewer-job-title']
        title = soup.find('span', {'class': possible_titles}).text
        title_of_reviewer.append(title)
        #date_of_review =
        print(title_of_reviewer)
        #print(company_name, title_of_reviewer)
        break

print(company_name[0])
#Title of the reviewer
# for j in all_matches:
#     review_url = 'http://www.indeed.com'+j['href']+'/reviews'
#     for each in review_url:
#         responses = requests.get(review_url)
#         page = responses.text
#         soup = BeautifulSoup(page, 'lxml')
#         title = soup.find('span', {'class':'cmp-reviewer'}).text
#         print(title)
#         #title_of_reviewer.append(title)
#         #print(title_of_reviewer)
#         break

reviews = {'name of company': company_name,
         'job title': title_of_reviewer}
df = pd.DataFrame.from_dict(reviews)
print(df)
