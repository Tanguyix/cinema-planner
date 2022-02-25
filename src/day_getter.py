from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import inquirer
import time

from clean_exit import cleanExit

def getDayName(dayElem):
  dayElemSpan = dayElem.find_element(By.CSS_SELECTOR, "span")
  return (dayElemSpan.get_attribute("innerHTML").strip(), {"elem": dayElem, "name": dayElemSpan.get_attribute("innerHTML").strip()})

def pickDay(driver):
  try:
    days = driver.find_elements(By.CSS_SELECTOR, "[id^=nav_date_]")
    q = [inquirer.List("day", "Quel jour souhaites-tu aller au cinéma ?", choices = list(map(getDayName, days)))]
    promptResult = inquirer.prompt(q)
    driver.execute_script("let sts = [...document.getElementsByClassName('slick-track')]; sts.forEach((st) => {st.style.width = '100%';})")
    promptResult["day"]["elem"].click()
    time.sleep(1) # TODO: better handling of wait
    return promptResult["day"]["name"]
  except NoSuchElementException:
    print("Une erreur est survenue")
    cleanExit(driver)