def removeMinutes(hours, minutes, minutesToRemove):
  if (minutesToRemove > 60):
    raise Exception("should not try to remove more than 60 minutes") 
  if (minutesToRemove < minutes):
    return ("0" + str(hours) + ":" + ("0" + str(minutes - minutesToRemove))[-2:])[-5:]
  if (hours - 1 > 0):
    return ("0" + str(hours - 1) + ":" + ("0" + str(60 + minutes - minutesToRemove))[-2:])[-5:]
  return "23:" + str(60 + minutes - minutesToRemove)

def addMinutes(hours, minutes, minutesToAdd):
  if (minutesToAdd > 60):
    raise Exception("should not try to add more than 60 minutes") 
  if (minutesToAdd + minutes < 60):
    return ("0" + str(hours) + ":" + ("0" + str(minutes + minutesToAdd))[-2:])[-5:]
  if (hours + 1 < 24):
    return ("0" + str(hours + 1) + ":" + ("0" + str(minutes + minutesToAdd - 60))[-2:])[-5:]
  return "00:" + str(minutes + minutesToAdd - 60)

def isAfter(firstTime, secondTime):
  firstHour = int(firstTime[0:2])
  firstMinutes = int(firstTime[3:5])
  secondHour = int(secondTime[0:2])
  secondMinutes = int(secondTime[3:5])
  if (firstHour == 0 and secondHour > 0):
    return True
  if (secondHour == 0 and firstHour > 0):
    return False
  return (firstHour > secondHour or (firstHour == secondHour and firstMinutes >= secondMinutes))

def isBefore(firstTime, secondTime):
  return isAfter(secondTime, firstTime)

def areTwoMoviesSimultanous(movie1, movie2):
  movie1EndTimeWithExtra = addMinutes(int(movie1["movieTime"]["endTime"][0:2]), int(movie1["movieTime"]["endTime"][3:5]), 15)
  return ((isBefore(movie1["movieTime"]["startTime"], movie2["movieTime"]["startTime"]) and
        isAfter(movie1EndTimeWithExtra, movie2["movieTime"]["startTime"])) or
        (isAfter(movie1["movieTime"]["startTime"], movie2["movieTime"]["startTime"]) and
        isBefore(movie1["movieTime"]["endTime"], movie2["movieTime"]["endTime"])))

def hasSimultanousMovies(plan):
  for i in range(len(plan) - 1) :
    for j in range(i + 1, len(plan)):
      if areTwoMoviesSimultanous(plan[i], plan[j]) or areTwoMoviesSimultanous(plan[j], plan[i]):
        return True
  return False

def diffTime(firstTime, secondTime):
  diffTime = (int(secondTime[0:2]) - int(firstTime[0:2])) * 60
  diffTime += int(secondTime[3:5]) - int(firstTime[3:5])
  return diffTime
