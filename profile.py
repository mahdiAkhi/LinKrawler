from math import fabs
from operator import truediv
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
import csv
import time 

caps = DesiredCapabilities().EDGE
caps["pageLoadStrategy"] = "eager"
options = Options()
# options.headless = True

driver = webdriver.ChromiumEdge(capabilities=caps,options=options)

def splitNameAndLink(profile):
    link = profile.get_attribute('href').split('?')[0]
    name = profile.text.encode("utf-8")
    return (name , link)

cookies = {
    'name': 'li_at',
    'value':'***',
    'domain':"www.linkedin.com",
    'path':'/'
    }

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33',
    'Content-Type': 'text/html',
}

page = 1
url = "https://www.linkedin.com/search/results/people/?currentCompany=%5B%221035%22%5D&page="
print(url+str(page))
driver.get(url+str(page))
driver.add_cookie(cookies)
driver.get(url+str(page))
profileLink = list()
try:
    while(True):
        time.sleep(4)
        links = driver.find_elements(By.XPATH,"//span[contains(@class,'entity-result__title-text')]/a[contains(@class,'app-aware-link')]")
        print(splitNameAndLink(link) for link in links)
        profileLink = profileLink + [splitNameAndLink(link) for link in links]
        page = page+1
        driver.get(url+str(page))
except Exception as e:
    print(str(e),"page is:"+str(page))

# driver.close()
with open("microsoft-2.csv", "a+") as f:
    writer = csv.writer(f)
    writer.writerows(profileLink)