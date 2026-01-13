from flask import Blueprint

bp_dashboard = Blueprint("dashboard", __name__)

@bp_dashboard.route("/dashboard")
def dashboard():
    return "<h1>Dashboard en construcción</h1>"
