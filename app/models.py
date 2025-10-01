from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Proyecto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    url = db.Column(db.String(200))

    def __repr__(self):
        return f"<Proyecto {self.nombre}>"