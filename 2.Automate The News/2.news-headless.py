#!/usr/bin/which python3
# 2.news-headless.py
# extract information from a site using Xpath's chrome webdriver
# this will NOT open a browser but extract the pages from the URL anyway

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd
import os
import sys

WEB = 'https://www.thesun.co.uk/sport/football/'
PROG = os.path.basename(sys.argv[0])
DRIVER_PATH = os.path.expanduser('~/Downloads/chromedriver')  # introduce path here
OUT_FILE = 'headline.csv'

print('{}--> driver.get('.format(PROG), end='', flush=True)
# add headless mode
options = Options()
options.headless = True
driver_service = Service(executable_path=DRIVER_PATH)
driver = webdriver.Chrome(service=driver_service, options=options)
driver.get(WEB)

print('{} )'.format(WEB), end='', flush=True)
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
    print(".", end='', flush=True)

my_dict = {'title': titles, 'subtitle': subtitles, 'link': links}
df_headlines = pd.DataFrame(my_dict)
df_headlines.to_csv(OUT_FILE)
print(" {} [{} entries]".format(OUT_FILE, len(titles)))

driver.quit()
exit(0)
