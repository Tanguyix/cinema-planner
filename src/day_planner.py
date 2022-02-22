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
  if (not len(movie["movieTimes"])):
    return plan
  for i in range(len(plan)):
    newPlan = newPlan + duplicateList(plan[i], len(movie["movieTimes"]) + 1)
  for j in range(len(newPlan) - 1):
    newPlan[j].append({"title": movie["title"], "mustWatch": movie["mustWatch"], "movieTime": movie["movieTimes"][j % len(movie["movieTimes"])] })
  return newPlan

def createAllPlans(movies):
  plan = [[]]
  for i in range(len(movies[0]["movieTimes"])):
    plan.append([{ "title": movies[0]["title"], "mustWatch": movies[0]["mustWatch"], "movieTime": movies[0]["movieTimes"][i]}])
  for j in range(1, len(movies)):
    plan = addMovieToPlan(plan, movies[j])
  return plan

def countMustWatch(plan):
  return len([elem for elem in plan if elem["mustWatch"]])

def getHours(planElem):
  return planElem["movieTime"]["startTime"][0:2]

def sortPlan(plan):
  return plan.sort(key=getHours)

def getBreakTimes(plan):
  if (not plan or len(plan) <= 1):
    return 0
  totalBreakTime = 0
  for i in range(len(plan) - 1):
    totalBreakTime += diffTime(addMinutes(int(plan[i]["movieTime"]["endTime"][0:2]), int(plan[i]["movieTime"]["endTime"][3:5]), 15), plan[i + 1]["movieTime"]["beginTime"])
  return totalBreakTime

def getBestPlan(plans):
  currentMustWatch = 0
  currentMayWatch = 0
  currentBreakTime = 1440
  currentNonBreakTime = 0
  planWithSimul = 0
  for plan in plans:
    if hasSimultanousMovies(plan):
      planWithSimul += 1
      continue
    else:
      mustWatch = countMustWatch(plan)
      mayWatch = len(plan) - mustWatch
      orderedPlan = sortPlan(plan)
      breakTimes = getBreakTimes(orderedPlan)
      if (mustWatch > currentMustWatch or (mustWatch == currentMustWatch and mayWatch > currentMayWatch)):
        currentMustWatch = mustWatch
        currentMayWatch = mayWatch
        res = plan
  print(res)
  return res
        
      

def planDay(movies, availableHours):
  moviesInAvailableHours = removeUnavailableHours(movies, availableHours)
  allMovies = groupAllMovies(moviesInAvailableHours)
  allPlans = createAllPlans(allMovies)
  plan = getBestPlan(allPlans)
  return plan