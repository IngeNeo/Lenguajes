from tkinter import * #Importamos todo lo que contiene la libreria

"""main_window = Tk() #Declaramos e inicializamos la ventana principal
main_window.mainloop() #Usamos esta funcion para permitir que la ventana permanezca abierta durante la ejecución."""

"""main_window = Tk()

main_frame = Frame(main_window, bg='#ff0033', height=500, width=500, cursor='dot')
#Declaramos el marco y sus propiedades
main_frame.pack() #Lo instanciamos en la interfaz
main_window.mainloop()"""

"""main_window = Tk()
main_frame = Frame(main_window, bg='green', height=500, width=500, padx=50, pady= 50)
main_frame.pack()
title_label = Label(main_frame, text="Hola Mundo!!", font=('Arial',11)) #Definimos el label y sus propiedades
title_label.pack() #Lo instanciamos en la interfaz
body_label1 = Label(main_frame, text="Bye Inge")
body_label1.pack()
main_window.mainloop()"""

"""main_window = Tk()
main_frame = Frame(main_window, bg='green', height=500, width=500, padx=50, pady=50)
main_frame.pack()
title_label = Label(main_frame, text="Hola Mundo!!", font=('Arial',11))
title_label.pack()
imagen = PhotoImage(file='python-logo.png') #Asignamos una variable al archivo de la imagen
body_label1 = Label(main_frame, image=imagen) #Asignamos la imagen como una propiedad                del label
body_label1.pack()
main_window.mainloop()"""

"""main_window = Tk()
main_frame = Frame(main_window, bg='green', height=500, width=500, padx=50, pady=50)
main_frame.pack()
title_label = Label(main_frame, text="Hola Mundo!!", font=('Arial',11))
title_label.pack()
boton = Button(main_frame, text="Inge") #Declaramos el boton y sus propiedades
boton.pack()
main_window.mainloop()"""


"""def accion(): #Funcion que sera ejecutada por el boton
	global boton_text
	if boton_text == "Inge":
		boton_text ='Bye!'
	else:
		boton_text ='Hola Inge'
	boton.config(text=boton_text)

main_window = Tk()
main_frame = Frame(main_window, bg='green', height=500, width=500, padx=50, pady=50)
main_frame.pack()
title_label = Label(main_frame, text="Hola Mundo!!", font=('Arial',11))
title_label.pack()

boton_text='Inge'
boton = Button(main_frame, text=boton_text, command=accion) #Asignamos la funcion al
boton.pack()
main_window.mainloop()"""

"""def accion(mensaje):
	title_label.config(text=mensaje)

main_window = Tk()
main_frame = Frame(main_window, bg='green', height=500, width=500, padx=50, pady=50)
main_frame.pack()
title_label = Label(main_frame, text="Hola Mundo!!", font=('Arial',11))
title_label.pack()
boton_text='Boton'
mensaje = "Este es un parametro"
boton = Button(main_frame, text=boton_text, command= lambda: accion(mensaje))
boton.pack()
main_window.mainloop()"""

def accion():
	text = textbox.get()
	textbox.delete(0,END)
	text_label.config(text=text)

main_window = Tk()
main_frame = Frame(main_window, bg='green', height=500, width=500, padx=50, pady=50)
main_frame.pack()
title_label = Label(main_frame, text="Hola Mundo!!", font=('Arial',11))
title_label.pack()

boton_text='Boton'
boton = Button(main_frame, text=boton_text, command= accion)
boton.pack()

textbox = Entry(main_frame)
textbox.pack()
text_label = Label(main_frame, bg="green")
text_label.pack()
main_window.mainloop()