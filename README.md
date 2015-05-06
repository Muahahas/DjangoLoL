# DjangoLoL
Gestio d'una competicio de League of Legends

User:admin
Pass:1234

#Models Creats:
  TOTS
  (Almenys atributs basics)

#HTML:
  INDEX, nouusuari, base, equipform ("nou Equip"), ingresar ("login"), noactivo("Error usuari bann"), nousuario("usuari no registrat"), privado ("Mi cuenta"), teamokey("Equip creat")
  
#Views:
  Index, NouUsuari, login, logout, nouEquip, 

#URLS:

	/register
	/login
	/privado
	/cerrar
	/teamregister
  
  
#Errors a corregir
Si l'usuari ja esta registrat el codi "peta", si es fa desde crear equip no.
Desde crear equip demana dos cops un nom, el nom del equip i el del user, HAURIA DE SER EL MATEIX

El usuari es crea quan es crea un equip pero el login amb aquest equip no funciona pq no agafa ve la password(Si es mira desdel admin es veu que no es correcta s'haura de mirar com ho fa el del registre d'user normal)