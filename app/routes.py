from flask import Blueprint, render_template, request, redirect, url_for, flash
from bson import ObjectId
from app import mongo

bp = Blueprint("main", __name__)


# =========================
#   HOME
# =========================
@bp.route("/")
def index():
    return render_template("index.html")


# =========================
#   CATEQUIZADOS (CRUD)
# =========================
@bp.route("/catequizados")
def catequizados_lista():
    data = list(mongo.db.catequizados.find())
    return render_template("catequizados/lista.html", data=data)

@bp.route("/catequizados/crear", methods=["GET", "POST"])
def catequizados_crear():
    if request.method == "POST":
        mongo.db.catequizados.insert_one({
            "nombre": request.form.get("nombre"),
            "apellido": request.form.get("apellido"),
            "grupo_id": request.form.get("grupo_id"),
            "documento_identidad": request.form.get("documento_identidad")
        })
        return redirect(url_for("main.catequizados_lista"))
    return render_template("catequizados/crear.html")

@bp.route("/catequizados/editar/<id>", methods=["GET", "POST"])
def catequizados_editar(id):
    c = mongo.db.catequizados.find_one({"_id": ObjectId(id)})
    if request.method == "POST":
        mongo.db.catequizados.update_one(
            {"_id": ObjectId(id)},
            {"$set": {
                "nombre": request.form.get("nombre"),
                "apellido": request.form.get("apellido"),
                "grupo_id": request.form.get("grupo_id"),
                "documento_identidad": request.form.get("documento_identidad")
            }}
        )
        return redirect(url_for("main.catequizados_lista"))
    return render_template("catequizados/editar.html", c=c)

@bp.route("/catequizados/eliminar/<id>")
def catequizados_eliminar(id):
    mongo.db.catequizados.delete_one({"_id": ObjectId(id)})
    return redirect(url_for("main.catequizados_lista"))


# =========================
#   CATEQUISTAS (CRUD)
# =========================
@bp.route("/catequistas")
def catequistas_lista():
    data = list(mongo.db.catequistas.find())
    return render_template("catequistas/lista.html", data=data)

@bp.route("/catequistas/crear", methods=["GET", "POST"])
def catequistas_crear():
    if request.method == "POST":
        mongo.db.catequistas.insert_one({
            "nombre": request.form.get("nombre"),
            "apellido": request.form.get("apellido"),
            "telefono": request.form.get("telefono"),
            "email": request.form.get("email"),
            "especialidad": request.form.get("especialidad")
        })
        return redirect(url_for("main.catequistas_lista"))
    return render_template("catequistas/crear.html")

@bp.route("/catequistas/editar/<id>", methods=["GET", "POST"])
def catequistas_editar(id):
    persona = mongo.db.catequistas.find_one({"_id": ObjectId(id)})
    if request.method == "POST":
        mongo.db.catequistas.update_one(
            {"_id": ObjectId(id)},
            {"$set": {
                "nombre": request.form.get("nombre"),
                "apellido": request.form.get("apellido"),
                "telefono": request.form.get("telefono"),
                "email": request.form.get("email"),
                "especialidad": request.form.get("especialidad")
            }}
        )
        return redirect(url_for("main.catequistas_lista"))
    return render_template("catequistas/editar.html", c=persona)

@bp.route("/catequistas/eliminar/<id>")
def catequistas_eliminar(id):
    mongo.db.catequistas.delete_one({"_id": ObjectId(id)})
    return redirect(url_for("main.catequistas_lista"))


# =========================
#   ACTIVIDADES (CRUD)
# =========================
@bp.route("/actividades")
def actividades_lista():
    data = list(mongo.db.actividades.find())
    return render_template("actividades/lista.html", data=data)

@bp.route("/actividades/crear", methods=["GET", "POST"])
def actividades_crear():
    if request.method == "POST":
        mongo.db.actividades.insert_one({
            "titulo": request.form.get("titulo"),
            "descripcion": request.form.get("descripcion"),
            "fecha": request.form.get("fecha")
        })
        return redirect(url_for("main.actividades_lista"))
    return render_template("actividades/crear.html")

