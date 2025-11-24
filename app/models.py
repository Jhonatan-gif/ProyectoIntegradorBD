from . import db
from datetime import date

class Catequizando(db.Model):
    __tablename__ = 'Catequizando'
    __table_args__ = {'schema': 'dbo'}
    catequizando_id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    fecha_nacimiento = db.Column(db.Date, nullable=False)
    sexo = db.Column(db.String(1))
    documento_identidad = db.Column(db.String(20))
    direccion = db.Column(db.String(150))
    telefono = db.Column(db.String(20))
    email = db.Column('email', db.String(100))
    escolaridad = db.Column(db.String(50))
    fecha_inscripcion = db.Column(db.Date, default=date.today)
    fe_bautismo_presentada = db.Column(db.Boolean, default=False)
    fecha_bautismo = db.Column(db.Date)
    observaciones = db.Column(db.String(255))

class Representante(db.Model):
    __tablename__ = 'Representante'
    __table_args__ = {'schema': 'dbo'}
    representante_id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    parentesco = db.Column(db.String(30))
    documento_identidad = db.Column(db.String(20))
    telefono = db.Column(db.String(20))
    email = db.Column('email', db.String(100))
    direccion = db.Column(db.String(150))
    observaciones = db.Column(db.String(255))

class Inscripcion(db.Model):
    __tablename__ = 'Inscripcion'
    __table_args__ = {'schema': 'dbo'}
    inscripcion_id = db.Column(db.Integer, primary_key=True)
    catequizando_id = db.Column(db.Integer, db.ForeignKey('dbo.Catequizando.catequizando_id', ondelete='CASCADE'), nullable=False)
    grupo_id = db.Column(db.Integer, db.ForeignKey('dbo.Grupo.grupo_id', ondelete='CASCADE'), nullable=False)
    fecha_inscripcion = db.Column(db.Date, default=date.today)
    estado_inscripcion = db.Column(db.String(20))
    aprobado = db.Column(db.Boolean, default=False)
    motivo_retiro = db.Column(db.String(255))

class Grupo(db.Model):
    __tablename__ = 'Grupo'
    __table_args__ = {'schema': 'dbo'}
    grupo_id = db.Column(db.Integer, primary_key=True)
    nivel_id = db.Column(db.Integer, db.ForeignKey('dbo.Nivel.nivel_id'), nullable=False)
    catequista_principal_id = db.Column(db.Integer, db.ForeignKey('dbo.Catequista.catequista_id'), nullable=False)
    catequista_apoyo_id = db.Column(db.Integer, db.ForeignKey('dbo.Catequista.catequista_id'))
    nombre_grupo = db.Column(db.String(30), nullable=False)
    horario = db.Column(db.String(100))
    periodo = db.Column(db.String(20))
    capacidad = db.Column(db.Integer, default=30)

class Nivel(db.Model):
    __tablename__ = 'Nivel'
    __table_args__ = {'schema': 'dbo'}
    nivel_id = db.Column(db.Integer, primary_key=True)
    nombre_nivel = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.String(255))
    orden_nivel = db.Column(db.Integer, nullable=False)

class Usuario(db.Model):
    __tablename__ = 'Usuario'
    __table_args__ = {'schema': 'dbo'}
    usuario_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password_hash = db.Column(db.String(255), nullable=False)
    rol = db.Column(db.String(30), nullable=False)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    email = db.Column('email', db.String(100))
    activo = db.Column(db.Boolean, default=True)
