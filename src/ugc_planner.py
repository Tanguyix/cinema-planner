from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

from day_getter import pickDay
from select_movies import pickMoviesToWatch
from pick_hours import pickHours
from pick_cinema import pickCinema
from day_planner import planDay
from plan_display import displayPlan

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def openMoviePage(theatreId):
  driver.get("https://www.ugc.fr/cinema.html?id=" + theatreId)
  driver.find_element(By.CSS_SELECTOR, "#didomi-notice-agree-button").click()
  time.sleep(1) # TODO: better handling of wait
  try:
    driver.find_element(By.CSS_SELECTOR, "#modal-nl-advertising-rgpd-close").click()
  except NoSuchElementException:
    pass

theatre = pickCinema()
openMoviePage(theatre["id"])
day = pickDay(driver)
availableHours = pickHours()
movies = pickMoviesToWatch(driver)
plan = planDay(movies, availableHours)
displayPlan(plan, day, theatre["name"])
