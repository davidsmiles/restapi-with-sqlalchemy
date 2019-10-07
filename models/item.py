from DB import DB


class ItemModel(DB.Model):

    __tablename__ = 'items'
    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(80))
    price = DB.Column(DB.Float(precision=2))

    store_name = DB.Column(DB.Integer, DB.ForeignKey('stores.name'))
    store = DB.relationship('StoreModel')

    def __init__(self, name, price, store_name):
        self.name = name
        self.price = price
        self.store_name = store_name

    def json(self):
        return {
                'id': self.id,
                'name': self.name,
                'price': self.price,
                'store_name': self.store_name
            }

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def upsert(self):
        DB.session.add(self)
        DB.session.commit()

    def delete(self):
        DB.session.delete(self)
        DB.session.commit()

    @classmethod
    def delete_all(cls):
        try:
            DB.session.query(ItemModel).delete()
            DB.session.commit()
        except:
            DB.session.rollback()
