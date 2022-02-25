import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from open_movie_page import openMoviePage
from select_movies import parseMovies
from clean_exit import cleanExit

def openDay(driver, day):
  driver.execute_script("let sts = [...document.getElementsByClassName('slick-track')]; sts.forEach((st) => {st.style.width = '100%';})")
  dayElems = driver.find_elements(By.CSS_SELECTOR, "[id^=nav_date_]")
  for dayElem in dayElems:
    dayElemSpan = dayElem.find_element(By.CSS_SELECTOR, "span")
    if (day == dayElemSpan.get_attribute("innerHTML").strip()):
      dayElem.click()

def openBookingPage(movieTimeBlocks, movieStartTime):
  for movieTimeBlock in movieTimeBlocks:
    startTime = movieTimeBlock.find_element(By.CSS_SELECTOR, ".screening-start").get_attribute("innerHTML").strip()
    if (startTime == movieStartTime):
      movieTimeBlock.click()
      time.sleep(1)
      return

def handleBookingForm(driver):
  driver.find_element(By.CSS_SELECTOR, ".icon-listederoulante-down").click()
  plusBtn = driver.find_elements(By.CSS_SELECTOR, ".plus")[0]
  ActionChains(driver).move_to_element(plusBtn).perform()
  time.sleep(1)
  plusBtn.click()
  time.sleep(1)
  driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
  # Give time to click on checkbox, should handle later. Probably just click on label actually
  time.sleep(5) 
  validateBtn = driver.find_element(By.CSS_SELECTOR, ".btn.submit")
  ActionChains(driver).move_to_element(validateBtn).perform()
  validateBtn.click()
  time.sleep(3)
  finalBtn = driver.find_element(By.CSS_SELECTOR, ".cta.submit")
  finalBtn.click()
  time.sleep(3)


def bookMovie(driver, allMovies, movie):
  for existingMovie in allMovies:
    prevMovie = existingMovie[1]
    if (prevMovie["title"] == movie["title"]):
      openBookingPage(prevMovie["movieTimeBlocks"], movie["movieTime"]["startTime"])
      time.sleep(1)
      handleBookingForm(driver)
      return
  print("Une erreur est survenue, le film" + movie["title"] + "et les suivants n'ont pas pu être réservés")
  cleanExit(driver)

def bookMovies(driver, plan, day, theatreId):
  for movie in plan:
    openMoviePage(driver, theatreId)
    openDay(driver, day)
    time.sleep(1)
    allMovies = parseMovies(driver)
    bookMovie(driver, allMovies, movie)
  print("Toutes les réservations ont été effectuées. Bonnes séances")
  cleanExit(driver)