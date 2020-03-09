@ECHO OFF 
TITLE Salesforce Trailhead Crawler
ECHO Please wait... Updating Selenium
pip install selenium
PAUSE
python trailhead_scraper.py trailhead-url.txt results.csv
PAUSE
ECHO DONE!
