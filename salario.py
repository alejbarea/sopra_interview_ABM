def salario(horas_trabajadas,tarifa):
	return (horas_trabajadas>40)*(tarifa*(horas_trabajadas*1.5 - 20)) + (horas_trabajadas<=40)*tarifa*horas_trabajadas


if __name__ == "__main__":
	horas_trabajadas = -1
	tarifa = -1
	while horas_trabajadas < 0:
		try:
			horas_trabajadas = int(input("Introduzca las horas trabajadas: "))
		except:
			print("Introduzca un número válido.")
	while tarifa < 0:
		try:
			tarifa = float(input("¿A cuánto la hora? (en euros): "))
		except:
			print("Introduzca un número válido.")
	print(f"Su salario es de {salario(horas_trabajadas,tarifa)} euros.")