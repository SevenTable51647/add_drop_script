from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
from pathlib import Path
from datetime import datetime, timezone, timedelta
import time
import os

driver = webdriver.Chrome()

driver.get("https://bannersso.dartmouth.edu/ssomanager/saml/login?relayState=/c/auth/SSB?pkg=twbkwssb.set_origin?launch_page=zp_web_add_drop.pz_timetable")

CASbutton = WebDriverWait(driver, 600).until(
        EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "30942")
    )

for x in range(3000):
    time.sleep(2)
    crn1 = driver.find_element(By.ID, 'crn_id1')
    crn1.send_keys("31693")
    submitCRNbutton = driver.find_element(By.XPATH, "//input[@type='submit' and @value='Submit Changes']")
    submitCRNbutton.click()
