from selenium import webdriver
from lxml.html import fromstring
import requests
from itertools import cycle, islice
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from selenium.webdriver.common.proxy import Proxy, ProxyType

def get_configured_webdriver():
    ua = UserAgent()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
#    chrome_options.add_argument('--proxy-server={}'.format(proxy))
    chrome_options.add_argument('user-agent={}'.format(ua.random))
    chrome_options.add_argument('--no-sandbox') # required when running as root user. otherwise you would get no sandbox errors.
    driver = webdriver.Chrome(options=chrome_options,
          service_args=['--verbose', '--log-path=/tmp/chromedriver.log'])
    return driver

url = 'https://public-apps.apexclearing.com/session/#/login/'

driver = get_configured_webdriver()
print("trying to get url")
driver.get(url)
print(f"|{driver.title}|")

print(f"{driver.page_source}")


#with open("web.html", "w") as text_file:
#      text_file.write(content)

#web_content = None
##with open("cost.html", "r") as text_file:
#with open("web.html", "r") as text_file:
#      web_content = text_file.read()
#
##print(web_content)
#
#soup = BeautifulSoup(web_content, "html.parser")
#table = soup.findAll("table", {"class": "dividend-history"})
#print(table)
