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

def sleep_until_datetime(target_datetime):
    """Pauses the script until a specific datetime is reached."""
    now = datetime.now()
    # Calculate the time difference in seconds
    time_difference = (target_datetime - now).total_seconds()
    
    if time_difference > 0:
        print(f"Sleeping for {time_difference} seconds until {target_datetime}")
        time.sleep(time_difference)
    else:
        print("Target time is in the past, continuing immediately.")

BASE_DIR = Path(__file__).resolve().parent.parent
envPath = BASE_DIR/'.env'

driver = webdriver.Chrome()
load_dotenv(envPath)
username = os.getenv("CAS_USERNAME")
password = os.getenv("CAS_PASSWORD")

driver.get("https://bannersso.dartmouth.edu/ssomanager/saml/login?relayState=/c/auth/SSB?pkg=twbkwssb.set_origin?launch_page=zp_web_add_drop.pz_timetable")

CASuserInput = driver.find_element(By.ID, 'username')
print(CASuserInput)
print('--------------')
CASpasswordInput = driver.find_element(By.ID, 'password')
print(CASpasswordInput)
print('--------------|--------------')

CASuserInput.clear()
CASpasswordInput.clear()

CASuserInput.send_keys(username)
CASpasswordInput.send_keys(password)

CASbutton = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "submitBtn"))
    )
CASbutton.click()

#----------------------------------------Past 2FA code, need to wait for user

"""
for testing purposes

removes he hidden attribute from the selection button if still before registration
"""
"""
print("start of wait")
disabled_element = WebDriverWait(driver, 600).until(
        EC.presence_of_element_located((By.NAME, "term"))
    )
print("end of wait")
driver.execute_script("arguments[0].removeAttribute('disabled');", disabled_element)
print("The 'disabled' attribute has been removed.")


print("start of wait")
disabled_element = WebDriverWait(driver, 600).until(
        EC.presence_of_element_located((By.NAME, "term"))
    )



removes he hidden attribute from the selection button if still before registration

for testing purposes
"""

sleep_until_datetime(datetime(2026,2,27,8,0,0,1))
driver.refresh()

"""
disabled_element = WebDriverWait(driver, 600).until(
        EC.presence_of_element_located((By.NAME, "term"))
    )

print("end of wait")
driver.execute_script("arguments[0].removeAttribute('disabled');", disabled_element)
print("The 'disabled' attribute has been removed.")
"""

TermSelectButton = WebDriverWait(driver, 600).until(
        EC.element_to_be_clickable((By.NAME, "term"))
    )


TermSelectButton.click()


TermSubmitButton = driver.find_element(By.XPATH, "//input[@type='submit' and @value='Select']")

TermSubmitButton.click()

#------------------------- CRN page

crn1 = WebDriverWait(driver, 600).until(
        EC.element_to_be_clickable((By.ID, "crn_id1"))
    )
crn2 = driver.find_element(By.ID, 'crn_id2')
crn3 = driver.find_element(By.ID, 'crn_id3')
crn1.send_keys("31693")
crn2.send_keys("30885")
crn3.send_keys("31786")


submitCRNbutton = TermSubmitButton = driver.find_element(By.XPATH, "//input[@type='submit' and @value='Submit Changes']")

submitCRNbutton.click()

input("Press Enter to Close")
driver.quit()