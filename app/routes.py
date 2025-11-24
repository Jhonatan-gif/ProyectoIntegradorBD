from flask import Blueprint, render_template, redirect, url_for, flash, request
from .models import Catequizando
from .forms import CatequizadoForm
from . import db

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    q = request.args.get('q', '')
    if q:
        # búsqueda simple por nombre/apellido
        datos = Catequizando.query.filter(
            (Catequizando.nombre.ilike(f"%{q}%")) | (Catequizando.apellido.ilike(f"%{q}%"))
        ).order_by(Catequizando.fecha_inscripcion.desc()).all()
    else:
        datos = Catequizando.query.order_by(Catequizando.fecha_inscripcion.desc()).all()
    return render_template('index.html', datos=datos, q=q)

@bp.route('/crear', methods=['GET', 'POST'])
def crear():
    form = CatequizadoForm()
    if form.validate_on_submit():
        nuevo = Catequizando(
            nombre=form.nombre.data,
            apellido=form.apellido.data,
            fecha_nacimiento=form.fecha_nacimiento.data,
            sexo=form.sexo.data or None,
            documento_identidad=form.documento_identidad.data,
            direccion=form.direccion.data,
            telefono=form.telefono.data,
            email=form.email.data,
            escolaridad=form.escolaridad.data,
            fecha_bautismo=form.fecha_bautismo.data,
            observaciones=form.observaciones.data
        )
        db.session.add(nuevo)
        db.session.commit()
        flash("Catequizado creado.", "success")
        return redirect(url_for('main.index'))
    return render_template('crear.html', form=form)

@bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    obj = Catequizando.query.get_or_404(id)
    form = CatequizadoForm(obj=obj)
    if form.validate_on_submit():
        form.populate_obj(obj)
        db.session.commit()
        flash("Catequizado actualizado.", "success")
        return redirect(url_for('main.index'))
    return render_template('editar.html', form=form, obj=obj)

@bp.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    obj = Catequizando.query.get_or_404(id)
    db.session.delete(obj)
    db.session.commit()
    flash("Catequizado eliminado.", "info")
    return redirect(url_for('main.index'))
