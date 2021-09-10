import misFunciones as mF

n = int(input("Entre valor de n "))
r = int(input("Entre valor de r "))

fn = mF.factorial(n)
fr = mF.factorial(r)
fnr = mF.factorial(n - r)

nc = fn // fr // fnr

print("n =", n, "  r =", r, "  Factorial de n =", fn, " Factorial de r =", fr, "  Factorial de n − r =", fnr,"  Número de combinaciones =", nc)