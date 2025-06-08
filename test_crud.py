import unittest
from crud import ProductoCRUD


class TestProductoCRUD(unittest.TestCase):

    def setUp(self):
        self.crud = ProductoCRUD()

    def test_crear_producto_exitoso(self):
        arroz = self.crud.crear_producto(
            1, "Arroz", "Arroz blanco premium", 4500, 20)
        self.assertEqual(arroz.nombre, "Arroz")

    def test_crear_producto_id_duplicado(self):
        self.crud.crear_producto(2, "Panela", "Panela redonda", 2500, 10)
        with self.assertRaises(ValueError):
            self.crud.crear_producto(
                2, "Panela Morena", "Panela más oscura", 2600, 5)

    def test_listar_productos(self):
        self.crud.crear_producto(3, "Huevos", "Huevos AA x 12", 8200, 8)
        productos = self.crud.listar_productos()
        self.assertEqual(len(productos), 1)

    def test_listar_sin_productos(self):
        productos = self.crud.listar_productos()
        self.assertEqual(productos, [])  # espera una lista vacía

    def test_actualizar_producto_exitoso(self):
        self.crud.crear_producto(4, "Leche", "Leche entera 1L", 3800, 15)
        actualizado = self.crud.actualizar_producto(
            4, nuevo_precio=4000, nueva_cantidad=12)
        self.assertEqual(actualizado.precio, 4000)
        self.assertEqual(actualizado.cantidad, 12)

    def test_actualizar_producto_inexistente(self):
        resultado = self.crud.actualizar_producto(999, nuevo_precio=1000)
        self.assertIsNone(resultado)

    def test_eliminar_producto_exitoso(self):
        self.crud.crear_producto(5, "Aceite", "Aceite vegetal 900ml", 9500, 5)
        eliminado = self.crud.eliminar_producto(5)
        self.assertTrue(eliminado)

    def test_eliminar_producto_inexistente(self):
        resultado = self.crud.eliminar_producto(888)
        self.assertFalse(resultado)

    def test_id_no_se_modifica(self):
        self.crud.crear_producto(10, "Sal", "Sal marina", 1200, 5)
        producto = self.crud.actualizar_producto(10, nuevo_precio=1500)
        self.assertEqual(producto.id, 10)



if __name__ == '__main__':
    unittest.main()
