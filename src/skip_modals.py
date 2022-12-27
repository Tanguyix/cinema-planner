import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def skipModals(driver):
  try:
    driver.find_element(By.CSS_SELECTOR, "#didomi-notice-agree-button").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "#modal-nl-advertising-rgpd-close").click()
  except NoSuchElementException:
    pass