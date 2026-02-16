import unittest
from src.app import app

class BasicTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_status_code(self):
        """La página principal debe responder correctamente"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_contains_title(self):
        """La página principal debe contener texto de la tienda"""
        response = self.app.get('/')
        self.assertIn("Tienda de Videojuegos", response.data.decode())

if __name__ == "__main__":
    unittest.main()
