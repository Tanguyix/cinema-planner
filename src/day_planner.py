from time_helper import removeMinutes, addMinutes

def removeUnuvailableHours(movies, availableHours):
  availableHoursWithSomeMargin = {
    "startHour": removeMinutes(int(availableHours["startHour"][0:2]), int(availableHours["startHour"][3:5]), 10),
    "endHour": addMinutes(int(availableHours["endHour"][0:2]), int(availableHours["endHour"][3:5]), 10)
  }
  print(availableHoursWithSomeMargin)

def planDay(movies, availableHours):
  plan = []
  maxMustWatch = 0
  maxShouldWatch = 0
  maxBreakTime = 0
  moviesInAvailableHours = removeUnuvailableHours(movies, availableHours)
  print("available Hours = ", availableHours, "movies = ", movies)
  # Remove unavailable hours for all movies (ie run through all movie times in both must and may_watch, if (start before available StartHour or end after available endHour, remove it, with a few minutes margin))
  # Loop through all movies, then all available hours, test every case, pass if collision, if mustWatch > previousMax, ou == et mayWatch > max ou == et breakTime > maxBreak, nouveau plan, sinon do nothing
  return plan
