#Importasmos la libreria grafica tkinter
from tkinter import *
from typing import Sized

#Creamos objeto de la clase tkinter
root = Tk()
#Anadimos un titulo a la ventana
root.title("Hola mundo!")
#Definimos el tamaño de la ventana a mostrar
root.geometry("400x400")

#Creamos los label que se visualizaran
my_label = Label(root, text="Hola Inge!", fg="white", bg="black", font="Arial")
#Definimos la posición en la que se mostrará el label
my_label.grid(row=0, column=0)

my_label2 = Label(root, text="Otro elemento Inge!")
#Definimos la posición en la que se mostrará el label
my_label2.grid(row=1, column=1, sticky=W)

#Mostramos la ventana
root.mainloop()