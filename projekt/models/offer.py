from projekt.hunter.application import db

class Offer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.String(254), unique=False, nullable=True)
    city = db.Column(db.String(254), unique=False, nullable=True, default="")
    district = db.Column(db.String(254), unique=False, nullable=True)
    price = db.Column(db.Integer, unique=False, nullable=True, default=0)
    ref = db.Column(db.String(1024), unique=False, nullable=True)
    img = db.Column(db.String(1024), unique=False, nullable=True)
    title = db.Column(db.String(254), unique=False, nullable=True)
    date = db.Column(db.TEXT, unique=False, nullable=True)
    read = db.Column(db.Integer, unique=False, nullable=True, default=1)
    last = db.Column(db.TEXT, unique=False, nullable=True)
    active = db.Column(db.Integer, unique=False, nullable=True, default=True)

    def __repr__(self):
        return f"({self.id}, {self.city}, {self.district}, {self.price}, {self.title}, {self.date}, {self.read}, {self.last}, {self.active})"

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        m = db.session.query(Offer).filter(Offer.id==self.id).first()
        m.read = self.read
        m.last = self.last
        db.session.add(m)
        db.session.commit()

    def load_by_id(self, id):
        return db.session.filter(Offer.id==id).first()

    def load_all(self):
        return db.session.query(Offer).all()

if __name__ == "__main__":
    db.create_all()
    pass