import inquirer

parisCinemaTuples = [
  ("UGC Les Halles", "10"),
  ("UGC Grand Normandie", "53"),
  ("UGC Normandie", "2"),
  ("UGC Maillot", "7"),
  ("UGC Montparnasse", "14"),
  ("UGC Rotonde", "15"),
  ("UGC Odéon", "13"),
  ("UGC Danton", "4"),
  ("UGC Ciné Cité Bercy", "12"),
  ("UGC Lyon Bastille", "11"),
  ("UGC Gobelins", "5"),
  ("UGC Opéra", "9"),
  ("UGC Ciné Cité Paris 19", "37"),
]

suburbsCinemaTuples = [
  ("UGC Ciné Cité La Défense", "20"),
  ("Le Cin'hoche Sartrouville", "49"),
]

def pickCinema():
  cityQuestion = [
    inquirer.List("city_tuple_list", "Dans quelle ville souhaites-tu aller au cinéma ?", choices = [("Paris", parisCinemaTuples), ("Région Parisienne", suburbsCinemaTuples)])
  ]
  city = inquirer.prompt(cityQuestion)
  theatreQuestion = [
    inquirer.List("cinema_id", "Dans quel cinéma souhaites-tu te rendre ?", choices = city["city_tuple_list"])
  ]
  return inquirer.prompt(theatreQuestion)["cinema_id"]
  