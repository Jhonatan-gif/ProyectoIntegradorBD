from flask import Blueprint

bp_pdf = Blueprint("pdf", __name__)

@bp_pdf.route("/reportes")
def reportes():
    return "<h1>Reportes PDF en construcción</h1>"
