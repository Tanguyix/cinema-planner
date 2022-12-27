import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from clean_exit import cleanExit
from skip_modals import skipModals

def getCinemaList():
  driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
  driver.get("https://www.ugc.fr/cinemas.html")
  time.sleep(1)
  skipModals(driver)
  time.sleep(1)


  cinemaTuplesGroup = []
  navItems = driver.find_elements(By.CSS_SELECTOR, ".nav-item")
  for navItem in navItems:
    cinemaTuples = []
    cityName = navItem.find_element(By.TAG_NAME, "h2").get_attribute("innerHTML").strip().replace(" &amp; ", " & ")
    if cityName == 'Tous':
      continue
    driver.execute_script("arguments[0].click();", navItem)
    time.sleep(2)
    cinemaLinks = driver.find_elements(By.CSS_SELECTOR, ".block--title > a")
    for cinemaLink in cinemaLinks:
      cinemaName = cinemaLink.get_attribute("title")
      url = cinemaLink.get_attribute("href")
      if not url == 'javascript:void(0)' and not url == '':
        cinemaTuples.append({ 'url': url, 'name': cinemaName })
    cinemaTuplesGroup.append({ 'cityName': cityName, 'tuples': cinemaTuples})
    
  with open("cinemas.config", "w") as file:
    file.write(str(cinemaTuplesGroup))
