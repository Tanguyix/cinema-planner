import inquirer
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

def getLoginAnswer():
  return inquirer.confirm("Voulez-vous vous connecter à votre compte UGC pour réserver automatiquement vos billets (carte UGC illimité requise) ?", default = False)

def getLoginCredentials():
  print("Veuillez entrer vos informations de connection")
  q = [
    inquirer.Text("email", "Email"),
    inquirer.Password("password", echo="*", message="Mot de passe")
  ]
  return inquirer.prompt(q)

def logIn(driver, credentials):
  emailInput = driver.find_element(By.CSS_SELECTOR, "#mail")
  emailInput.clear()
  emailInput.send_keys(credentials["email"])
  passwordInput = driver.find_element(By.CSS_SELECTOR, "#password")
  passwordInput.clear()
  passwordInput.send_keys(credentials["password"])
  driver.find_element(By.CSS_SELECTOR, "#connectLink").click()
  time.sleep(1) # TODO: better handling of wait
  try:
    driver.find_element(By.CSS_SELECTOR, ".icon-deconnexion")
    return True
  except NoSuchElementException:
    return False

def openLoginPage(driver):
  driver.get("https://www.ugc.fr/login.html")

def loginToUGCAccount(driver):
  shouldLogIn = getLoginAnswer()
  if (not shouldLogIn):
    return False
  openLoginPage(driver)
  while True:
    credentials = getLoginCredentials()
    loggedIn = logIn(driver, credentials)
    if loggedIn:
      return True
    else:
      print("Erreur d'identification")
  