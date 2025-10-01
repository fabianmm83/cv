from flask import Flask
from .routes import main  # Importa las rutas desde routes.py

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')  # Carga la configuración desde config.py

    # Registra el blueprint de las rutas
    app.register_blueprint(main)

    return app