@bp.route("/actividades/editar/<id>", methods=["GET", "POST"])
def actividades_editar(id):
    a = mongo.db.actividades.find_one({"_id": ObjectId(id)})
    if request.method == "POST":
        mongo.db.actividades.update_one(
            {"_id": ObjectId(id)},
            {"$set": {
                "titulo": request.form.get("titulo"),
                "descripcion": request.form.get("descripcion"),
                "fecha": request.form.get("fecha")
            }}
        )
        return redirect(url_for("main.actividades_lista"))
    return render_template("actividades/editar.html", a=a)

@bp.route("/actividades/eliminar/<id>")
def actividades_eliminar(id):
    mongo.db.actividades.delete_one({"_id": ObjectId(id)})
    return redirect(url_for("main.actividades_lista"))


# =========================
#   ASISTENCIAS (CRUD)
# =========================
@bp.route("/asistencias")
def asistencias_lista():
    data = list(mongo.db.asistencias.find())
    return render_template("asistencias/lista.html", data=data)

@bp.route("/asistencias/crear", methods=["GET", "POST"])
def asistencias_crear():
    if request.method == "POST":
        mongo.db.asistencias.insert_one({
            "catequizado_id": request.form.get("catequizado_id"),
            "grupo_id": request.form.get("grupo_id"),
            "fecha": request.form.get("fecha"),
            "presente": bool(request.form.get("presente")),
            "marcado_por": request.form.get("marcado_por"),
            "dispositivo": request.form.get("dispositivo"),
            "comentario": request.form.get("comentario")
        })
        return redirect(url_for("main.asistencias_lista"))
    return render_template("asistencias/crear.html")

@bp.route("/asistencias/editar/<id>", methods=["GET", "POST"])
def asistencias_editar(id):
    a = mongo.db.asistencias.find_one({"_id": ObjectId(id)})
    if request.method == "POST":
        mongo.db.asistencias.update_one(
            {"_id": ObjectId(id)},
            {"$set": {
                "catequizado_id": request.form.get("catequizado_id"),
                "grupo_id": request.form.get("grupo_id"),
                "fecha": request.form.get("fecha"),
                "presente": bool(request.form.get("presente")),
                "marcado_por": request.form.get("marcado_por"),
                "dispositivo": request.form.get("dispositivo"),
                "comentario": request.form.get("comentario")
            }}
        )
        return redirect(url_for("main.asistencias_lista"))
    return render_template("asistencias/editar.html", a=a)

@bp.route("/asistencias/eliminar/<id>")
def asistencias_eliminar(id):
    mongo.db.asistencias.delete_one({"_id": ObjectId(id)})
    return redirect(url_for("main.asistencias_lista"))


# =========================
#   EVALUACIONES (CRUD)
# =========================
@bp.route("/evaluaciones")
def evaluaciones_lista():
    data = list(mongo.db.evaluaciones.find())
    return render_template("evaluaciones/lista.html", data=data)

@bp.route("/evaluaciones/crear", methods=["GET", "POST"])
def evaluaciones_crear():
    if request.method == "POST":
        mongo.db.evaluaciones.insert_one({
            "catequizado_id": request.form.get("catequizado_id"),
            "actividad_id": request.form.get("actividad_id"),
            "fecha": request.form.get("fecha"),
            "calificacion": request.form.get("calificacion"),
            "observaciones": request.form.get("observaciones")
        })
        return redirect(url_for("main.evaluaciones_lista"))
    return render_template("evaluaciones/crear.html")

@bp.route("/evaluaciones/editar/<id>", methods=["GET", "POST"])
def evaluaciones_editar(id):
    e = mongo.db.evaluaciones.find_one({"_id": ObjectId(id)})
    if request.method == "POST":
        mongo.db.evaluaciones.update_one(
            {"_id": ObjectId(id)},
            {"$set": {
                "catequizado_id": request.form.get("catequizado_id"),
                "actividad_id": request.form.get("actividad_id"),
                "fecha": request.form.get("fecha"),
                "calificacion": request.form.get("calificacion"),
                "observaciones": request.form.get("observaciones")
            }}
        )
        return redirect(url_for("main.evaluaciones_lista"))
    return render_template("evaluaciones/editar.html", e=e)

