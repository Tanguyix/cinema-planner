from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import inquirer


def getAvailableDays(driver):
  driver.get("https://www.ugc.fr/cinema.html?id=10")

def getDayName(dayElem):
  return dayElem.get_attribute("innerHTML").strip()

def pickDay(driver):
  days = getAvailableDays(driver);
  try:
    days = driver.find_elements(By.CSS_SELECTOR, "[id^=nav_date_] span")
    q = [inquirer.List("day", "Quel jour souhaites-tu aller au cinéma ?", choices = list(map(getDayName, days)))]
    chosenDay = inquirer.prompt(q)
  except NoSuchElementException:
    print("error")
    pass