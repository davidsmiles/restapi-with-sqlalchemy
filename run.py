from app import app
from DB import DB

DB.__init__(app)


@app.before_first_request
def create_table():
    DB.create_all()