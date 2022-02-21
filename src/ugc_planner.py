from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

from day_getter import pickDay
from select_movies import pickMoviesToWatch
from pick_hours import pickHours
from pick_cinema import pickCinema
from day_planner import planDay

driver = webdriver.Chrome()

def openMoviePage(theatreId):
  driver.get("https://www.ugc.fr/cinema.html?id=" + theatreId)
  driver.find_element(By.CSS_SELECTOR, "#didomi-notice-agree-button").click()
  time.sleep(1)
  # try:
  driver.find_element(By.CSS_SELECTOR, "#modal-nl-advertising-rgpd-close").click()
  # except NoSuchElementException:
  #   pass

theatreId = pickCinema()
openMoviePage(theatreId)
pickDay(driver)
availableHours = pickHours()
movies = pickMoviesToWatch(driver)
plan = planDay(movies, availableHours)