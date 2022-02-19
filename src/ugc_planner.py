from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from day_getter import pickDay

driver = webdriver.Chrome()

def displayMovieInfos(movieBlock):
  try:
    movieTitleBlock = movieBlock.find_element(By.CSS_SELECTOR, ".block--title")
    movieTitle = movieTitleBlock.find_element(By.CSS_SELECTOR, "a")
  except NoSuchElementException:
    pass
  else:
    print(movieTitle.get_attribute("innerHTML"))

def parseMoviesInLesHallesToday():
  driver.get("https://www.ugc.fr/cinema.html?id=10")
  try:
    movieBlocks = driver.find_elements(By.CSS_SELECTOR, ".slider-item .row")
    for movieBlock in movieBlocks:
      displayMovieInfos(movieBlock);
  except NoSuchElementException:
    pass

day = pickDay(driver);
# parseMoviesInLesHallesToday();