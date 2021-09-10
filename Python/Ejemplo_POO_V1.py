import random as r

class Fraccionario:
	denominador = None
	numerador = None

	def __init__(self, num, den):
		self.numerador = num
		self.denominador = den
	

	def convertir_en_decimal(self):
		if self.denominador == 0:
			return "No se puede dividir entre 0"
		else:
			return self.numerador / self.denominador

	def mostar_fraccion(self):
		print(self.numerador,"/", self.denominador)

	def crear_fraccion_aletoria(self):
		self.numerador = r.randint(0, 100)
		self.denominador = r.randint(0, 100)

# fin de la clase Fraccionario

n1 = float(input("Digite un numero: "))
n2 = float(input("Digite otro numero: "))

f1 = Fraccionario(n1, n2)
decimal = f1.convertir_en_decimal()

print("Parte decimal: ", decimal)

f1.mostar_fraccion()
f1.crear_fraccion_aletoria()
decimal = f1.convertir_en_decimal()

print("Parte decimal: ", decimal)
f1.mostar_fraccion()