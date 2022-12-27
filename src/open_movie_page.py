import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
# from skip_modals import skipModals

def openMoviePage(driver, url):
  driver.get(url)
  time.sleep(1) # TODO: better handling of wait
  #TODO this PR : replace again with skipModals
  try:
    driver.find_element(By.CSS_SELECTOR, "#didomi-notice-agree-button").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "#modal-nl-advertising-rgpd-close").click()
  except NoSuchElementException:
    pass