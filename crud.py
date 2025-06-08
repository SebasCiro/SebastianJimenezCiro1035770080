class Producto:
    def __init__(self, id, nombre, descripcion, precio, cantidad):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad = cantidad


class ProductoCRUD:
    def __init__(self):
        self.productos = []

    def crear_producto(self, id, nombre, descripcion, precio, cantidad):
        if any(p.id == id for p in self.productos):
            raise ValueError("El ID del producto ya está registrado.")
        producto = Producto(id, nombre, descripcion, precio, cantidad)
        self.productos.append(producto)
        return producto

    def listar_productos(self):
        return self.productos

    def actualizar_producto(self, id, nuevo_nombre=None, nueva_descripcion=None, nuevo_precio=None, nueva_cantidad=None):
        for producto in self.productos:
            if producto.id == id:
                if nuevo_nombre is not None:
                    producto.nombre = nuevo_nombre
                if nueva_descripcion is not None:
                    producto.descripcion = nueva_descripcion
                if nuevo_precio is not None:
                    producto.precio = nuevo_precio
                if nueva_cantidad is not None:
                    producto.cantidad = nueva_cantidad
                return producto
        return None

    def eliminar_producto(self, id):
        for producto in self.productos:
            if producto.id == id:
                self.productos.remove(producto)
                return True
        return False
