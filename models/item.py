from DB import DB


class ItemModel(DB.Model):

    __tablename__ = 'items'
    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(80))
    price = DB.Column(DB.Float(precision=2))

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def json(self):
        return {
                'name': self.name,
                'price': self.price
            }

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def upsert(self):
        DB.session.add(self)
        DB.session.commit()

    def delete(self):
        DB.session.delete(self)
        DB.session.commit()