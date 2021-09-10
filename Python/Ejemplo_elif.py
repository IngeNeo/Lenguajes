edad = int(input("Ingrese su edad:"))

if edad >= 1 and edad <= 10:
	print("A la edad de ", edad, " eres un infante")
elif edad >= 11 and edad <= 13:
	print("A la edad de ", edad, " eres un pre-adolecente")
elif edad >= 14 and edad <= 17:
	print("A la edad de ", edad, " eres un adolecente")
elif edad >= 18 and edad <= 30:
	print("A la edad de ", edad, " eres un adulto joven")
elif edad >= 31 and edad <= 60:
	print("A la edad de ", edad, " eres un adulto mayor")
else:
	print("A la edad de ", edad, " eres un anciano")
