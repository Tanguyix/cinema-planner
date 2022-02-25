import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def openMoviePage(driver, theatreId):
  driver.get("https://www.ugc.fr/cinema.html?id=" + theatreId)
  time.sleep(1) # TODO: better handling of wait
  try:
    driver.find_element(By.CSS_SELECTOR, "#didomi-notice-agree-button").click()
    driver.find_element(By.CSS_SELECTOR, "#modal-nl-advertising-rgpd-close").click()
  except NoSuchElementException:
    pass