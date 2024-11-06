from random import choice, randint, seed
class Persona():
	def __init__(self, edad, sexo):
		self.edad = edad
		self.sexo = sexo

def generar_muestra_aleatoria(cantidad, random_seed = 123):
	seed(random_seed)
	personas = []
	for i in range(cantidad):
		personas.append(Persona(randint(0,100),choice(["M","F"])))
	return personas

def introducir_lista(n):
	personas = []
	for i in range(n):
		sexo = ""
		while sexo != "M" and sexo != "F":
			sexo = input(f"Introduzca el sexo de la persona {i+1} (M/F): ").upper()
		edad = -1
		while edad < 0:
			try:
				edad = int(input(f"Introduzca la edad de la persona {i+1}: "))
			except:
				print("Introduzca una edad válida.")
		personas.append(Persona(edad,sexo))
	return personas

def mostrar_resultados(personas):
	numero_total = len(personas)
	mayores_18 = 0
	masculinas_mayores_18 = 0
	femeninas_menores_18 = 0
	mujeres = 0
	for persona in personas:
		sexo = persona.sexo
		edad = persona.edad
		if sexo == "F":
			mujeres+=1
			if edad < 18:
				femeninas_menores_18+=1
			else:
				mayores_18+=1
		else:
			if edad >= 18:
				masculinas_mayores_18+=1
				mayores_18 +=1
	print(f"Cantidad de personas mayores de edad: {mayores_18}")
	print(f"Cantidad de personas menores de edad: {numero_total - mayores_18}")
	print(f"Cantidad de personas masculinas mayores de edad: {masculinas_mayores_18}")
	print(f"Cantidad de personas femeninas menores de edad: {femeninas_menores_18}")
	print(f"Porcentaje que representan las personas mayores de edad respecto al total de personas: {mayores_18/numero_total*100} %")
	print(f"Porcentaje que representan las mujeres respecto al total de personas: {mujeres/numero_total*100} %")

if __name__ == "__main__":
	respuesta_1 = ""
	while respuesta_1 != "S" and respuesta_1 != "N":
		respuesta_1 = input("Introduzca S si desea introducir manualmente la lista y N si desea generarla aleatoriamente: ")

	numero_muestra = 0
	while numero_muestra <= 0:
		try:
			numero_muestra = int(input("Introduzca el número de personas que desea introducir o generar: "))
		except:
			print("Introduzca un número válido")

	if respuesta_1 == "S":
		personas = introducir_lista(numero_muestra)
	else:
		semilla = input("Introduzca una semilla aleatoria (enteros positivos): ")
		if semilla.isdigit():
			personas = generar_muestra_aleatoria(numero_muestra, int(semilla))
		else:
			personas = generar_muestra_aleatoria(numero_muestra)
	mostrar_resultados(personas)

