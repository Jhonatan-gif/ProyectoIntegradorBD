from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS
from .config import MONGO_URI

mongo = PyMongo()
cors = CORS()

def create_app():
    app = Flask(__name__)
    app.config["MONGO_URI"] = MONGO_URI

    mongo.init_app(app)
    cors.init_app(app)

    # IMPORTAR EL BLUEPRINT PRINCIPAL CORRECTO
    from app.routes import bp
    app.register_blueprint(bp)

    # Dashboard
    from app.dashboard_routes import bp_dashboard
    app.register_blueprint(bp_dashboard)

    # Exportación PDF
    from app.pdf_routes import bp_pdf
    app.register_blueprint(bp_pdf)

    return app
