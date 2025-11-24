from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Optional, Length, Email

class CatequizadoForm(FlaskForm):
    nombre = StringField("Nombre", validators=[DataRequired(), Length(max=50)])
    apellido = StringField("Apellido", validators=[DataRequired(), Length(max=50)])
    fecha_nacimiento = DateField("Fecha de nacimiento", validators=[DataRequired()], format="%Y-%m-%d")
    sexo = SelectField("Sexo", choices=[('', '---'), ('M', 'M'), ('F', 'F')], validators=[Optional()])
    documento_identidad = StringField("Documento", validators=[Optional(), Length(max=20)])
    direccion = StringField("Dirección", validators=[Optional(), Length(max=150)])
    telefono = StringField("Teléfono", validators=[Optional(), Length(max=20)])
    email = StringField("Correo", validators=[Optional(), Email(), Length(max=100)])
    escolaridad = StringField("Escolaridad", validators=[Optional(), Length(max=50)])
    fecha_bautismo = DateField("Fecha bautismo", validators=[Optional()], format="%Y-%m-%d")
    observaciones = TextAreaField("Observaciones", validators=[Optional(), Length(max=255)])
    submit = SubmitField("Guardar")
