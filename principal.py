from BD.conexion import DAO
from funciones import Funciones
from colorama import Fore, init

class Principal:
    def __init__(self) -> None:
        self.menuPrincipal()
    def menuPrincipal(self):
        opcion=-1
        bandera=True
        while bandera != False:
            print(Fore.BLUE +"==================== MENÚ PRINCIPAL ====================")
            print("1.- Listar jugadores")
            print("2.- Registrar jugadores")
            print("3.- Actualizar jugadores")
            print("4.- Eliminar jugadores")
            print("5.- Salir")
            print("========================================================")
            try:
                opcion = int(input("Seleccione una opción: "))
            except:
                print("Ingrese una opcion mostrada")
            if opcion < 1 or opcion > 5:
                    print("Opción incorrecta, ingrese nuevamente...")
            elif opcion == 5:
                bandera = False
                print("¡Gracias por usar este sistema!")
                break
            else:
                self.ejecutarOpcion(opcion)


    def ejecutarOpcion(self,opcion):
        dao = DAO()
        funciones=Funciones()

        if opcion == 1:
            try:
                cursos = dao.listarJugadores()
                if len(cursos) > 0:
                    funciones.listarCursos(cursos)
                else:
                    print("No se encontraron jugadores...")
            except:
                print("Ocurrió un error...")
        elif opcion == 2:
            curso = funciones.pedirDatosRegistro()
            try:
                dao.registrarJugadores(curso)
            except:
                print("Ocurrió un error...")
        elif opcion == 3:
            try:
                cursos = dao.listarJugadores()
                if len(cursos) > 0:
                    curso = funciones.pedirDatosActualizacion(cursos)
                    if curso:
                        dao.actualizarJugadores(curso)
                    else:
                        print("Código de jugador a actualizar no encontrado...\n")
                else:
                    print("No se encontraron jugadores...")
            except:
                print("Ocurrió un error...")
        elif opcion == 4:
            opcion=-1
            bandera=True
            while bandera != False:
                print("==================== MENÚ PRINCIPAL ====================")
                print("1.- Eliminar Jugador")
                print("2.- Eliminar Equipo")
                print("3.- Volver")
                print("========================================================")
                try:
                    opcion = int(input("Seleccione una opción mostrada: "))
                except:
                    print("Ingrese una opcion mostrada")
                if opcion==1:
                    try:
                        cursos = dao.listarJugadores()
                        if len(cursos) > 0:
                            codigoEliminar = funciones.pedirDatosEliminacion(cursos)
                            if not codigoEliminar==[]:
                                dao.eliminarJugadores(codigoEliminar)
                            else:
                                print("Código de curso no encontrado...\n")
                        else:
                            print("No se encontraron jugadores...")
                    except:
                        print("Ocurrió un error...")
                elif opcion==2:
                    try:
                        cursos = dao.listarEquipos()
                        if len(cursos) > 0:
                            codigoEliminar = funciones.pedirDatosEliminacionEquipo(cursos)
                            if not codigoEliminar==[]:
                                dao.eliminarEquipo(codigoEliminar)
                            else:
                                print("Código de jugador no encontrado...\n")
                        else:
                            print("No se encontraron jugadores...")
                    except:
                        print("Ocurrió un error...")
                elif opcion==3:
                    self.menuPrincipal()
        else:
            print("Opción no válida...")
Principal()