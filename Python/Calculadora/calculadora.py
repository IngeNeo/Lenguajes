import tkinter as Tk
from tkinter import *

def sumar():
	pass

def restar():
	pass

def multiplicar():
	pass

def dividir():
	pass

app = Tk()
app.title("Calculadora")

ventana = Frame(app)
ventana.grid(column=0, row=0,padx=(50,50), pady=(20,20))
ventana.columnconfigure(0, weight=1)
ventana.rowconfigure(0, weight=1)

numero1 = Label(ventana, text="Digite un numero")
numero1.grid(column=1, row=1, sticky=(W, E))

valor = ""
campo1 = Entry(ventana, width=10, textvariable=valor)
campo1.grid(column=2, row=1)

numero2 = Label(ventana, text="Digite otro numeros")
numero2.grid(column=3, row=1, sticky=(W, E))

valor2 = ""
campo2 = Entry(ventana, width=10, textvariable=valor2)
campo2.grid(column=4, row=1)

btn_sumar = Button(ventana, text="Sumar", command=sumar)
btn_sumar.grid(column=1, row=2)

btn_restar = Button(ventana, text="Restar", command=restar)
btn_restar.grid(column=2, row=2)

btn_multiplicar = Button(ventana, text="Multiplicar", command=multiplicar)
btn_multiplicar.grid(column=3, row=2)

btn_dividir = Button(ventana, text="Dividir", command=dividir)
btn_dividir.grid(column=4, row=2)

resultado = Label(ventana, text="Resultado")
resultado.grid(column=2, row=4, sticky=(W, E))

app.mainloop()
