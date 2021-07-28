# Google Flights Scraper

A Python-based script that uses Selenium and Chromedriver to scrape flight prices for a specified destination and then email the scraped data to an intended email address.

## Description

This Google Flights Scraper searches for the cheapest 1-week, roundtrip flight deals from a specified airport in the upcoming 6 months from when the scraper is run. The user of the script will set a maximum price and only flights with a roundtrip price that is cheaper than that maximum will be emailed to the receiver. It is recommended that users of this script create a new Gmail account or use a non-primary account to send the emails from because allowing less secure apps to send emails through it could potentially make it easier for others to gain access to the account.

## Getting Started

### Installation

* The user must have Python 3 installed on the machine that the scraper is to be run from. See [this article](https://realpython.com/installing-python/) for help installing it.
* The user must have Selenium installed on the machine that the scraper is to be run from. See [this article](https://www.geeksforgeeks.org/how-to-install-selenium-in-python/) for help installing it.

### Setting up the Sender Email

In order for the script to send flight prices and dates via email, a Gmail account will be used.

* Create a new Google account.
* Find the **Manage your Google Account** button and navigate to the security settings.
* Turn the setting to **allow less secure apps** on. 
  * *Note: This makes it easier for others to gain access to your account so it is best to create a new Google account without any sensitive information on it.*

### Personalize the Scraper

* Near the top of the [flight_scraper.py](https://github.com/cameronmolen/flight-scraper/blob/main/flight_scraper.py) file are constant variables for:
  * DEPARTING_AIRPORT - The airport from which you want all of the scraped flights to depart from.
  * MAX_PRICE - The maximum price of the roundtrip flights that you would like scraped.
  * SENDER_EMAIL - The email that you set up in the above step.
  * PASSWORD - The password for the email that you set up in the above step.
  * RECEIVER_EMAIL - The email of the account you wish to send the scraped data to.

### Executing program

* To execute the program, execute the following command in terminal or command prompt:
```
python3 flight_scraper.py
```
* This script could easily be repeated weekly, daily, hourly, etc. by creating a cron job on the machine to be run. See [this article](http://researchhubs.com/post/computing/linux-cmd/cron-repeat-jobs.html) for more details about how to set up a scheduled cron job.
