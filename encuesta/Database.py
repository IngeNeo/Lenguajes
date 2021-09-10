#importamos la librria PyMySQL
import pymysql

class Database:
	def __init__(self):
		self.connections = pymysql.connect(
			host = 'localhost',
			user = 'root',
			password = '',
			db = 'encuesta'
		)

		self.cursor = self.connections.cursor()
		print("Conexión establecida exitosamente!")

	def select_encuesta(self, id):
		sql = 'SELECT id_encuesta, sucursal, nombres_paciente, celular FROM encuesta WHERE id_encuesta = {}'.format(id)

		try:
			self.cursor.execute(sql)
			sucursal = self.cursor.fetchone()

			print("Id:", sucursal[0])
			print("sucursal:", sucursal[1])
			print("nombres_pacientes:", sucursal[2])
			print("celular:", sucursal[3])

		except Exception as e:
			raise

	def select_all_encuesta(self):
		sql = 'SELECT id_encuesta, sucursal, fecha, nombres_paciente, cedula, celular, email, confirmar, s_control, s_gerente, puntualidad, instalaciones, tratamiento, bioseguridad, observaciones FROM encuesta'

		try:
			self.cursor.execute(sql)
			sucursal = self.cursor.fetchall()

			# Las defiimos como globales
			global Cabecera_servicio, Cabecera_puntualidad, Cabecera_instalaciones, Cabecera_tratamiento,Cabecera_bioseguridad, Castellana_servicio, Castellana_puntualidad, Castellana_instalaciones, Castellana_tratamiento, Castellana_bioseguridad, Normandia_servicio, Normandia_puntualidad, Normandia_instalaciones, Normandia_tratamiento, Normandia_bioseguridad, suma_cabecera, suma_castellana, suma_normandia
			#Variables para almacenar puntajes que dan los pacientes
			Cabecera_servicio			= 0
			Cabecera_puntualidad		= 0
			Cabecera_instalaciones		= 0
			Cabecera_tratamiento		= 0
			Cabecera_bioseguridad		= 0
			Castellana_servicio			= 0
			Castellana_puntualidad		= 0
			Castellana_instalaciones	= 0
			Castellana_tratamiento		= 0
			Castellana_bioseguridad		= 0
			Normandia_servicio			= 0
			Normandia_puntualidad		= 0
			Normandia_instalaciones		= 0
			Normandia_tratamiento		= 0
			Normandia_bioseguridad		= 0
			suma_cabecera				= 0
			suma_castellana				= 0
			suma_normandia				= 0

			#For para recorrer los valores de la consulta
			for sucursal in sucursal:

				# Validamos si la sucursal es Cabecera
				if (sucursal[1] == "Cabecera"):

					# Se convierte a numero el valor que trae el campo de la base de datos
					servicio = int(sucursal[9])
					puntualidad = int(sucursal[10])
					instalaciones = int(sucursal[11])
					tratamiento = int(sucursal[12])
					bioseguridad = int(sucursal[13])
					# Se suman los valores de cada campo en su acumulador
					Cabecera_servicio += servicio
					Cabecera_puntualidad += puntualidad
					Cabecera_instalaciones += instalaciones
					Cabecera_tratamiento += tratamiento
					Cabecera_bioseguridad += bioseguridad
					suma_cabecera += 1

				# Validamos si la sucursal es Castellana
				elif (sucursal[1] == "Castellana"):
					# Se convierte a numero el valor que trae el campo de la base de datos
					servicio = int(sucursal[9])
					puntualidad = int(sucursal[10])
					instalaciones = int(sucursal[11])
					tratamiento = int(sucursal[12])
					bioseguridad = int(sucursal[13])
					# Se suman los valores de cada campo en su acumulador
					Castellana_servicio += servicio
					Castellana_puntualidad += puntualidad
					Castellana_instalaciones += instalaciones
					Castellana_tratamiento += tratamiento
					Castellana_bioseguridad += bioseguridad
					suma_castellana += 1

				# Validamos si la sucursal es Normandia
				elif (sucursal[1] == "Normandia"):
					# Se convierte a numero el valor que trae el campo de la base de datos
					servicio = int(sucursal[9])
					puntualidad = int(sucursal[10])
					instalaciones = int(sucursal[11])
					tratamiento = int(sucursal[12])
					bioseguridad = int(sucursal[13])
					# Se suman los valores de cada campo en su acumulador
					Normandia_servicio += servicio
					Normandia_puntualidad += puntualidad
					Normandia_instalaciones += instalaciones
					Normandia_tratamiento += tratamiento
					Normandia_bioseguridad += bioseguridad
					suma_normandia += 1
		except Exception as e:
			raise
#TODO Revisar si se puede simplificar estas funciones

	def promedio_servico(self, sede):
		if (sede == "Cabecera"):
			Resultado = Cabecera_servicio / suma_cabecera
			return Resultado
		elif (sede == "Castellana"):
			Resultado = Castellana_servicio / suma_castellana
			return Resultado
		elif (sede == "Normandia"):
			Resultado = Normandia_servicio / suma_normandia
			return Resultado

	def promedio_puntualidad(self, sede):
		if (sede == "Cabecera"):
			Resultado = Cabecera_puntualidad / suma_cabecera
			return Resultado
		elif (sede == "Castellana"):
			Resultado = Castellana_puntualidad / suma_castellana
			return Resultado
		elif (sede == "Normandia"):
			Resultado = Normandia_puntualidad / suma_normandia
			return Resultado

	def promedio_instalaciones(self, sede):
		if (sede == "Cabecera"):
			Resultado = Cabecera_instalaciones / suma_cabecera
			return Resultado
		elif (sede == "Castellana"):
			Resultado = Castellana_instalaciones / suma_castellana
			return Resultado
		elif (sede == "Normandia"):
			Resultado = Normandia_instalaciones / suma_normandia
			return Resultado

	def promedio_tratamiento(self, sede):
		if (sede == "Cabecera"):
			Resultado = Cabecera_tratamiento / suma_cabecera
			return Resultado
		elif (sede == "Castellana"):
			Resultado = Castellana_tratamiento / suma_castellana
			return Resultado
		elif (sede == "Normandia"):
			Resultado = Normandia_tratamiento / suma_normandia
			return Resultado

	def promedio_bioseguridad(self, sede):
		if (sede == "Cabecera"):
			Resultado = Cabecera_bioseguridad / suma_cabecera
			return Resultado
		elif (sede == "Castellana"):
			Resultado = Castellana_bioseguridad / suma_castellana
			return Resultado
		elif (sede == "Normandia"):
			Resultado = Normandia_bioseguridad / suma_normandia
			return Resultado