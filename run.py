from app import app
from DB import DB

DB.__init__(app)


print('app started')
@app.before_first_request
def create_table():
    print('db created')
    DB.create_all()