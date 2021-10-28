from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://stuyactivities.org/catalog")

time.sleep(20);

main = driver.find_element_by_class_name("my-masonry-grid_column")

print(main.text)

time.sleep(2)

driver.quit()
