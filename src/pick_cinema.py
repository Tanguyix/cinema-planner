import inquirer

parisCinemaTuples = [
  ("UGC Les Halles", {"id":"10", "name": "UGC Les Halles"}),
  ("UGC Grand Normandie", {"id": "53", "name": "UGC Grand Normandie"}),
  ("UGC Normandie", {"id": "2", "name": "UGC Normandie"}),
  ("UGC Maillot", {"id": "7", "name": "UGC Maillot"}),
  ("UGC Montparnasse", {"id": "14", "name": "UGC Montparnasse"}),
  ("UGC Rotonde", {"id": "15", "name": "UGC Rotonde"}),
  ("UGC Odéon", {"id": "13", "name": "UGC Odéon"}),
  ("UGC Danton", {"id": "4", "name": "UGC Danton"}),
  ("UGC Ciné Cité Bercy", {"id": "12", "name": "UGC Ciné Cité Bercy"}),
  ("UGC Lyon Bastille", {"id": "11", "name": "UGC Lyon Bastille"}),
  ("UGC Gobelins", {"id": "5", "name": "UGC Gobelins"}),
  ("UGC Opéra", {"id": "9", "name": "UGC Opéra"}),
  ("UGC Ciné Cité Paris 19", {"id": "37", "name": "UGC Ciné Cité Paris 19"}),
]

suburbsCinemaTuples = [
  ("UGC Ciné Cité La Défense", {"id": "20", "name": "UGC Ciné Cité La Défense"}),
  ("Le Cin'hoche Sartrouville", {"id": "49", "name": "Le Cin'hoche Sartroutrou"}),
]

def pickCinema():
  cityQuestion = [
    inquirer.List("city_tuple_list", "Dans quelle ville souhaites-tu aller au cinéma ?", choices = [("Paris", parisCinemaTuples), ("Région Parisienne", suburbsCinemaTuples)])
  ]
  city = inquirer.prompt(cityQuestion)
  theatreQuestion = [
    inquirer.List("cinema", "Dans quel cinéma souhaites-tu te rendre ?", choices = city["city_tuple_list"])
  ]
  return inquirer.prompt(theatreQuestion)["cinema"]
