from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import inquirer
import time

def getDayName(dayElem):
  dayElemSpan = dayElem.find_element(By.CSS_SELECTOR, "span")
  return (dayElemSpan.get_attribute("innerHTML").strip(), dayElem)

def pickDay(driver):
  try:
    days = driver.find_elements(By.CSS_SELECTOR, "[id^=nav_date_]")
    q = [inquirer.List("day", "Quel jour souhaites-tu aller au cinéma ?", choices = list(map(getDayName, days)))]
    promptResult = inquirer.prompt(q)
    promptResult["day"].click() # scroll to element if not in screen
    time.sleep(1)
    # Properly handle loading
  except NoSuchElementException:
    print("error")
    pass