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
      driver.execute_script("arguments[0].click();", dayElem)

def openBookingPage(driver, movieTimeBlocks, movieStartTime):
  for movieTimeBlock in movieTimeBlocks:
    startTime = movieTimeBlock.find_element(By.CSS_SELECTOR, ".screening-start").get_attribute("innerHTML").strip()
    if (startTime == movieStartTime):
      movieTimeBlock.click()
      time.sleep(1)
      return
  print("hour for movie not found")
  cleanExit(driver)

def handleBookingForm(driver):
  driver.find_element(By.CLASS_NAME, "block--title").click()
  plusBtn = driver.find_elements(By.CLASS_NAME, "plus")[0]
  driver.execute_script("arguments[0].scrollIntoView(true);", plusBtn);
  driver.execute_script("arguments[0].click();", plusBtn)
  time.sleep(1)
  driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
  cgrAccept = driver.find_element(By.CSS_SELECTOR, "#cgr")
  driver.execute_script("arguments[0].click();", cgrAccept)
  validateBtn = driver.find_element(By.CSS_SELECTOR, ".btn.submit")
  ActionChains(driver).move_to_element(validateBtn).perform()
  driver.execute_script("arguments[0].click();", validateBtn)
  time.sleep(3)
  finalBtn = driver.find_element(By.CSS_SELECTOR, ".cta.submit")
  driver.execute_script("arguments[0].click();", finalBtn)
  time.sleep(3)


def bookMovie(driver, allMovies, movie):
  for existingMovie in allMovies:
    prevMovie = existingMovie[1]
    if (prevMovie["title"] == movie["title"]):
      openBookingPage(driver, prevMovie["movieTimeBlocks"], movie["movieTime"]["startTime"])
      time.sleep(1)
      handleBookingForm(driver)
      return
  print("Une erreur est survenue, le film" + movie["title"] + "et les suivants n'ont pas pu être réservés")
  cleanExit(driver)

def bookMovies(driver, plan, day, url):
  for movie in plan:
    openMoviePage(driver, url)
    openDay(driver, day)
    time.sleep(1)
    allMovies = parseMovies(driver)
    bookMovie(driver, allMovies, movie)
  print("Toutes les réservations ont été effectuées. Bonnes séances")
  cleanExit(driver)