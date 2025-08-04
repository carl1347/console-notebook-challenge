# TODO: Agrega el código de las clases de la interfaz de usuario aquí. Borra este comentario al terminar.
class UI Notebook:
    def __init__(self):
        self.notas = []  # Aquí se guardarían las notas

    def mostrar_menu(self):
        print("\n--- Menú ---")
        print("1. Agregar nota")
        print("2. Listar notas")
        print("3. Agregar etiqueta a nota")
        print("4. Listar notas importantes")
        print("5. Eliminar nota")
        print("6. Mostrar notas por etiqueta")
        print("7. Mostrar etiqueta con más notas")
        print("8. Salir")

    def agregar_nota(self):
        titulo = input("Título de la nota: ")
        contenido = input("Contenido de la nota: ")
        importante = input("¿Es importante? (s/n): ").lower() == 's'
        nota = {
            "titulo": titulo,
            "contenido": contenido,
            "importante": importante,
            "etiquetas": []
        }
        self.notas.append(nota)
        print("Nota agregada.")

    def listar_notas(self):
        if not self.notas:
            print("No hay notas.")
        for idx, nota in enumerate(self.notas):
            print(f"{idx + 1}. {nota['titulo']}")

