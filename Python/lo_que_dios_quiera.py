
class Asignatura:
      # propiedades del objeto
    estudiante_id = None
    estudiante = None
    profesor = None
    nombre = None
    nota1 = None
    nota2 = None
    nota3 = None

      # constructor
    def __init__(self, alumno = None, notaI = 0, notaII = 0, notaIII = 0
                , alumno_id = None, docente = None,
                materia = None):
          self.estudiante = alumno
          self.nota1 = notaI
          self.nota2 = notaII
          self.nota3 = notaIII
          self.estudiante_id = alumno_id
          self.profesor = docente
          self.nombre = materia

    def calcular_nota_definitiva(self):
        return self.nota1 * 0.30 + self.nota2 * 0.3 + self.nota3 * 0.4


class GestionAcademica:
    matricula = None

    def __init__(self):
        self.matricula = dict()

    def agregar_asignatura(self, asignatura):
        if asignatura.nombre  in self.matricula.keys():
            return False
        else:
            self.matricula[asignatura.nombre] = asignatura
            return len(self.matricula)

    def buscar_asignatura(self, nombre):
        nombres_asginatura = self.matricula.keys()
        asignaturas_encontradas = {}
        for materia in nombres_asginatura:
            if materia.find(nombre):
                asignaturas_encontradas[materia] = self.matricula[materia]
        return asignaturas_encontradas

    def registrar_nota(self, nombre_asignatura, nota1 = None, nota2 = None, nota3 = None):
        asignaturas = self.buscar_asignatura(nombre_asignatura)
        if len(asignaturas) == 1:
            materia = asignaturas[nombre_asignatura]
            if nota1 != None:
                materia.nota1 = nota1
            if nota2 != None:
                materia.nota2 = nota2
            if nota3 != None:
                materia.nota3 = nota3
        elif len(asignaturas) > 1:
            print("Asignaturas Disponibles")
            cuenta = 1
            salir = True
            while salir:
                for clave in asignaturas.keys():
                    print(cuenta,").",clave)
                else:
                    print("Escoja una: ", end="")
                    nombre = input()
                    if nombre in asignaturas.keys():
                       n1 = nota1
                       n2 = nota2
                       n3 = nota3
                       salir = False
                       self.registrar_nota(self, nombre, nota1=n1, nota2=n2, nota3=n3)
        else:
            print("Asignatura no existe")


print("PROGRAMA DE NOTAS")
print("==================")

secretaria = GestionAcademica()

salir = False
materia = Asignatura()
while not salir:
    materia.estudiante_id = input("Ingrese el Codigo del Estudiante: ")
    materia.estudiante =  input("Ingrese el Nombre del Estudiante: ")
    materia.profesor =  input("Ingrese el Nombre del Profesor: ")
    materia.nombre = input("Ingrese el Nombre de la Asignatura: ")
    materia.nota1 =  input(f"La Nota I de {materia.nombre} de {materia.estudiante}: ")
    materia.nota2 =  input(f"La Nota II de {materia.nombre} de {materia.estudiante}: ")
    materia.nota3 =  input(f"La Nota III de {materia.nombre} de {materia.estudiante}: ")
    if not secretaria.agregar_asignatura(materia):
        print(f"La asignatura {materia.nombre} ya existe")
    while True:
        res = input("¿Desea agregar otra asignatura? SI/NO: ")
        res = res.upper()
        if res != "NO" and res != "SI":
            print("SI/NO")
        elif res == "NO":
           salir = True
           break
        elif res == "SI":
            break
else:
    print("SU REPORTE DE NOTAS ES:")
    print("**************************")
    print("")
    cuenta = 1
    for nombre, materia in secretaria.matricula.items():
        print(cuenta,"), ",nombre )
        print("------------------")
        nd = materia.calcular_nota_definitiva()
        print("NOTA DEFINITIVA:",nd)
