# DjangoLoL
Gestio d'una competicio de League of Legends

	User:admin
	Pass:1234

#Models Creats:
 	TOTS
	(Almenys atributs basics)
	#RECORDATORI: Modificar foriegnkey de jugador a equip (es User a de ser Equip)

#HTML:
	- INDEX
	- nou_usuari
	- base
	- equipform ("nou Equip")
	- ingresar ("login"),
	- noactivo("Error usuari bann"),
	- nousuario("usuari no registrat"),
	- privado ("Mi cuenta"),
	- teamokey("Equip creat")
  
#Views:
	- Index
	- NouUsuari
	- login
	- logout
	- nouEquip

#URLS:

	/register
	/login
	/privado
	/cerrar
	/teamregister
<<<<<<< HEAD
  
 




=======
	
#SPRINT ACTUAL:

	Generar horari (Fet: falta arreglar noms de lligues i jornades) (sabem que les partides duren 1h, oalmenys aixi ho vam definir amb la Oliva, aleshores, com ha maxim son 48 partides x jornada, ja q son 2 dies, i cada dia son 24h/24 partits. Cada partit té 2 equip. Les jornades dependran del nombre d'inscripcions)
	Recontar inscripcions(FET(Es mostren el numero i el llistat, pero nomes amb l'user, tot i aixi es pot deshabilitar) i vull mostrar el nombre d'activats pero es complicat)
	Enviar informació(FET)
	Registre equip(Faltaria arreglar que mires que no hi hagi cap jugador amb el mateix nom(de moment a la BD el nom no esta unique per a testejar millor))
	Comprobaciò usuaris(Funcio JSON)
	Generar documents XML(Com a la prac de SITW) (Correcte)

#Errors a corregir



(Solucionat)
Nomes mostre un formulari d'un jugador, hauria de mostrar el dels 5 i obligar a que es fiquin els 5.
Arreglar mostrar jugadors de l'equip dsde l'index.


#(Solucionat)
Al crear un jugador, no se com passar el equip, nomes li puc passar l'user. I per aixo esta cambiat al model la foreignkey d'equip.
El problema es que s'asigna a un user i no a un equip.


#( JA ESTAN ARREGLATS PERO SON PUNTS A REVISAR PER SI N'HI HA MES COM AQUETS )

Si l'usuari ja esta registrat el codi "peta", si es fa desde crear equip no.
Desde crear equip demana dos cops un nom, el nom del equip i el del user, HAURIA DE SER EL MATEIX

El usuari es crea quan es crea un equip pero el login amb aquest equip no funciona pq no agafa ve la password(Si es mira desdel admin es veu que no es correcta s'haura de mirar com ho fa el del registre d'user normal)
