def displayPlan(plan, day, cinema):
  print("Votre planning cinéma : ")
  print(day)
  print("Cinéma : ", cinema, "\n")
  for movie in plan:
    print(movie["title"], "de", movie["movieTime"]["startTime"], "à", movie["movieTime"]["endTime"])
