from DB import DB


class UserModel(DB.Model):

    __tablename__ = 'users'
    id = DB.Column(DB.Integer, primary_key=True)
    username = DB.Column(DB.String(80))
    password = DB.Column(DB.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def json(self):
        return {
            'id': self.id,
            'username': self.username,
        }

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, user_id):
        return cls.query.filter_by(id=user_id).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def add_to_db(self):
        DB.session.add(self)
        DB.session.commit()

    def delete(cls):
        DB.session.delete(cls)
        DB.session.commit()
