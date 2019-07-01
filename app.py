# Numero unite : Lieu
# Numéro d’automate : Machine du lieu
# Type d’automate : entier : fixe : 0X0000BA20 à de 0X0000BA2F

import random
import json
import time
from datetime import datetime

seconds = str(time.time()).replace('.', '')

now = datetime.now()
timestamp = str(datetime.timestamp(now)).replace('.', '')

# TODO Change vars
numUnite = 1 # between 1 and 5
numAutomate = 1 # between 1 and 10 
typeAutomate = '0X0000BA20' # between 0X0000BA20 and 0X0000BA2F -> Héxadécimal

tempCuve = round(random.uniform(2.5, 4), 1)
tempExt = round(random.uniform(8, 14), 1)
poidsLaitCuve = random.randint(3512, 4607)
# TODO rentre dynamique (diff entre les 2 derniere mesure poids lait cuve)
poidsProdFini = 1002
mesurePh = round(random.uniform(6.8, 7.2), 1)
mesureK = random.randint(35, 47)
concNaCl = round(random.uniform(1, 1.7), 1)
nivBacSal = random.randint(17, 37)
nivBacEcoli = random.randint(35, 49)
nivBacListeria = random.randint(28, 54)

print('Create json file')
json = json.dumps({'NumeroUnite': numUnite, 'NumeroAutomate': numAutomate, 'TypeAutomate': typeAutomate,
    'TemperatureCuve': tempCuve,'TemperatureExterieure': tempExt,'PoidsDuLaitEnCuve': poidsLaitCuve,'PoidsDuProduitFiniRealise': poidsProdFini, 'MesurePH': mesurePh, 'MesureK': mesureK,
    'concentrationDeNaCl': concNaCl, 'NiveauBacterienSalmonelle': nivBacSal, 'NiveauBacterienEcoli': nivBacEcoli, 'NiveauBacterienListeria': nivBacListeria, 'timestamp' : timestamp},
{'NumeroUnite': numUnite, 'NumeroAutomate': numAutomate, 'TypeAutomate': typeAutomate,
    'TemperatureCuve': tempCuve,'TemperatureExterieure': tempExt,'PoidsDuLaitEnCuve': poidsLaitCuve,'PoidsDuProduitFiniRealise': poidsProdFini, 'MesurePH': mesurePh, 'MesureK': mesureK,
    'concentrationDeNaCl': concNaCl, 'NiveauBacterienSalmonelle': nivBacSal, 'NiveauBacterienEcoli': nivBacEcoli, 'NiveauBacterienListeria': nivBacListeria, 'timestamp' : timestamp},
{'NumeroUnite': numUnite, 'NumeroAutomate': numAutomate, 'TypeAutomate': typeAutomate,
    'TemperatureCuve': tempCuve,'TemperatureExterieure': tempExt,'PoidsDuLaitEnCuve': poidsLaitCuve,'PoidsDuProduitFiniRealise': poidsProdFini, 'MesurePH': mesurePh, 'MesureK': mesureK,
    'concentrationDeNaCl': concNaCl, 'NiveauBacterienSalmonelle': nivBacSal, 'NiveauBacterienEcoli': nivBacEcoli, 'NiveauBacterienListeria': nivBacListeria, 'timestamp' : timestamp},
{'NumeroUnite': numUnite, 'NumeroAutomate': numAutomate, 'TypeAutomate': typeAutomate,
    'TemperatureCuve': tempCuve,'TemperatureExterieure': tempExt,'PoidsDuLaitEnCuve': poidsLaitCuve,'PoidsDuProduitFiniRealise': poidsProdFini, 'MesurePH': mesurePh, 'MesureK': mesureK,
    'concentrationDeNaCl': concNaCl, 'NiveauBacterienSalmonelle': nivBacSal, 'NiveauBacterienEcoli': nivBacEcoli, 'NiveauBacterienListeria': nivBacListeria, 'timestamp' : timestamp},
{'NumeroUnite': numUnite, 'NumeroAutomate': numAutomate, 'TypeAutomate': typeAutomate,
    'TemperatureCuve': tempCuve,'TemperatureExterieure': tempExt,'PoidsDuLaitEnCuve': poidsLaitCuve,'PoidsDuProduitFiniRealise': poidsProdFini, 'MesurePH': mesurePh, 'MesureK': mesureK,
    'concentrationDeNaCl': concNaCl, 'NiveauBacterienSalmonelle': nivBacSal, 'NiveauBacterienEcoli': nivBacEcoli, 'NiveauBacterienListeria': nivBacListeria, 'timestamp' : timestamp},	sort_keys=True, indent=4)

file = open('./json_file/' + typeAutomate + "_" + str(numUnite) + "_" + seconds + ".json", "w")
file.write(json)
file.close()
