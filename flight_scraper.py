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
    # Move to slider and change slider to desired price # FIXME
    slider = driver.find_element_by_xpath("/html/body/c-wiz[2]/div/div[2]/div/div/div/c-wiz/div[2]/div/div[1]/div[1]/section/div/div[1]/div[1]/div[1]/div[3]/div[2]/div/div/div/div/div[2]/div/div/div/div[4]")
    ActionChains(driver).move_to_element(slider).pause(1).click_and_hold(slider).move_by_offset(-50, 0).release().perform()
    sliderPriceElement = driver.find_element_by_xpath("/html/body/c-wiz[2]/div/div[2]/div/div[1]/div/c-wiz/div[2]/div/div[1]/div[1]/section/div/div[1]/div[1]/div[1]/div[3]/div[2]/div/div/div/div/div[2]/div/div/div/div[4]/div[4]/div")
    sliderValue = sliderPriceElement.text
#    while(sliderValue != MAX_PRICE):
#        ActionChains(driver).click_and_hold(slider).pause(1).move_by_offset(-30, 0).release().perform()
#        sliderPriceElement = driver.find_element_by_xpath("/html/body/c-wiz[2]/div/div[2]/div/div[1]/div/c-wiz/div[2]/div/div[1]/div[1]/section/div/div[1]/div[1]/div[1]/div[3]/div[2]/div/div/div/div/div[2]/div/div/div/div[4]/div[4]/div")
#        sliderValue = sliderPriceElement.text
    
    
    
finally:
    print("Completed.")

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
#driver.get("https://google.com")
#print(driver.page_source)
#driver.quit()
#-----------------------------------------------
