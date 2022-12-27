from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from open_movie_page import openMoviePage
from day_getter import pickDay
from select_movies import pickMoviesToWatch
from pick_hours import pickHours
from pick_cinema import pickCinema
from day_planner import planDay
from plan_display import displayPlan
from login import loginToUGCAccount
from movie_booking import bookMovies
from clean_exit import cleanExit

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

theatre = pickCinema()
openMoviePage(driver, theatre["id"])
day = pickDay(driver)
availableHours = pickHours()
movies = pickMoviesToWatch(driver)
plan = planDay(movies, availableHours)
displayPlan(plan, day, theatre["name"])
isLogged = loginToUGCAccount(driver)
if not isLogged:
  cleanExit(driver)
bookMovies(driver, plan, day, theatre["id"])