@bp.route("/evaluaciones/eliminar/<id>")
def evaluaciones_eliminar(id):
    mongo.db.evaluaciones.delete_one({"_id": ObjectId(id)})
    return redirect(url_for("main.evaluaciones_lista"))


# =========================
#   GRUPOS (CRUD)
# =========================
@bp.route("/grupos")
def grupos_lista():
    data = list(mongo.db.grupos.find())
    return render_template("grupos/lista.html", data=data)

@bp.route("/grupos/crear", methods=["GET", "POST"])
def grupos_crear():
    if request.method == "POST":
        mongo.db.grupos.insert_one({
            "nombre_grupo": request.form.get("nombre_grupo"),
            "nivel_id": request.form.get("nivel_id"),
            "catequista_principal": request.form.get("catequista_principal"),
            "horario": request.form.get("horario"),
            "periodo": request.form.get("periodo"),
            "capacidad": request.form.get("capacidad")
        })
        return redirect(url_for("main.grupos_lista"))
    return render_template("grupos/crear.html")

@bp.route("/grupos/editar/<id>", methods=["GET", "POST"])
def grupos_editar(id):
    g = mongo.db.grupos.find_one({"_id": ObjectId(id)})
    if request.method == "POST":
        mongo.db.grupos.update_one(
            {"_id": ObjectId(id)},
            {"$set": {
                "nombre_grupo": request.form.get("nombre_grupo"),
                "nivel_id": request.form.get("nivel_id"),
                "catequista_principal": request.form.get("catequista_principal"),
                "horario": request.form.get("horario"),
                "periodo": request.form.get("periodo"),
                "capacidad": request.form.get("capacidad")
            }}
        )
        return redirect(url_for("main.grupos_lista"))
    return render_template("grupos/editar.html", g=g)

@bp.route("/grupos/eliminar/<id>")
def grupos_eliminar(id):
    mongo.db.grupos.delete_one({"_id": ObjectId(id)})
    return redirect(url_for("main.grupos_lista"))


# =========================
#   INSCRIPCIONES (CRUD)
# =========================
@bp.route("/inscripciones")
def inscripciones_lista():
    data = list(mongo.db.inscripciones.find())
    return render_template("inscripciones/lista.html", data=data)

@bp.route("/inscripciones/crear", methods=["GET", "POST"])
def inscripciones_crear():
    if request.method == "POST":
        mongo.db.inscripciones.insert_one({
            "catequizado_id": request.form.get("catequizado_id"),
            "grupo_id": request.form.get("grupo_id"),
            "fecha_inscripcion": request.form.get("fecha_inscripcion"),
            "estado": request.form.get("estado"),
            "aprobado": request.form.get("aprobado") == "true"
        })
        return redirect(url_for("main.inscripciones_lista"))
    return render_template("inscripciones/crear.html")

@bp.route("/inscripciones/editar/<id>", methods=["GET", "POST"])
def inscripciones_editar(id):
    insc = mongo.db.inscripciones.find_one({"_id": ObjectId(id)})
    if request.method == "POST":
        mongo.db.inscripciones.update_one(
            {"_id": ObjectId(id)},
            {"$set": {
                "catequizado_id": request.form.get("catequizado_id"),
                "grupo_id": request.form.get("grupo_id"),
                "fecha_inscripcion": request.form.get("fecha_inscripcion"),
                "estado": request.form.get("estado"),
                "aprobado": request.form.get("aprobado") == "true"
            }}
        )
        return redirect(url_for("main.inscripciones_lista"))
    return render_template("inscripciones/editar.html", i=insc)

@bp.route("/inscripciones/eliminar/<id>")
def inscripciones_eliminar(id):
    mongo.db.inscripciones.delete_one({"_id": ObjectId(id)})
    return redirect(url_for("main.inscripciones_lista"))


# =========================
#   NIVELES (CRUD)
# =========================
@bp.route("/niveles")
def niveles_lista():
    data = list(mongo.db.niveles.find())
    return render_template("niveles/lista.html", data=data)

