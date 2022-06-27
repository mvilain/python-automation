#!/usr/bin/which python3
# 3.news-automation.py
# extract information from a site using Xpath's chrome webdriver
# this will NOT open a browser but extract the pages from the URL anyway
# name output file with date, so it can be run via cron regularly

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd
from datetime import datetime
import os
import sys

WEB = 'https://www.thesun.co.uk/sport/football/'
PROG = os.path.basename(sys.argv[0])
DRIVER_PATH = os.path.expanduser('~/Downloads/chromedriver')

OUT_FILE = 'football_headlines_{}.csv'.format(datetime.now().strftime("%Y%m%d"))
"""
# os.path.join ensures name is not OS dependent (e.g. directory seperator MacOS="/", Win="\")
# but I don't want the file stored where python is stored so commented out
"""
# OUT_FILE = os.path.join(os.path.dirname(sys.executable), OUT_FILE)

print('{}--> driver.web('.format(PROG), end='', flush=True)
# Headless mode
options = Options()
options.headless = True
driver_service = Service(executable_path=DRIVER_PATH)
driver = webdriver.Chrome(service=driver_service, options=options)
driver.get(WEB)

print('{}) '.format(WEB), end='', flush=True)
containers = driver.find_elements(by='xpath', value='//div[@class="teaser__copy-container"]')

titles = []
subtitles = []
links = []
link_count = 0
for container in containers:
    title = container.find_element(by='xpath', value='./a/h2').text
    subtitle = container.find_element(by='xpath', value='./a/p').text
    link = container.find_element(by='xpath', value='./a').get_attribute('href')
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)
    link_count += 1
    if (link_count % 5) == 0:  # print "+" when count mod 5 = 0
        print(".", end='', flush=True)

# Exporting data to the same folder where the executable will be located
my_dict = {'title': titles, 'subtitle': subtitles, 'link': links}
df_headlines = pd.DataFrame(my_dict)
df_headlines.to_csv(OUT_FILE)
print(" {} [{} entries]".format(OUT_FILE, len(titles)))

driver.quit()
