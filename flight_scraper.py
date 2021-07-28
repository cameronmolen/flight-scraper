import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

# For headless driver
DRIVER_PATH = "/Volumes/WD Drive/Applications/Chromedriver/chromedriver"
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(options = options, executable_path = DRIVER_PATH)
driver.get("https://google.com/flights")

# For driver with GUI
#DRIVER_PATH = "/Volumes/WD Drive/Applications/Chromedriver/chromedriver"
#driver = webdriver.Chrome(executable_path = DRIVER_PATH)
#driver.get("https://www.google.com/flights")

DEPARTING_AIRPORT = "Salt Lake City"            # Enter departing airport here
MAX_PRICE = 400                                 # Enter max price here
SENDER_EMAIL = "@gmail.com"     # Enter sender email here
PASSWORD = "pass"                       # Insert password here
RECEIVER_EMAIL = "@gmail.com"       # Insert reciver email here
emailMessage = "Subject: Cheap Flights from " + DEPARTING_AIRPORT + "\n\n"

try:
    # Enter in departing airport
    try:
        whereFromInput = driver.find_element_by_xpath("//*[@id=\"i6\"]/div[1]/div/div/div[1]/div/div/input")
        whereFromInput.click()
        whereFromInput.send_keys(DEPARTING_AIRPORT)
        whereFromInput.send_keys(Keys.ENTER)
        time.sleep(1)
        airportSelector = driver.find_element_by_xpath("/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div/c-wiz/div[2]/div[1]/div[1]/div[2]/div[1]/div[6]/div[2]/div[6]/div/ul/li[1]/div[2]/div[1]/div")
        airportSelector.click()
    except:
        print("Error: Scraping done on incorrect location.")
    # Click search button
    searchButton = driver.find_element_by_xpath("//*[@id=\"yDmH0d\"]/c-wiz[2]/div/div[2]/div/c-wiz/div/c-wiz/div[2]/div[1]/div[2]/div/button")
    searchButton.click()
    # Click bags button and select 1 carry-on
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/c-wiz[2]/div/div[2]/div/div[1]/div/c-wiz/div[2]/div/div[1]/div[1]/div/div/div/div/div[2]/div[1]/div/div[5]")))
    bagsButton = driver.find_element_by_xpath("/html/body/c-wiz[2]/div/div[2]/div/div[1]/div/c-wiz/div[2]/div/div[1]/div[1]/div/div/div/div/div[2]/div[1]/div/div[5]")
    bagsButton.click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/c-wiz[2]/div/div[2]/div/div[1]/div/c-wiz/div[2]/div/div[1]/div[1]/div/div/div/div[2]/div[2]/div[1]/div[1]/section/div[2]/div/div[2]/div[2]/div/div/button[2]")))
    carryonButton = driver.find_element_by_xpath("/html/body/c-wiz[2]/div/div[2]/div/div[1]/div/c-wiz/div[2]/div/div[1]/div[1]/div/div/div/div[2]/div[2]/div[1]/div[1]/section/div[2]/div/div[2]/div[2]/div/div/button[2]")
    carryonButton.click()
    # Change calendar dates to flexible trip
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/c-wiz[2]/div/div[2]/div/div/div/c-wiz/div[2]/div/div[1]/div[1]/section/div/div[1]/div[1]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div/div[1]/div/div[1]/div/input"))).click()
    time.sleep(1)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/c-wiz[2]/div/div[2]/div/div/div/c-wiz/div[2]/div/div[1]/div[1]/section/div/div[1]/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/div/span/button[2]/span[2]"))).click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/c-wiz[2]/div/div[2]/div/div[1]/div/c-wiz/div[2]/div/div[1]/div[1]/section/div/div[1]/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[3]/div[1]/button"))).click()
    time.sleep(3)
    # Scrape all listings generated
    ticketList = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/c-wiz[2]/div/div[2]/div/div[1]/div/c-wiz/div[2]/div/div[1]/main/div/div[2]/ol")))
    for listing in ticketList.find_elements_by_xpath(".//li"):
        try:
            destination = listing.find_element_by_xpath(".//div/div[2]/div[1]/h3").text
            price = listing.find_element_by_xpath(".//div/div[2]/div[2]/div/span/span").text[1:]
            duration = listing.find_element_by_xpath(".//div/div[2]/div[1]/div[1]").text
            if int(price) <= MAX_PRICE:
                emailMessage += destination + " - $" + price + "\n" + duration + "\n\n"
        except:
            break
    # Add the current URL to the emailMessage
    emailMessage += driver.current_url
    
finally:

    #------------------------------------------Create and send email------------------------------------------#
    import smtplib, ssl
    
    port = 465
    context = ssl.create_default_context()
    
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(SENDER_EMAIL, PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, emailMessage.encode("utf-8"))
    #---------------------------------------------------------------------------------------------------------#
    
    driver.quit()
    print("Scraping completed. Email sent.")
