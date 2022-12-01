from colorama import Fore, init
class Funciones:
    def listarCursos(self,cursos):
        print("\nCursos: \n")
        contador = 1
        for jug in cursos:
            datos = "\n{0}. \n|id:{1}\n|Equipo:{2}\n|Nombre:{3}\n|Apellido:{4}\n|Numero Camiseta:{5}\n|Posicion:{6}\n|Numero de goles:{7}\n|Partidas ganadas:{8}\n|Edad:{9} años\n|peso:{10} kg\n|altura:{11} cm"
            print(datos.format(contador,jug[0],jug[1],jug[2],jug[3],jug[4],jug[5],jug[6],jug[7],jug[8],jug[9],jug[10]))
            contador = contador + 1
        print(" ")
    
    def listarEquipos(self,cursos):
        print("\nequipos: \n")
        contador = 1
        for jug in cursos:
            datos = "Equipo:{0}"
            print(datos.format(jug[0]))
            contador = contador + 1
        print(" ")


    def pedirDatosRegistro(self):
        codigoCorrecto = False
        while(not codigoCorrecto):
            id = input(Fore.GREEN +"Ingrese id: ")
            if len(id) == 3:
                codigoCorrecto = True
            else:
                print("Código incorrecto: Debe tener 3 dígitos.")

        equipo = input("Ingrese equipo: ")
        nombre = input("Ingrese nombre: ")
        apellido = input("Ingrese apellido: ")
        nroCamiseta= input("Ingrese numero de camiseta: ")
        posicion= input("Ingrese posicion: ")
        nroGoles= input("Ingrese numero de goles: ")
        nroPartidas= input("Ingrese numero de partidas: ")
        edad= input("Ingrese edad: ")
        peso= input("Ingrese peso en kg: ")
        altura= input("Ingrese en cm: ")

        curso = (id,equipo,nombre,apellido,nroCamiseta,posicion,nroGoles,nroPartidas,edad,peso,altura)
        return curso

    def pedirDatosActualizacion(self,cursos):
        self.listarCursos(cursos)
        existeCodigo = False
        id = int(input("Ingrese el id del jugador a editar: "))
        for jug in cursos:
            if jug[0] == id:
                existeCodigo = True
                break

        if existeCodigo:
            equipo = input("Ingrese equipo a modificar: ")
            nombre = input("Ingrese nombre a modificar: ")
            apellido = input("Ingrese apellido a modificar: ")
            nroCamiseta= input("Ingrese numero de camiseta a modificar: ")
            posicion= input("Ingrese posicion a modificar: ")
            nroGoles= input("Ingrese numero de goles a modificar: ")
            nroPartidas= input("Ingrese numero de partidas a modificar: ")
            edad= input("Ingrese edad a modificar: ")
            peso= input("Ingrese peso en kg a modificar: ")
            altura= input("Ingrese en cm a modificar: ")


            curso = (id,equipo,nombre,apellido,nroCamiseta,posicion,nroGoles,nroPartidas,edad,peso,altura)
        else:
            curso = None

        return curso


    def pedirDatosEliminacion(self,cursos):
        self.listarCursos(cursos)
        existeCodigo = False
        codigoEliminar =int(input("Ingrese el id del jugador a eliminar:"))
        for jug in cursos:
            if jug[0] == codigoEliminar:
                existeCodigo = True
                break

        if not existeCodigo:
            codigoEliminar=""
        return codigoEliminar

    def pedirDatosEliminacionEquipo(self,cursos):
        self.listarEquipos(cursos)
        existeCodigo = False
        codigoEliminar =str(input("Ingrese el nombre del equipo a eliminar:"))
        for jug in cursos:
            if jug[0] == codigoEliminar:
                existeCodigo = True
                break

        if not existeCodigo:
            codigoEliminar=""
        return codigoEliminar