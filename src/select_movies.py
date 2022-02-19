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

def parseMoviesInLesHallesToday(driver):
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

def pickMoviesToWatch(driver):
  q = [
    inquirer.Checkbox(
      "must_watch",
      "Quel(s) film(s) souhaites-tu absolument voir ? (5 maximum)",
      choices = parseMoviesInLesHallesToday(driver),
      validate = lambda _, x: len(x) < 6
      ),
    inquirer.Checkbox("may_watch", "Quel(s) film(s) est-tu prêt à voir ?", choices = parseMoviesInLesHallesToday(driver)),
    # Remove already selected movies in first list
  ]
  promptResult = inquirer.prompt(q)
  return promptResult

