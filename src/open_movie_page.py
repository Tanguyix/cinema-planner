import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from skip_modals import skipModals

def openMoviePage(driver, theatreId):
  driver.get("https://www.ugc.fr/cinema.html?id=" + theatreId)
  time.sleep(1) # TODO: better handling of wait
  skipModals(driver)