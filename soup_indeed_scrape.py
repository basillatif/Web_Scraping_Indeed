from bs4 import BeautifulSoup
import urllib
import re
import pandas as pd
import requests
from urllib.request import urlopen

url = "https://www.indeed.com/m/jobs?q=%22data+scientist%22&l=Los+Angeles%2C+CA"
response = requests.get(url)

#page = urlopen(url)
page= response.text
soup = BeautifulSoup(page, 'lxml')

all_matches = soup.find_all('a', attrs={'rel':['nofollow']})

title = []
company = []
location = []
jd = []
i=0
sum_py=0
sum_c=0
sum_cplus=0
sum_java=0
sum_js=0
sum_r=0
sum_sql=0
sum_hadoop=0
sum_hive=0
sum_pig=0
sum_spark=0
sum_aws=0
sum_tab=0
for i in range(14):
    page = urlopen(url)
    soup = BeautifulSoup(page, 'lxml')
    all_matches = soup.findAll(attrs={'rel':['nofollow']})
    for each in all_matches:
        jd_url= 'http://www.indeed.com/m/'+each['href']
        #jd_page = urlopen(jd_url)
        response = requests.get(jd_url)
        jd_page= response.text
        jd_soup = BeautifulSoup(jd_page, 'lxml')
        jd_desc = jd_soup.findAll('div',attrs={'id':['desc']}) ## find the structure like: <div id="desc"></> #break
        title.append(jd_soup.body.p.b.font.text)
        company.append(jd_desc[0].span.text)
        location.append(jd_soup.body.p.span.text)
        jd.append(jd_desc[0].text)
        c_lang = re.findall(r'[\b\/\s]?C\b[\s\,]', str(jd_desc))
        c_plus = re.findall(r'[\b\/\s,]?C\+\+', str(jd_desc))
        java = re.findall(r'[Jj]ava\b[\s\,]', str(jd_desc))
        javascript = re.findall(r'Java[Ss]cript', str(jd_desc))
        python = re.findall(r'[\/\b]?[Pp]ython[\s\,\/]?', str(jd_desc))
        r_lang = re.findall(r'[\b\/\s]?R[\b\s\,]', str(jd_desc))
        sql = re.findall(r'SQL[\s,\/]?', str(jd_desc))
        hadoop = re.findall(r'Hadoop[\s,\/]?', str(jd_desc))
        hive = re.findall(r'Hive[\s,\/]?', str(jd_desc))
        pig = re.findall(r'Pig[\s,\/]?', str(jd_desc))
        spark = re.findall(r'Spark[\s,\/]?', str(jd_desc))
        aws = re.findall(r'AWS[\s,\/]?', str(jd_desc))
        tab = re.findall(r'Tableau[\s,\/]?', str(jd_desc))
        sum_c += len(c_lang)
        sum_cplus += len(c_plus)
        sum_java += len(java)
        sum_js += len(javascript)
        sum_r += len(r_lang)
        sum_py += len(python)
        sum_sql += len(sql)
        sum_hadoop += len(hadoop)
        sum_hive += len(hive)
        sum_pig += len(pig)
        sum_spark += len(spark)
        sum_aws += len(aws)
        sum_tab += len(tab)
        url_all = soup.findAll(attrs={'rel':['next']})
        url = 'http://www.indeed.com/m/'+ str(url_all[0]['href'])
        job = {'title': title,
         'company': company,
         'location': location,
         'Job Description': jd}
print("C: ", sum_c)
print("C++: ", sum_cplus)
print("Java: ", sum_java)
print("JavaScript: ", sum_js)
print("R: ", sum_r)
print("Python: ", sum_py)
print("SQL: ", sum_sql)
print("Hadoop: ", sum_hadoop)
print("Hive: ", sum_hive)
print("Pig: ", sum_pig)
print("Spark: ", sum_spark)
print("AWS: ", sum_aws)
print("Tableau", sum_tab)



#Print frequencies San Francisco, Los Angeles, New York, Boston, Chicago, Austin and DC.
