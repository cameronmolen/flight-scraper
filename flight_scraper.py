import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

DEPARTING_AIRPORT = "Salt Lake City"
MAX_PRICE = 400

DRIVER_PATH = "/Volumes/WD Drive/Applications/Chromedriver/chromedriver"
driver = webdriver.Chrome(executable_path = DRIVER_PATH)
driver.get("https://www.google.com/flights")

try:
    # Enter in departing airport
    time.sleep(1)
    whereFromInput = driver.find_element_by_xpath("//*[@id=\"i6\"]/div[1]/div/div/div[1]/div/div/input")
    whereFromInput.click()
    whereFromInput.send_keys(DEPARTING_AIRPORT)
    whereFromInput.send_keys(Keys.ENTER)
    time.sleep(1)
    airportSelector = driver.find_element_by_xpath("/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div/c-wiz/div[2]/div[1]/div[1]/div[2]/div[1]/div[6]/div[2]/div[6]/div/ul/li[1]/div[2]/div[1]/div")
    airportSelector.click()
    # Click search button
    searchButton = driver.find_element_by_xpath("//*[@id=\"yDmH0d\"]/c-wiz[2]/div/div[2]/div/c-wiz/div/c-wiz/div[2]/div[1]/div[2]/div/button")
    searchButton.click()
    # Click bags button and select 1 carry-on
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/c-wiz[2]/div/div[2]/div/div[1]/div/c-wiz/div[2]/div/div[1]/div[1]/div/div/div/div/div[2]/div[1]/div/div[5]")))
    bagsButton = driver.find_element_by_xpath("/html/body/c-wiz[2]/div/div[2]/div/div[1]/div/c-wiz/div[2]/div/div[1]/div[1]/div/div/div/div/div[2]/div[1]/div/div[5]")
    bagsButton.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/c-wiz[2]/div/div[2]/div/div[1]/div/c-wiz/div[2]/div/div[1]/div[1]/div/div/div/div[2]/div[2]/div[1]/div[1]/section/div[2]/div/div[2]/div[2]/div/div/button[2]")))
    carryonButton = driver.find_element_by_xpath("/html/body/c-wiz[2]/div/div[2]/div/div[1]/div/c-wiz/div[2]/div/div[1]/div[1]/div/div/div/div[2]/div[2]/div[1]/div[1]/section/div[2]/div/div[2]/div[2]/div/div/button[2]")
    carryonButton.click()
    # TODO: Instead of changing the slider, just scrape all listings and check the price on each one to decide whether or not to include it in DataFrame.
    
    
    
finally:
    print("Scraping completed.")

#-------For headless mode, use this code-------
#from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
#
#DRIVER_PATH = "/Volumes/WD Drive/Applications/Chromedriver/chromedriver"
#
#options = Options()
#options.headless = True
#options.add_argument("--window-size=1920,1200")
#
#driver = webdriver.Chrome(options = options, executable_path = DRIVER_PATH)
#driver.get("https://google.com/flights")
#print(driver.page_source)
#driver.quit()
#-----------------------------------------------
