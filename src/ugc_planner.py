from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from day_getter import pickDay
from select_movies import pickMoviesToWatch

driver = webdriver.Chrome()

def openMoviePage():
  driver.get("https://www.ugc.fr/cinema.html?id=10")
  driver.find_element(By.CSS_SELECTOR, "#didomi-notice-agree-button").click()

openMoviePage();
day = pickDay(driver);
movies = pickMoviesToWatch(driver);