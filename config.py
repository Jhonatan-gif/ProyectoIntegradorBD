class Config:
    SECRET_KEY = "dev-secret-change-me"
    # Windows Auth (trusted_connection)
    # Ajusta SERVER y DATABASE si no son localhost / ParroquiaDB
    SQLALCHEMY_DATABASE_URI = (
        "mssql+pyodbc://@localhost/ParroquiaDB"
        "?driver=ODBC+Driver+17+for+SQL+Server"
        "&trusted_connection=yes"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
