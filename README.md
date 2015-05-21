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
#SPRINT Actual>
Resolucio Reclamacio
Enviar resolucio al equip i marketing
obtenir equips espera (FET)
asignar IPs (FET)
publicar noticia

#Sprint Seguent
Top 25
Identificar jugador top

#Coses a reparar:
getStatus, pillar del shards i fer un urlopen a cada slug.

xml jerarquic





#SPRINT Anterior:

	Formulari reclamaciò
	Finalitzar una jornada.
	Obtenir resultats
	Crear clasificació
	Preparar nova jornada



	
#SPRINT Anterior:

	Generar horari (Fet)
	Recontar inscripcions(FET)
	Enviar informació(FET)
	Registre equip(Fet)
	Comprobaciò usuaris(Fet)
	Generar documents XML(Fet)

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
