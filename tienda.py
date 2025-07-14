from abc import ABC, abstractmethod
class ItemInventario(ABC):
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

    @abstractmethod
    def detalles(self):
        pass
class ProductoFisico(ItemInventario):
    def detalles(self):
        return f"Producto Físico - {self.nombre}: {self.precio:.2f} €"

class ProductoDigital(ItemInventario):
    def detalles(self):
        return f"Producto Digital - {self.nombre}: {self.precio:.2f} €"

class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"[{self.codigo}] {self.nombre} - Precio: {self.precio:.2f} €"


def buscar_producto(inventario, codigo_buscar):
   for producto in inventario:
        if producto.codigo == codigo_buscar:
            return producto

def mostrar_inventario(inventario):
    print("\n--- INVENTARIO ACTUAL ---")
    if not inventario:
        print("El inventario está vacío.")
    else:
        for producto in inventario:
            print(producto)


def calcular_valor_total(inventario):
    total = 0.0
    for producto in inventario:
        total += producto.precio
    return total


def main():
    inventario = [
        Producto("PROD001", "Teclado Mecánico", 75.50),
        Producto("PROD002", "Mouse Inalámbrico", 25.00)
    ]

    while True:
        print("\n===============================")
        print("  MENÚ DE GESTIÓN DE INVENTARIO")
        print("===============================")
        print("1. Mostrar inventario")
        print("2. Buscar producto")
        print("3. Calcular valor total del inventario")
        print("4. Salir")
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == '1':
            mostrar_inventario(inventario)
        elif opcion == '2':
            codigo_buscar = input("Ingrese el código del producto a buscar: ")
            producto_encontrado = buscar_producto(inventario, codigo_buscar)
            if producto_encontrado:
                print(f"\n>> Producto encontrado: {producto_encontrado}")
            else:
                print(">> No se encontró ningún producto con ese código.")

        elif opcion == '3':
            valor_total = calcular_valor_total(inventario)
            print(f"\n>> El valor total del inventario es: {valor_total:.2f} €")
        elif opcion == '4':
            print("\nSaliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elija entre 1 y 4.")


if __name__ == "__main__":
    main()
