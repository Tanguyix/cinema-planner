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

def hasSimultanousMovies(plan):
  for i in range(len(plan) - 1) :
    for j in range(1, len(plan)):
      if ((isAfter(addMinutes(int(plan[i]["movieTime"]["endTime"][0:2]), int(plan[i]["movieTime"]["endTime"][3:5]), 15), plan[j]["movieTime"]["startTime"]) and 
          isBefore(plan[i]["movieTime"]["startTime"], plan[j]["movieTime"]["startTime"])) or
          (isAfter(plan[j]["movieTime"]["endTime"], plan[i]["movieTime"]["startTime"]) and 
          isBefore(plan[j]["movieTime"]["startTime"], plan[i]["movieTime"]["startTime"])) or
          (isAfter(plan[i]["movieTime"]["startTime"], plan[j]["movieTime"]["startTime"]) and
          isBefore(plan[i]["movieTime"]["endTime"], plan[j]["movieTime"]["endTime"])) or
          (isAfter(plan[j]["movieTime"]["startTime"], plan[i]["movieTime"]["startTime"]) and
          isBefore(plan[j]["movieTime"]["endTime"], plan[i]["movieTime"]["endTime"]))):
        return True
  return False

