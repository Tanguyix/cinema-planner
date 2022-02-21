def removeMinutes(hours, minutes, minutesToRemove):
  if (minutesToRemove > 60):
    raise Exception("should not try to remove more than 60 minutes") 
  if (minutesToRemove < minutes):
    return str(hours) + ":" + str(minutes - minutesToRemove)
  if (hours - 1 > 0):
    return str(hours - 1) + ":" + str(60 + minutes - minutesToRemove)
  return "23:" + str(60 + minutes - minutesToRemove)

def addMinutes(hours, minutes, minutesToAdd):
  if (minutesToAdd > 60):
    raise Exception("should not try to add more than 60 minutes") 
  if (minutesToAdd + minutes < 60):
    return str(hours) + ":" + str(minutes + minutesToAdd)
  if (hours + 1 < 24):
    return str(hours + 1) + ":" + str(minutes + minutesToAdd - 60)
  return "00:" + str(minutes + minutesToAdd - 60)
