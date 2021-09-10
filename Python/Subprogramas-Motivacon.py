n = int(input("Entre valor de n "))
r = int(input("Entre valor de r "))

fn = 1								#   fn es la variable donde se almacenará el factorial de n

for i   in   range(1, n + 1):		#   instrucciones para calcular el factorial de n
	fn = fn * i

fr = 1								#   fr es la variable donde se almacenará el factorial de n

for i   in   range(1, r + 1):		#   instrucciones para calcular el factorial de r
	fr = fr * i

fnr = 1								#    fnr es la variable donde se almacenará el factorial de n – r

for i   in   range(1, n - r + 1):	#   Instrucciones para calcular el factorial de n – r
	fnr = fnr * i

nc = fn // fr // fnr

print("n =", n, "  r =", r, "  Factorial de n =", fn, " Factorial de r =", fr ,"Factorial de n − r =", fnr,"  Número de combinaciones =", nc)