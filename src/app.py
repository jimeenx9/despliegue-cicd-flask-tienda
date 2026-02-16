# Este archivo convierte la aplicación académica en una app ejecutable por CI/CD

from src.aplicacion.app import app
from src.aplicacion.models import db
from src.aplicacion.models import Categoria, Articulo, Usuario

# ===== AUTO-INICIALIZACIÓN =====
with app.app_context():

    # Crear tablas si no existen
    db.create_all()

    # Insertar datos iniciales solo si la DB está vacía
    if not Categoria.query.first():
        categorias = ["Deportes", "Arcade", "Carreras", "Acción"]
        for cat in categorias:
            db.session.add(Categoria(nombre=cat))
        db.session.commit()

        juegos = [
            {"nombre": "Fernando Martín Basket", "precio": 12, "descripcion": "Baloncesto 1 contra 1", "stock": 10, "categoria_id": 1, "imagen": "basket.jpeg", "iva": 21},
            {"nombre": "Hyper Soccer", "precio": 10, "descripcion": "Fútbol Konami", "stock": 7, "categoria_id": 1, "imagen": "soccer.jpeg", "iva": 21},
            {"nombre": "Arkanoid", "precio": 15, "descripcion": "Arcade clásico", "stock": 10, "categoria_id": 2, "imagen": "arkanoid.jpeg", "iva": 21},
            {"nombre": "Tetris", "precio": 6, "descripcion": "Puzzle clásico", "stock": 5, "categoria_id": 2, "imagen": "tetris.jpeg", "iva": 21},
        ]

        for jue in juegos:
            db.session.add(Articulo(**jue))

        db.session.commit()

    # Crear admin automático
    if not Usuario.query.filter_by(username="admin").first():
        user = Usuario(
            username="admin",
            nombre="Administrador",
            email="admin@admin.com",
            admin=True
        )
        user.password = "admin123"
        db.session.add(user)
        db.session.commit()


# ===== ENTRYPOINT PARA DOCKER =====
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
