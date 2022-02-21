from time_helper import *

def removeUnavailableHoursForOneType(movies, availableHours):
  for movie in movies:
    movie["movieTimes"] = [movieTime for movieTime in movie["movieTimes"] if isAfter(movieTime["startTime"], availableHours["startHour"]) and isBefore(movieTime["endTime"], availableHours["endHour"])]
  return movies

def removeUnavailableHours(movies, availableHours):
  availableHoursWithSomeMargin = {
    "startHour": removeMinutes(int(availableHours["startHour"][0:2]), int(availableHours["startHour"][3:5]), 10),
    "endHour": addMinutes(int(availableHours["endHour"][0:2]), int(availableHours["endHour"][3:5]), 10)
  }
  cleanMustWatch = removeUnavailableHoursForOneType(movies['mustWatchAnswer'], availableHoursWithSomeMargin)
  cleanMayWatch = removeUnavailableHoursForOneType(movies['mayWatchAnswer'], availableHoursWithSomeMargin)
  return {
    "mustWatchAnswers": cleanMustWatch,
    "mayWatchAnswers": cleanMayWatch
  }

def planDay(movies, availableHours):
  plan = []
  maxMustWatch = 0
  maxShouldWatch = 0
  maxBreakTime = 0
  moviesInAvailableHours = removeUnavailableHours(movies, availableHours)
  # Remove unavailable hours for all movies (ie run through all movie times in both must and may_watch, if (start before available StartHour or end after available endHour, remove it, with a few minutes margin))
  # Loop through all movies, then all available hours, test every case, pass if collision, if mustWatch > previousMax, ou == et mayWatch > max ou == et breakTime > maxBreak, nouveau plan, sinon do nothing
  return plan
