from DB import DB


class StoreModel(DB.Model):

    __tablename__ = 'stores'
    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(80))

    items = DB.relationship('ItemModel', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'item': [item.json() for item in self.items.all()]}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def insert(self):
        DB.session.add(self)
        DB.session.commit()

    def delete(self):
        DB.session.delete(self)
        DB.session.commit()

    @classmethod
    def delete_all(cls):
        try:
            DB.session.query(StoreModel).delete()
            DB.session.commit()
        except:
            DB.session.rollback()