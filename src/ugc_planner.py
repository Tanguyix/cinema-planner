from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.ugc.fr/cinema.html?id=10")

def parseMoviesInOneCinema():
  print("test")


parseMoviesInOneCinema();