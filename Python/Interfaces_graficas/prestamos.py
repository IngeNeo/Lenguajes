import tkinter as tk
from tkinter.constants import END
import tkinter.font as tkFont

class App:
	def __init__(self, root):
		self.numerocuotas = {}
		#setting title
		root.title("Software de prestamos")
		#setting window size
		width=500
		height=500
		screenwidth = root.winfo_screenwidth()
		screenheight = root.winfo_screenheight()
		alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
		root.geometry(alignstr)
		root.resizable(width=False, height=False)

		self.eti_titulo=tk.Label(root)
		ft = tkFont.Font(family='Times',size=16)
		self.eti_titulo["font"] = ft
		self.eti_titulo["fg"] = "#d61e1e"
		self.eti_titulo["justify"] = "center"
		self.eti_titulo["text"] = "SOFTWARE DE PRESTAMOS"
		self.eti_titulo.place(x=90,y=50,width=293,height=30)

		self.eti_cliente=tk.Label(root)
		ft = tkFont.Font(family='Times',size=12)
		self.eti_cliente["font"] = ft
		self.eti_cliente["fg"] = "#1e90ff"
		self.eti_cliente["justify"] = "center"
		self.eti_cliente["text"] = "Nombre de cliente"
		self.eti_cliente.place(x=70,y=130,width=124,height=30)

		self.campo_cliente=tk.Entry(root)
		self.campo_cliente["borderwidth"] = "1px"
		ft = tkFont.Font(family='Times',size=10)
		self.campo_cliente["font"] = ft
		self.campo_cliente["fg"] = "#333333"
		self.campo_cliente["justify"] = "center"
		self.campo_cliente["text"] = ""
		self.campo_cliente.place(x=230,y=130,width=134,height=30)

		self.eti_prestamo=tk.Label(root)
		ft = tkFont.Font(family='Times',size=12)
		self.eti_prestamo["font"] = ft
		self.eti_prestamo["fg"] = "#1e90ff"
		self.eti_prestamo["justify"] = "center"
		self.eti_prestamo["text"] = "Valor del prestamo"
		self.eti_prestamo.place(x=70,y=180,width=128,height=30)

		self.campo_prestamo=tk.Entry(root)
		self.campo_prestamo["borderwidth"] = "1px"
		ft = tkFont.Font(family='Times',size=10)
		self.campo_prestamo["font"] = ft
		self.campo_prestamo["fg"] = "#333333"
		self.campo_prestamo["justify"] = "center"
		self.campo_prestamo["text"] = ""
		self.campo_prestamo.place(x=230,y=180,width=134,height=30)

		self.eti_cuotas=tk.Label(root)
		ft = tkFont.Font(family='Times',size=12)
		self.eti_cuotas["font"] = ft
		self.eti_cuotas["fg"] = "#1e90ff"
		self.eti_cuotas["justify"] = "center"
		self.eti_cuotas["text"] = "Numero de cuotas"
		self.eti_cuotas.place(x=70,y=240,width=128,height=30)

		self.campo_cuota=tk.Entry(root)
		self.campo_cuota["borderwidth"] = "1px"
		ft = tkFont.Font(family='Times',size=10)
		self.campo_cuota["font"] = ft
		self.campo_cuota["fg"] = "#333333"
		self.campo_cuota["justify"] = "center"
		self.campo_cuota["text"] = ""
		self.campo_cuota.place(x=230,y=240,width=134,height=30)

		self.eti_interes=tk.Label(root)
		ft = tkFont.Font(family='Times',size=12)
		self.eti_interes["font"] = ft
		self.eti_interes["fg"] = "#1e90ff"
		self.eti_interes["justify"] = "center"
		self.eti_interes["text"] = "Interes"
		self.eti_interes.place(x=140,y=300,width=70,height=25)

		self.campo_interes=tk.Entry(root)
		self.campo_interes["borderwidth"] = "1px"
		ft = tkFont.Font(family='Times',size=10)
		self.campo_interes["font"] = ft
		self.campo_interes["fg"] = "#333333"
		self.campo_interes["justify"] = "center"
		self.campo_interes["text"] = ""
		self.campo_interes.place(x=230,y=300,width=134,height=30)

		self.listas_cuotas=tk.Listbox(root)
		self.listas_cuotas["borderwidth"] = "1px"
		ft = tkFont.Font(family='Times',size=10)
		self.listas_cuotas["font"] = ft
		self.listas_cuotas["fg"] = "#333333"
		self.listas_cuotas["justify"] = "center"
		self.listas_cuotas.place(x=110,y=400,width=288,height=65)

		self.btn_cancelar=tk.Button(root)
		self.btn_cancelar["bg"] = "#efefef"
		ft = tkFont.Font(family='Times',size=10)
		self.btn_cancelar["font"] = ft
		self.btn_cancelar["fg"] = "#000000"
		self.btn_cancelar["justify"] = "center"
		self.btn_cancelar["text"] = "Cancelar"
		self.btn_cancelar.place(x=130,y=360,width=70,height=25)
		self.btn_cancelar["command"] = self.cancelar

		self.btn_calcular=tk.Button(root)
		self.btn_calcular["bg"] = "#efefef"
		ft = tkFont.Font(family='Times',size=12)
		self.btn_calcular["font"] = ft
		self.btn_calcular["fg"] = "#000000"
		self.btn_calcular["justify"] = "center"
		self.btn_calcular["text"] = "Calcular"
		self.btn_calcular.place(x=290,y=360,width=70,height=25)
		self.btn_calcular["command"] = self.calcular

	def cancelar(self):
		self.campo_cliente.delete(0, END)
		self.campo_prestamo.delete(0, END)
		self.campo_cuota.delete(0, END)
		self.campo_interes.delete(0, END)
		self.listas_cuotas.delete(0, END)

	def calcular(self):
		print("command")

if __name__ == "__main__":
	root = tk.Tk()
	app = App(root)
	root.mainloop()