from selenium import webdriver
from selenium.webdriver.common.by import By # Used for locating elements
from selenium.webdriver.common.keys import Keys # Used for keyboard action
import json

driver = webdriver.Chrome()

driver.get("https://banner.dartmouth.edu")

with open('webpage_cookies.json', 'r') as file:
    cookies = json.load(file)

for cookie in cookies:
    print(cookie)
    driver.add_cookie(cookie)

driver.get("https://banner.dartmouth.edu/banner/groucho/zp_web_add_drop.pz_timetable")

try:
    driver.switch_to.alert.dismiss()
except:
    pass

input("Press Enter to Close")
driver.quit()