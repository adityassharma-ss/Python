import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait

# Setting up the connection

PROXY = " " # Add your proxy here

PATH = "D:\Python\chromedriver_win32" # Add your path to chromedriver here

options = webdriver.ChromeOptions()
options.add_argument('proxy.soax.com'.format(PROXY))
driver = webdriver.Chrome(service=Service(PATH), options = options)

# Connecting Instagram
driver.get("https://www.instagram.com/accounts/login/")

# Target Username

username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))

#Enter the fields

username.clear()
username.send_keys(" ") # Add your username here
password.clear()
password.send_keys(" ") # Add your password here

# Login

button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
button.click()

# Target Search

searchbox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
searchbox.clear()

keyword = " " # Add your target keyword here
searchbox.send_keys(keyword)

# Time delay

time.sleep(5)
searchbox.send_keys(Keys.ENTER)
time.sleep(5)
searchbox.send_keys(Keys.ENTER)

# Scroll down

driver.execute_script("window.scrollTo(0, 1000);")

# Target The images

target.sleep(5)
images = driver.find_elements_by_tag_name('img')
images = [image.get_attribute('src') for image in images]
images = images[:-2]

# number of images scrapped

print(f"Found {len(images)} images")
print('The images are:')
driver.get()









