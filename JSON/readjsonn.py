#!/usr/bin/python

import json

class jugador():
    nom=""
    email=""


juga= jugador()
json_file='jugadors.json'
jugadors= '0'

json_data=open(json_file)
data=json.load(json_data)
listjugadors= []
json_data.close()
for i in range(len(data["jugadors"])):
    juga.nom=data["jugadors"][i]["nom"]
    juga.email=data["jugadors"][i]["correu"]
    listjugadors.append(juga)
    juga= jugador()

for x in range(len(listjugadors)):
    print listjugadors[x].nom
    print listjugadors[x].email

jugador1= jugador()
jugador1.nom="James"
jugador1.email="Bond@gmail.com"

