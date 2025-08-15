class Libro:
    def __init__(self, titulo, autor, publicacion):
        self.titulo = titulo
        self.autor = autor
        self.publicacion = publicacion

    def __str__(self):
        return f'Titulo: {self.titulo}, autor: {self.autor}, año de publicacion: {self.publicacion}'

class Usuario:
    def __init__(self, nombre, carrera):
        self.nombre = nombre
        self.carrera = carrera

    def __str__(self):
        return f'Nombre: {self.nombre}, carrera: {self.carrera}'


class GestionLibro:
    def __init__(self):
        self.libros = {}

    def agregar(self):
        while True:
            try:
                codigo = input("Codigo del libro: ")
                if codigo in self.libros:
                    print("Ya existe un libro con el código ingresado, intente con uno diferente")
                    continue
                titulo = input("\tTitulo: ")
                autor = input("\tAutor: ")
                publicacion = int(input("\tAño de publicación: "))
                if publicacion < 700 or publicacion > 2025:
                    print("Año de publicación no válida, el registro no se completó, intente de nuevo")
                    continue
                libro = Libro(titulo, autor, publicacion)
                self.libros[codigo] = {'libro': libro, 'estado': "Disponible"}
                print("El registro se completó correctamente")
                break
            except ValueError:
                print("ERROR: Dato ingresado no válido, el registro no se completó, intente de nuevo")

    def buscar(self, codigo):
        if codigo in self.libros:
            return self.libros[codigo]
        return None

    def mostrar(self):
        if len(self.libros) < 1:
            print("No hay libros registrados")
        else:
            print("Libros agregados:")
            for codigo, libro in self.libros.items():
                print(f"\nCódigo del libro: {codigo}")
                print(f"\t{libro['libro']}", end=" ")
                print("Estado: ", libro['estado'])


class GestionUsuario:
    def __init__(self):
        self.usuarios = {}

    def agregar(self):
        while True:
            carne = input("Carné del estudiante: ")
            if carne in self.usuarios:
                print("Ya hay un usuario registrado con el carné ingresado, intente con uno diferente")
                continue
            nombre = input("\tNombre: ")
            carrera = input("\tCarrera: ")
            usuario = Usuario(nombre, carrera)
            self.usuarios[carne] = {'usuario': usuario}
            print("Se completó el registro correctamente")
            break

    def buscar(self, carne):
        if carne in self.usuarios:
            return self.usuarios[carne]
        else:
            return None

    def mostrar(self):
        if len(self.usuarios) < 1:
            print("No hay usuarios registrados")
        else:
            print("Usuarios agregados:")
            for carne, usuario in self.usuarios.items():
                print(f"Carné: {carne}")
                print(f"\t{usuario['usuario']}")


class GestionarPrestamo:
    def __init__(self):
        self.prestamos = {}

    def realizar_prestamo(self, libro, usuario):
        try:
            codigo_libro = input("Código del libro: ")
            buscar_libro = libro.buscar(codigo_libro)
            if buscar_libro is None or buscar_libro["estado"] != "Disponible":
                raise ValueError("Libro no encontrado o no disponible.")
            carnet_usuario = input("Carné del usuario: ")
            buscar_usuario = usuario.buscar(carnet_usuario)
            if buscar_usuario is None:
                raise ValueError("Usuario no encontrado.")
            num_prestamo = input("Número de préstamo: ")
            if num_prestamo in self.prestamos:
                raise ValueError("Ya existe un préstamo con ese número.")
            self.prestamos[num_prestamo] = {
                "libro": buscar_libro,
                "usuario": buscar_usuario
            }
            buscar_libro["estado"] = "No disponible"
            print("Préstamo registrado correctamente.")

        except ValueError as e:
            print(f"Error: {e}")

    def mostrar(self):
        if len(self.prestamos) < 1:
            print("No se ha realizado ningún préstamo")
        else:
            print("Prestamos agregados:")
            for num_prestamo, prestamo in self.prestamos.items():
                print(f"Péstamo número: {num_prestamo}")
                print(f"\tLibro: {prestamo['libro']['libro']}, usuario: {prestamo['usuario']['usuario']}")


opcion = 0
gestionar_libro = GestionLibro()
gestionar_usuario = GestionUsuario()
gestionar_prestamo = GestionarPrestamo()
while opcion != 6:
    print("----MENÚ----")
    print("1.Registrar libro")
    print("2.Registrar usuario")
    print("3.Mostrar libros y usuarios")
    print("4.Realizar préstamo")
    print("5.Mostrar prestamos")
    print("6.Salir")
    try:
        opcion = int(input("\nSeleccione una opción: "))
        match opcion:
            case 1:
                print("---REGISTRAR LIBRO---")
                print("Ingrese datos del libro: ")
                gestionar_libro.agregar()
            case 2:
                print("---REGISTRAR USUARIO---")
                print("Ingrese datos del usuario: ")
                gestionar_usuario.agregar()
            case 3:
                print("---MOSTRAR LIBROS Y USUARIOS---")
                gestionar_libro.mostrar()
                gestionar_usuario.mostrar()
            case 4:
                print("---REALIZAR PRÉSTAMO---")
                gestionar_prestamo.realizar_prestamo(gestionar_libro, gestionar_usuario)
            case 5:
                print("---MOSTRAR PRÉSTAMOS---")
                gestionar_prestamo.mostrar()
            case 6:
                confirmar = int(input("¿Está seguro que desea salir del programa? \n1.Si\t2.No\nR: "))
                if confirmar == 1:
                    print("Saliendo del programa...")
                elif confirmar == 2:
                    print("Regresando al menú...")
                    opcion = 0
                else:
                    print("Confirmación no válida, regresando al menú")
                    opcion = 0
            case _:
                print("Opción no válida")
    except ValueError:
        print("ERROR: Dato ingresado no válido")
