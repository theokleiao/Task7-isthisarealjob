import time
from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import pdb
#create a csv file to store the scraped data
with open('data_db.csv','w') as file:
    file.write("JOBTITLE,LOCATION,DESCRIPTION \n")
driver = webdriver.Chrome('/Users/naeamakachalokwu/Documents/sscrape/chromedriver')
driver.get("https://ng.indeed.com/jobs?q=&l=Lagos")
#allow the page to load for 5seconds
driver.implicitly_wait(5)
#want to extract list of job roles
html = driver.page_source
# print(html)
soup = BeautifulSoup(html, 'html.parser') 
data = []
JOBTITLES = driver.find_elements_by_css_selector('.title')
for job_title in JOBTITLES:
    index = JOBTITLES.index(job_title)
    data.append([job_title.text])


DESCRIPTIONS = driver.find_elements_by_css_selector('.summary')
LOCATIONS = driver.find_elements_by_css_selector('div.sjcl .location')
for description in DESCRIPTIONS:
    index = DESCRIPTIONS.index(description)
    data[index].append(description.text)

for location in LOCATIONS:
    # pdb.set_trace()
    index = LOCATIONS.index(location)
    data[index].append(location.text)

for row in data:
    with open('data_db.csv','a') as file:
        file.write(','.join(row))

#with open('data_db.csv','w') as file: