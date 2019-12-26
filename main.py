from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

import json


import requests
import time
import shadow_useragent
from itertools import cycle, islice
from bs4 import BeautifulSoup
from selenium.webdriver.common.proxy import Proxy, ProxyType

def get_configured_webdriver():
    ua = shadow_useragent.ShadowUserAgent()
    print(ua.random)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
#    chrome_options.add_argument('--proxy-server={}'.format(proxy))
    chrome_options.add_argument('user-agent={}'.format(ua.random))
    chrome_options.add_argument('--no-sandbox') # required when running as root user. otherwise you would get no sandbox errors.
    driver = webdriver.Chrome(options=chrome_options,
          service_args=['--verbose', '--log-path=/tmp/chromedriver.log'])
    return driver

def download_cost_basis_file(account, username, password):
    url = f"https://public-apps.apexclearing.com/accounts/#/{account}/cost_basis?skipSearch=true"
    driver = get_configured_webdriver()
    print("Using URL")
    print(url)
    print("Getting URL Title")
    driver.get(url)
    print(f"|{driver.title}|")

    print("Taking screenshot of login prompt...")
    driver.save_screenshot('login_prompt.png')
    element = driver.find_element_by_id("username")
    element.clear()
    element.send_keys(username)

    element = driver.find_element_by_id("password")
    element.clear()
    element.send_keys(password)

    print("Taking screenshot of login filled out...")
    driver.save_screenshot('login_prompt_filled.png')

    element.send_keys(Keys.RETURN)

    print("sleeping...")
    time.sleep(10)

    print("Taking screenshot of logged in...")
    driver.save_screenshot('logged.png')

    print("Clicking on the export csv button...")
    driver.find_element_by_xpath("//a[@class='btn btn-link ng-isolate-scope']").click()

def download_activity_file(account, username, password, start_date, end_date):
    url = f"https://public-apps.apexclearing.com/accounts/#/{account}/activity?startDate={start_date}&endDate={end_date}&skipSearch=true&activityType=TRADES&activityType=MONEY_MOVEMENTS&activityType=POSITION_ADJUSTMENTS"
    driver = get_configured_webdriver()
    print("Using URL")
    print(url)
    print("Getting URL Title")
    driver.get(url)
    print(f"|{driver.title}|")

    print("Taking screenshot of login prompt...")
    driver.save_screenshot('login_prompt.png')
    element = driver.find_element_by_id("username")
    element.clear()
    element.send_keys(username)

    element = driver.find_element_by_id("password")
    element.clear()
    element.send_keys(password)

    print("Taking screenshot of login filled out...")
    driver.save_screenshot('login_prompt_filled.png')

    element.send_keys(Keys.RETURN)

    print("sleeping...")
    time.sleep(10)

    print("Taking screenshot of logged in...")
    driver.save_screenshot('logged.png')

    print("Clicking on the export csv button...")
    driver.find_element_by_xpath("//export-ui-grid-csv[@class='ng-isolate-scope']//button[1]").click()

with open('cred.json') as json_file:
    cred = json.load(json_file)
    print(f"cred: {cred}")

download_activity_file(cred['apex_account'], cred['apex_username'] , cred['apex_password'], "2019-01-06", "2019-12-42")
#download_cost_basis_file(cred['apex_account'], cred['apex_username'] , cred['apex_password'])
time.sleep(10)

##element = driver.find_element_by_id("someUniqueId")
##element = driver.find_element_by_name("searchbox")
##element = driver.find_element_by_xpath("//input[@id='someUniqueId']")
#
#try:
#    elem = driver.find_element_by_name("qq")
#except NoSuchElementException:
##    raise Exception("Unable to find the element")
#    print("element not found")
