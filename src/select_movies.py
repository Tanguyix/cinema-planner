import inquirer
import re
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from sens_critique import getInfoFromSensCritique

def getMovieTimes(movieTimeBlocks):
  timeBlocks = []
  for movieTimeBlock in movieTimeBlocks:
    startTime = movieTimeBlock.find_element(By.CSS_SELECTOR, ".screening-start").get_attribute("innerHTML").strip()
    endTime = movieTimeBlock.find_element(By.CSS_SELECTOR, ".screening-end").get_attribute("innerHTML").strip()
    cleanEndTime = re.search("[0-9]{1,2}:[0-9]{1,2}", endTime).group()
    timeBlocks.append({
      "startTime": startTime,
      "endTime": cleanEndTime,
    })
  return timeBlocks


def getMoviesInfo(movieBlock):
  try:
    movieTimeBlocks = movieBlock.find_elements(By.CSS_SELECTOR, ".component--screening-cards li")
    movieTimes = getMovieTimes(movieTimeBlocks)
    movieTitleBlock = movieBlock.find_element(By.CSS_SELECTOR, ".block--title")
    movieTitle = movieTitleBlock.find_element(By.CSS_SELECTOR, "a")
  except NoSuchElementException:
    pass
  else:
    if len(movieTimes):
      title = movieTitle.get_attribute("innerHTML").strip()
      return(movieTitle.get_attribute("innerHTML").strip(), {
        "movieTimes": movieTimes,
        "movieTimeBlocks": movieTimeBlocks,
        "title": title,
        "sc_info": getInfoFromSensCritique(title)
      })

def parseMovies(driver):
  movieList = []
  try:
    movieBlocks = driver.find_elements(By.CSS_SELECTOR, ".slider-item .row")
    for movieBlock in movieBlocks:
      movieInfo = getMoviesInfo(movieBlock)
      if movieInfo:
        movieList.append(movieInfo)
  except NoSuchElementException:
    pass
  return movieList

def removePreviousPickedMovies(movieList, previous):
  previousTitles = list(map(lambda x: x['title'] , previous))
  return [movie for movie in movieList if movie[1]['title'] not in previousTitles]

def pickMoviesToWatch(driver):
  movieList = parseMovies(driver)
  mustWatch = [
    inquirer.Checkbox(
      "must_watch",
      "Quel(s) film(s) souhaites-tu absolument voir ? (5 maximum)",
      choices = movieList,
      validate = lambda _, x: len(x) < 6
      ),
  ]
  mustWatchAnswer = inquirer.prompt(mustWatch)
  maxLen = 7 - len(mustWatchAnswer['must_watch'])
  may_watch = [
      inquirer.Checkbox(
      "may_watch",
      "Quel(s) film(s) souhaites-tu également voir ? (" + str(maxLen) + " maximum)",
      choices = removePreviousPickedMovies(movieList, mustWatchAnswer['must_watch']),
      validate = lambda _, x: len(x) < maxLen + 1
      ),
  ]
  mayWatchAnswer = inquirer.prompt(may_watch)
  return {"mustWatchAnswer": mustWatchAnswer["must_watch"], "mayWatchAnswer": mayWatchAnswer["may_watch"]}
