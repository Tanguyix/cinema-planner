from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import inquirer

def getMoviesInfo(movieBlock):
  try:
    movieTitleBlock = movieBlock.find_element(By.CSS_SELECTOR, ".block--title")
    movieTitle = movieTitleBlock.find_element(By.CSS_SELECTOR, "a")
  except NoSuchElementException:
    pass
  else:
    return(movieTitle.get_attribute("innerHTML").strip())
    # get better data as actual result and only return movie if it has openings on that day

def parseMoviesInLesHalles(driver):
  movieList = [];
  try:
    movieBlocks = driver.find_elements(By.CSS_SELECTOR, ".slider-item .row")
    for movieBlock in movieBlocks:
      movieInfo = getMoviesInfo(movieBlock)
      if movieInfo:
        movieList.append(getMoviesInfo(movieBlock));
  except NoSuchElementException:
    pass
  return movieList

def removePreviousPickedMovies(movieList, previousAnswers):
  return [movie for movie in movieList if movie not in previousAnswers]

def pickMoviesToWatch(driver):
  movieList = parseMoviesInLesHalles(driver)
  mustWatch = [
    inquirer.Checkbox(
      "must_watch",
      "Quel(s) film(s) souhaites-tu absolument voir ? (6 maximum)",
      choices = movieList,
      validate = lambda _, x: len(x) < 7
      ),
  ]
  mustWatchAnswer = inquirer.prompt(mustWatch)
  maxLen = 6 - len(mustWatchAnswer['must_watch'])
  if maxLen:
    may_watch = [
        inquirer.Checkbox(
        "may_watch",
        "Quel(s) film(s) souhaites-tu également voir ? (" + str(maxLen) + " maximum)",
        choices = removePreviousPickedMovies(movieList, mustWatchAnswer['must_watch']),
        validate = lambda _, x: len(x) < 6
        ),
    ]
    shouldWatchAnswer = inquirer.prompt(may_watch)
    return [mustWatchAnswer, shouldWatchAnswer]
  return [mustWatchAnswer, None]

