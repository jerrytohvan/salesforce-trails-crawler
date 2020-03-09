import time
import sys
import json
import csv
from time import sleep
import os.path
from random import randint
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0
from selenium.common.exceptions import NoSuchElementException


#to use: python trailhead_scraper.py input_file output_file
#input file is the file with one column of links to trailhead links
#output file is the file to write scrapped data to
#both files are to be in csv type



if len(sys.argv) != 3:
    print()
    print("To use: python trailhead_scraper.py input_file output_file")
    print("input file is the file with links to trailhead links")
    print("output file is the file to write scrapped data to")
    print("both files are to be in csv type")
    sys.exit()


input_file = sys.argv[1]
output_file = sys.argv[2]

links = []

#get links from csv
with open(input_file, 'r') as file:
    for line in file:
        if len(line.strip()) > 0:
            links.append(line.strip())

#remove headers
links = links[1:]

driver = webdriver.Chrome('./chromedriver.exe')




#driver = webdriver.Chrome(executable_path="C:\path\to\chromedriver.exe")
driver.implicitly_wait(120)
driver.maximize_window()


all_names = []
all_total_badges = []
all_points = []
all_trails = []
all_titles = []


for link in links:
    

    driver.get(link)

    sleep(randint(2,3))
    #
    name = driver.find_element_by_xpath('//*[@id="lightning"]/div/div/div[2]/div/div[2]/div/div/div/div[1]/article/div/div[1]/div[2]/h1')

    total_badges = driver.find_element_by_xpath('//*[@id="lightning"]/div/div/div[2]/div/div[2]/div/div/div[2]/c-trailhead-rank/c-lwc-card/article/div/slot/div[2]/c-lwc-tally[1]/span/span[1]')

    # json_obj = json.loads(str(broth['data-react-props']))
    points = driver.find_element_by_xpath('//*[@id="lightning"]/div/div/div[2]/div/div[2]/div/div/div[2]/c-trailhead-rank/c-lwc-card/article/div/slot/div[2]/c-lwc-tally[2]/span/span[1]')


    trails = driver.find_element_by_xpath('//*[@id="lightning"]/div/div/div[2]/div/div[2]/div/div/div[2]/c-trailhead-rank/c-lwc-card/article/div/slot/div[2]/c-lwc-tally[3]/span/span[1]')


    #TRIGGER CLICK BUTTON
  #  if(check_exists_by_xpath(driver,'/html/body/div[1]/div/div/div[2]/div/div[2]/div/div/div[1]/c-lwc-trailhead-badges/c-lwc-card/article/footer/slot/c-lwc-card-footer-link/button')):
   #     print("link found")
     


    try:
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[2]/div/div/div[1]/c-lwc-trailhead-badges/c-lwc-card/article/footer/slot/c-lwc-card-footer-link/button').click()
        sleep(randint(2,3))
    except NoSuchElementException:
        print("not found.")
        
    #BADGES
    titles = []
    print("OK")


    contents = driver.find_elements_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[2]/div/div/div[1]/c-lwc-trailhead-badges/c-lwc-card/article/div/slot/div/c-lwc-trailhead-badge/div/figure/figcaption/a')
    for content in contents:
        titles.append(content.text)


    print(name.text)
    sleep(randint(2,3))

    all_names.append(name.text)
    all_points.append(points.text)
    all_total_badges.append(total_badges.text)
    all_trails.append(trails.text)
    all_titles.append(titles)

    print("Retrieval DONE!")


driver.quit()
print(all_names)
    
with (open(output_file, 'w', newline='')) as file:
    writer = csv.writer(file)
    writer.writerow(['link', 'name', 'badges', 'points', 'trails', 'badges_obtained'])

    for i in range(0,len(all_names)):
        to_write = [links[i], all_names[i], all_total_badges[i], all_points[i], all_trails[i], "|".join(all_titles[i])]
        writer.writerow(to_write)
