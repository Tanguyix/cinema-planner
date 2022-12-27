import inquirer
import ast

def pickCinema():
  with open("cinemas.config", "r") as file:
    cinemaTuples = ast.literal_eval(file.read())
    cityChoices = []
    for cinemaTuple in cinemaTuples:
      cityChoices.append((cinemaTuple["cityName"], cinemaTuple["tuples"]))
    cityQuestion = [
      inquirer.List("city_tuple_list", "Dans quelle ville souhaites-tu aller au cinéma ?", choices = cityChoices)
    ]
    city = inquirer.prompt(cityQuestion)
    cinemaChoices = []
    for cityTuple in city["city_tuple_list"]:
      cinemaChoices.append((cityTuple["name"], { "url": cityTuple["url"], "name": cityTuple["name"]}))
    theatreQuestion = [
      inquirer.List("cinema", "Dans quel cinéma souhaites-tu te rendre ?", choices = cinemaChoices)
    ]
  return inquirer.prompt(theatreQuestion)["cinema"]
