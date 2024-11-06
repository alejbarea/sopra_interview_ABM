def paridad(n):
	if n%2==0:
		print("Es par")
	else:
		print("Es impar")
	while n >= 0:
		print(n)
		n = n - 2


if __name__ == "__main__":
	numero = -1
	while numero < 0:
		try:
			numero = int(input("Introduzca el número: "))
		except:
			print("Introduzca un número válido: ")
	paridad(numero)