@bp.route("/niveles/crear", methods=["GET", "POST"])
def niveles_crear():
    if request.method == "POST":
        mongo.db.niveles.insert_one({
            "nombre_nivel": request.form.get("nombre_nivel"),
            "descripcion": request.form.get("descripcion"),
            "orden_nivel": request.form.get("orden_nivel")
        })
        return redirect(url_for("main.niveles_lista"))
    return render_template("niveles/crear.html")

@bp.route("/niveles/editar/<id>", methods=["GET", "POST"])
def niveles_editar(id):
    n = mongo.db.niveles.find_one({"_id": ObjectId(id)})
    if request.method == "POST":
        mongo.db.niveles.update_one(
            {"_id": ObjectId(id)},
            {"$set": {
                "nombre_nivel": request.form.get("nombre_nivel"),
                "descripcion": request.form.get("descripcion"),
                "orden_nivel": request.form.get("orden_nivel")
            }}
        )
        return redirect(url_for("main.niveles_lista"))
    return render_template("niveles/editar.html", n=n)

@bp.route("/niveles/eliminar/<id>")
def niveles_eliminar(id):
    mongo.db.niveles.delete_one({"_id": ObjectId(id)})
    return redirect(url_for("main.niveles_lista"))


# =========================
#   REPRESENTANTES (CRUD)
# =========================
@bp.route("/representantes")
def representantes_lista():
    data = list(mongo.db.representantes.find())
    return render_template("representantes/lista.html", data=data)

@bp.route("/representantes/crear", methods=["GET", "POST"])
def representantes_crear():
    if request.method == "POST":
        mongo.db.representantes.insert_one({
            "catequizado_id": request.form.get("catequizado_id"),
            "nombre": request.form.get("nombre"),
            "apellido": request.form.get("apellido"),
            "parentesco": request.form.get("parentesco"),
            "documento_identidad": request.form.get("documento_identidad"),
            "telefono": request.form.get("telefono"),
            "email": request.form.get("email"),
            "direccion": request.form.get("direccion")
        })
        return redirect(url_for("main.representantes_lista"))
    return render_template("representantes/crear.html")

@bp.route("/representantes/editar/<id>", methods=["GET", "POST"])
def representantes_editar(id):
    r = mongo.db.representantes.find_one({"_id": ObjectId(id)})
    if request.method == "POST":
        mongo.db.representantes.update_one(
            {"_id": ObjectId(id)},
            {"$set": {
                "catequizado_id": request.form.get("catequizado_id"),
                "nombre": request.form.get("nombre"),
                "apellido": request.form.get("apellido"),
                "parentesco": request.form.get("parentesco"),
                "documento_identidad": request.form.get("documento_identidad"),
                "telefono": request.form.get("telefono"),
                "email": request.form.get("email"),
                "direccion": request.form.get("direccion")
            }}
        )
        return redirect(url_for("main.representantes_lista"))
    return render_template("representantes/editar.html", r=r)

@bp.route("/representantes/eliminar/<id>")
def representantes_eliminar(id):
    mongo.db.representantes.delete_one({"_id": ObjectId(id)})
    return redirect(url_for("main.representantes_lista"))


# =========================
#   REGISTROS EVENTOS (CRUD)
# =========================
@bp.route("/registros_eventos")
def registros_eventos_lista():
    data = list(mongo.db.registros_eventos.find())
    return render_template("registros_eventos/lista.html", data=data)

@bp.route("/registros_eventos/editar/<id>", methods=["GET", "POST"])
def registros_eventos_editar(id):
    r = mongo.db.registros_eventos.find_one({"_id": ObjectId(id)})
    if request.method == "POST":
        mongo.db.registros_eventos.update_one(
            {"_id": ObjectId(id)},
            {"$set": {
                "usuario": request.form.get("usuario"),
                "accion": request.form.get("accion"),
                "descripcion": request.form.get("descripcion"),
                "fecha": request.form.get("fecha"),
                "ip": request.form.get("ip")
            }}
        )
        return redirect(url_for("main.registros_eventos_lista"))
    return render_template("registros_eventos/editar.html", r=r)

@bp.route("/registros_eventos/eliminar/<id>")
def registros_eventos_eliminar(id):
    mongo.db.registros_eventos.delete_one({"_id": ObjectId(id)})
    return redirect(url_for("main.registros_eventos_lista"))
