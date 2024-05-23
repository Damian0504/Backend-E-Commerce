from typing import List

class Producto:
    def __init__(self, nombre: str, precio: float, stock: int):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def incrementar_stock(self, cantidad: int) -> None:
        if cantidad > 0:
            self.stock += cantidad
            print(f"Stock de {self.nombre} incrementado en {cantidad}. Stock actual: {self.stock}")
        else:
            print("Cantidad a incrementar debe ser positiva.")

    def decrementar_stock(self, cantidad: int) -> None:
        if 0 < cantidad <= self.stock:
            self.stock -= cantidad
            print(f"Stock de {self.nombre} decrementado en {cantidad}. Stock actual: {self.stock}")
        else:
            print("Cantidad a decrementar debe ser positiva y no mayor al stock actual.")

    def __repr__(self) -> str:
        return f"Producto(nombre={self.nombre}, precio={self.precio}, stock={self.stock})"

class Proveedor:
    def __init__(self, nombre: str, direccion: str, telefono: str):
        self._nombre = nombre
        self._direccion = direccion
        self._telefono = telefono
        self._productos: List[Producto] = []

    def nombre(self) -> str:
        return self._nombre

    def direccion(self) -> str:
        return self._direccion

    def telefono(self) -> str:
        return self._telefono

    def productos(self) -> List[Producto]:
        return self._productos

    def agregar_producto(self, producto: Producto, cantidad: int) -> None:
        if producto not in self._productos:
            self._productos.append(producto)
            producto.incrementar_stock(cantidad)
            print(f"{producto} ha sido agregado al proveedor con un stock inicial de {cantidad}.")
        else:
            producto.incrementar_stock(cantidad)
            print(f"Stock de {producto} incrementado en {cantidad}. Stock total: {producto.stock}.")

    def eliminar_producto(self, producto: Producto, cantidad: int) -> None:
        if producto in self._productos:
            producto.decrementar_stock(cantidad)
            if producto.stock == 0:
                self._productos.remove(producto)
                print(f"{producto} ha sido eliminado del proveedor debido a que su stock es 0.")
        else:
            print(f"{producto} no está en la lista de productos del proveedor.")

# Ejemplo de uso y explicacion:
#if __name__ == "__main__":
    #proveedor = Proveedor("Proveedor Ejemplo", "Calle Falsa 123", "555-1234")
    #producto1 = Producto("Producto 1", 10.0, 0)
    #producto2 = Producto("Producto 2", 20.0, 0)

    #proveedor.agregar_producto(producto1, 50)
    #proveedor.agregar_producto(producto2, 30)
    #proveedor.eliminar_producto(producto1, 20)
    #proveedor.eliminar_producto(producto2, 30)
    #proveedor.eliminar_producto(producto1, 30)


#Explicación de la Funcionalidad
#Clase Producto:

#Métodos:
#incrementar_stock(cantidad: int): Incrementa el stock del producto en la cantidad especificada.
#decrementar_stock(cantidad: int): Decrementa el stock del producto en la cantidad especificada si es válida.
#Representación:
#__repr__(): Proporciona una representación legible del producto.

#Clase Proveedor:
#Propiedades:
#nombre, direccion, telefono: Información del proveedor.
#productos: Lista de productos asociados al proveedor.
#Métodos:
#agregar_producto(producto: Producto, cantidad: int): Agrega un producto al proveedor e incrementa su stock.
#eliminar_producto(producto: Producto, cantidad: int): Decrementa el stock del producto y lo elimina si el stock llega a cero.
#Ejemplo de Uso:

#Se muestra cómo crear un proveedor y productos.
#Se ilustra cómo agregar productos al proveedor y gestionar su stock.
#Se muestra cómo eliminar productos del proveedor y decrementar su stock.