from app import app
from DB import DB


DB.init_app(app)


@app.before_first_request
def create_table():
    DB.create_all()
