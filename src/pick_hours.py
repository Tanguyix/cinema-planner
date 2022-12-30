import inquirer

hours = ['Ouverture', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00', '00:00']

def removePreviousHours(pickedHour):
  if (pickedHour == "Ouverture"):
    return hours[2:]
  cleanedHours = list(hour for hour in hours if hour != 'Ouverture' and (int(hour[0:2]) > int(pickedHour[0:2]) + 1 or int(hour[0:2]) < 2))
  cleanedHours.append("Fermeture")
  return cleanedHours

def pickHours():
  startHourQuestion = [
    inquirer.List("start_hour", "A partir de quelle heure souhaites-tu être au cinéma ?", choices = hours)
  ]
  startHour = inquirer.prompt(startHourQuestion)
  endHourQuestion = [
    inquirer.List("end_hour", "Jusqu'à quelle heure souhaites-tu être au cinéma ?", choices = removePreviousHours(startHour["start_hour"]))
  ]
  endHour = inquirer.prompt(endHourQuestion)
  if (startHour["start_hour"] == "Ouverture"):
     startHour["start_hour"] = "02:00"
  if (endHour["end_hour"] == "Fermeture"):
     endHour["end_hour"] = "00:30"
  return ({
    "startHour": startHour["start_hour"],
    "endHour": endHour["end_hour"]
  })
