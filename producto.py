"""
Ejercicio:4 punto 7
Tenemos a `Producto` separado.
aquí se aprecia bien que las clases abstractas son de "uso interno" y
bien prodrian ser privadas

"""
from abc import ABC, abstractmethod


class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"[{self.codigo}] {self.nombre} - Precio: {self.precio:.2f} €"


class _Promocionable(ABC):
    @abstractmethod
    def aplicar_descuento(self, porcentaje):
        pass


class _ItemInventario(ABC, Producto):
    @abstractmethod
    def detalles(self):
        pass

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        self.precio = precio

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")
        self.nombre = nombre


class ProductoFisico(_ItemInventario):
    def detalles(self):
        return f"Producto Físico - {self.nombre}: {self.precio:.2f} €"


class ProductoDigital(_ItemInventario):
    def detalles(self):
        return f"Producto Digital - {self.nombre}: {self.precio:.2f} €"


class ProductoEspecial(ProductoFisico, _Promocionable):
    def aplicar_descuento(self, porcentaje):
        if not (0 <= porcentaje <= 100):
            raise ValueError("El porcentaje debe estar entre 0 y 100.")
        self.set_precio(self.get_precio() * (1 - porcentaje / 100))


"""
    Finalmente solo exportamos lo que se quiere ofrecer al usuario del módulo.
"""
__all__ = [
    "Producto",
    "ProductoFisico",
    "ProductoDigital",
    "ProductoEspecial",
]
