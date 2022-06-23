#!/usr/bin/which python3
# 1.news-extract-data.py
# extract information from a site using Xpath's chrome webdriver
# this will open a browser session on the URL and allow extraction

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
import os, sys
PROG = os.path.basename( sys.argv[0] )
PATH = os.path.expanduser('~/Downloads/chromedriver')  # introduce path here
OUT = 'headline.csv'
WEB = 'https://www.thesun.co.uk/sport/football/'

print('{}--> {}'.format(PROG,WEB),end='',flush=True)
# Creating the driver
driver_service = Service(executable_path=PATH)
driver = webdriver.Chrome(service=driver_service)
driver.get(WEB)

# Finding Elements
containers = driver.find_elements(by='xpath', value='//div[@class="teaser__copy-container"]')

titles = []
subtitles = []
links = []
for container in containers:
    title = container.find_element(by='xpath', value='./a/h2').text
    subtitle = container.find_element(by='xpath', value='./a/p').text
    link = container.find_element(by='xpath', value='./a').get_attribute('href')
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)
    print(".",end='',flush=True)

# Exporting data to a CSV file
my_dict = {'title': titles, 'subtitle': subtitles, 'link': links}
df_headlines = pd.DataFrame(my_dict)
df_headlines.to_csv(OUT)
print("{} {} entries".format(OUT,len(titles)))
driver.quit()
exit(0)
