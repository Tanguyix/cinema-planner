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
  cleanMustWatch = removeUnavailableHoursForOneType(movies["mustWatchAnswer"], availableHoursWithSomeMargin)
  cleanMayWatch = removeUnavailableHoursForOneType(movies["mayWatchAnswer"], availableHoursWithSomeMargin)
  return {
    "mustWatchAnswer": cleanMustWatch,
    "mayWatchAnswer": cleanMayWatch
  }

def groupAllMovies(movies):
  for mustWatchMovie in movies["mustWatchAnswer"]:
    mustWatchMovie["mustWatch"] = True
  for mayWatchMovie in movies["mayWatchAnswer"]:
    mayWatchMovie["mustWatch"] = False
  return movies["mustWatchAnswer"] + movies["mayWatchAnswer"]


def duplicateList(list, nbDuplicates):
  ret = []
  for _ in range(0, nbDuplicates):
    ret.append(list.copy())
  return ret

def addMovieToPlan(plan, movie):
  newPlan = []
  for i in range(len(plan)):
    newPlan = newPlan + duplicateList(plan[i], len(movie["movieTimes"]))
  for j in range(len(newPlan)):
    newPlan[j].append({"title": movie["title"], "mustWatch": movie["mustWatch"], "movieTime": movie["movieTimes"][j % len(movie["movieTimes"])] })
  return newPlan

def createAllPlans(movies):
  # need to create plans without some movies
  plan = []
  for i in range(len(movies[0]["movieTimes"])):
    plan.append([{ "title": movies[0]["title"], "mustWatch": movies[0]["mustWatch"], "movieTime": movies[0]["movieTimes"][i]}])
  for j in range(1, len(movies)):
    plan = addMovieToPlan(plan, movies[j])
  return plan

def getBestPlan(plans):
  currentMustWatch = 0
  currentShouldWatch = 0
  # currentBreakTime = 0
  for plan in plans:
    if hasSimultanousMovies(plan):
      continue
  #   else:
  #     mw = countMustWatch(plan)
  #     sw = countShouldWatch(plan)
  #     if (mw > currentMustWatch or (mw == currentMustWatch and sw > currentShouldWatch)):
  #       res = plan
  # return plan
        
      

def planDay(movies, availableHours):
  moviesInAvailableHours = removeUnavailableHours(movies, availableHours)
  allMovies = groupAllMovies(moviesInAvailableHours)
  allPlans = createAllPlans(allMovies)
  plan = getBestPlan(allPlans)
  return plan