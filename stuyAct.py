from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files\chromedriver.exe"
driver = webdriver.Chrome(PATH)

import sys

stdoutOrigin=sys.stdout
sys.stdout = open("results.txt", "w")
driver.get("https://stuyactivities.org/catalog")
time.sleep(20)

allClubs = driver.find_elements(By.CLASS_NAME, "jss4")
print(len(allClubs))


for i in range (len(allClubs)):
    hyperlink = allClubs[i+1].get_attribute("href")
    driver2 = webdriver.Chrome(PATH)
    driver2.get(hyperlink + "/members")
    time.sleep(2)
    clubName = driver2.find_element_by_css_selector(".jss18")
    print("Club: " + clubName.text + "\nMembers are:")
    namesList = driver2.find_elements(By.CSS_SELECTOR, ".MuiTypography-body1")
    for x in range(len(namesList)-5):
        print(namesList[x+5].text)
    print("\n")
    driver2.close()

time.sleep(2)
driver.close()
sys.stdout.close()
sys.stdout=stdoutOrigin
