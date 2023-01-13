import os
import os.path as path

jugador = "Eleven"
vida = 100
armadura = 0

def crear_partida(jugador,vida,armadura):
	try:
		if (path.exists(f"{jugador}.txt")):
			print("El archivo ya existe")
		else:
			with open(f"{jugador}.txt", "w") as partida:
				partida.write("nombre: "+jugador+"\nvida: "+str(vida)+"\narmadura: "+str(armadura))
				print("Partida creada")
	except Exception as e:
		print("Hubo un error al crear el archivo de texto")

def cargar_partida(jugador):
	try:
		if (path.exists(f"{jugador}.txt")):
			with open(f"{jugador}.txt", "r") as partida:
				for texto in partida.readlines():
					if "nombre" in texto:
						nombre = texto
					if "vida" in texto:
						vida = texto
					if "armadura" in texto:
						armadura = texto
				return nombre, vida, armadura
	except Exception as e:
		print("Hubo un error al leer el archivo de texto")

crear_partida(jugador,vida,armadura)
#nombre, vida, armadura = cargar_partida(jugador)


