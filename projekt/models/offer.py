from projekt.hunter.application import db

class Offer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.String(254), unique=False, nullable=True)
    city = db.Column(db.String(254), unique=False, nullable=True)
    district = db.Column(db.String(254), unique=False, nullable=True)
    price = db.Column(db.Integer, unique=False, nullable=True)
    ref = db.Column(db.String(1024), unique=False, nullable=True)
    img = db.Column(db.String(1024), unique=False, nullable=True)
    title = db.Column(db.String(254), unique=False, nullable=True)
    date = db.Column(db.TEXT, unique=False, nullable=True)
    read = db.Column(db.Integer, unique=False, nullable=True)

    def __repr__(self):
        return f"({self.id}, {self.city}, {self.district}, {self.price}, {self.title}, {self.date}, {self.read})"

    def save(self, offer):
        db.session.add(offer)
        db.session.commit()

    def load_all(self):
        return db.session.query(Offer).all()

if __name__ == "__main__":
    db.create_all()
    pass