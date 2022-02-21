def removeMinutes(hours, minutes, minutesToRemove):
  if (minutesToRemove > 60):
    raise Exception("should not try to remove more than 60 minutes") 
  if (minutesToRemove < minutes):
    return ("0" + str(hours) + ":" + str(minutes - minutesToRemove))[-5:]
  if (hours - 1 > 0):
    return ("0" + str(hours - 1) + ":" + str(60 + minutes - minutesToRemove))[-5:]
  return "23:" + str(60 + minutes - minutesToRemove)

def addMinutes(hours, minutes, minutesToAdd):
  if (minutesToAdd > 60):
    raise Exception("should not try to add more than 60 minutes") 
  if (minutesToAdd + minutes < 60):
    return ("0" + str(hours) + ":" + str(minutes + minutesToAdd))[-5:]
  if (hours + 1 < 24):
    return ("0" + str(hours + 1) + ":" + str(minutes + minutesToAdd - 60))[-5:]
  return "00:" + str(minutes + minutesToAdd - 60)

def isAfter(firstTime, secondTime):
  firstHour = int(firstTime[0:2])
  firstMinutes = int(firstTime[3:5])
  secondHour = int(secondTime[0:2])
  secondMinutes = int(secondTime[3:5])
  print("ft = ", firstTime, "st = ", secondTime, "isAfter = ", firstHour > secondHour or (firstHour == secondHour and firstMinutes > secondMinutes))
  return (firstHour > secondHour or (firstHour == secondHour and firstMinutes > secondMinutes))

def isBefore(firstTime, secondTime):
  return isAfter(secondTime, firstTime)