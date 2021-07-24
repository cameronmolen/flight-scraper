from selenium import webdriver

DRIVER_PATH = "/Volumes/WD Drive/Applications/Chromedriver/chromedriver"
driver = webdriver.Chrome(executable_path = DRIVER_PATH)
driver.get('https://google.com')

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
