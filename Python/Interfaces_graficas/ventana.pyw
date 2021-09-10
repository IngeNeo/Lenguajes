from tkinter import Tk, Label, Button

def miFuncion():
	print("Mensaje de la función")

ventana = Tk()
ventana.geometry("400x200")
ventana.title("Primera ventana con Tkinter")

lbl = Label(ventana, text="Este es un [label] ")
lbl.pack()

#btn = Button(ventana, text="Presionar", command=miFuncion)
btn = Button(ventana, text="Presionar", fg="Red", bg="yellow", command=miFuncion)
#btn.config(fg="Red", bg="yellow")
#btn["fg"] = "Red"
#btn["bg"] = "Blue"
btn.pack()

ventana.mainloop()