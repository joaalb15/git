def pedir_numero(prompt):
	while True:
		try:
			return float(input(prompt))
		except ValueError:
			print("Entrada no válida. Por favor introduce un número.")


def main():
	print("Introduce dos números para sumarlos")
	a = pedir_numero("Número 1: ")
	b = pedir_numero("Número 2: ")
	s = a + b
	if s.is_integer():
		s = int(s)
	print(f"Resultado: {s}")


if __name__ == '__main__':
	main()

