class Libro:
    def __init__(self, titulo, autor, publicacion):
        self.titulo = titulo
        self.autor = autor
        self.publicacion = publicacion

    def __str__(self):
        return f'Titulo: {self.titulo}, autor: {self.autor}, año de publicacion: {self.publicacion}'

class AgregarLibor:
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
                publicacion = int(input("\tAño de ublicacion: "))
                if publicacion < 700 or publicacion > 2025:
                    print("Año de publicación no válida, el registro no se completó, intente de nuevo")
                    continue
                libro = Libro(titulo, autor, publicacion)
                self.libros[codigo] = {'libro', libro, 'estado', "Disponible"}
                print("El registro se completó correctamente")
                break
            except ValueError:
                print("ERROR: Dato ingresado no válido, el registro no se completó, intente de nuevo")

    def cambiar_estado(self, codigo):
        self.libros[codigo]['estado'] = "No disponible"

    def mostrar(self):
        if len(self.libros) < 1:
            print("No hay libros registrados")
        else:
            print("Libros agregados:")
            for codigo, libro in self.libros.items():
                print(f"\nCódigo del libro: {codigo}")
                print(f"\t{libro['libro']}", end=" ")
                print("Estado: ", libro['estado'])

class Usuario:
    def __init__(self, nombre, carrera):
        self.nombre = nombre
        self.carrera = carrera

    def __str__(self):
        return f'Nombre: {self.nombre}, carrera: {self.carrera}'

class AgregarUsuario:
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
            self.usuarios[carne] = usuario
class GestionarPrestamo:
    def __init__(self):
        self.prestamos = {}
