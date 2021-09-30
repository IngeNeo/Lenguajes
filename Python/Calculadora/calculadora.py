import tkinter as Tk
from tkinter import *


def sumar():
	n1 = int(campo1.get())
	n2 = int(campo2.get())
	suma = n1 + n2
	resultado.config(text=suma)

def restar():
	resta = int(campo1.get()) - int (campo2.get())
	resultado.config(text=resta)

def multiplicar():
	multiplica = int(campo1.get()) * int (campo2.get())
	resultado.config(text=multiplica)

def dividir():
	divide = int(campo1.get()) / int (campo2.get())
	resultado.config(text=divide)


app = Tk()
app.title("Calculadora En Python")


ventana = Frame(app)
ventana.grid(column=0, row=0, padx=(50,50), pady=(50,50))
ventana.columnconfigure(0, weight=2)
ventana.rowconfigure(0, weight=2)

numero1 = Label(ventana, text="Digite un numero")
numero1.grid(column=1, row=1, sticky=(W,E))

valor =""
campo1 = Entry(ventana, textvariable=valor)
campo1.grid(column=2, row=1)

numero2 = Label(ventana, text="Digite otro numero cualquiera")
numero2.grid(column=3, row=1, sticky=(W,E))

valor2 =""
campo2 = Entry(ventana, textvariable=valor2)
campo2.grid(column=4, row=1)


btn_sumar = Button(ventana, text="Sumar", command=sumar)
btn_sumar.grid(column=1, row=3)

btn_restar = Button(ventana, text="Restar", command=restar)
btn_restar.grid(column=2, row=3)

btn_multiplicar = Button(ventana, text="Multiplicar", command=multiplicar)
btn_multiplicar.grid(column=3, row=3)

btn_dividir = Button(ventana, text="Dividir", command=dividir)
btn_dividir.grid(column=4, row=3)

resultado = Label(ventana, text="El resultado es:")
resultado.grid(column=2, row=5)

app.mainloop()