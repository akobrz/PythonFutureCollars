from projekt.hunter.application import db

class Criteria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(254), unique=False, nullable=True)
    district = db.Column(db.String(254), unique=False, nullable=True)
    price_from = db.Column(db.Integer, unique=False, nullable=True)
    price_to = db.Column(db.Integer, unique=False, nullable=True)

    def __repr__(self):
        return f"({self.id}, {self.city}, {self.district}, {self.price_from}, {self.price_to})"

def save(criteria):
    db.session.add(criteria)
    db.session.commit()

def load():
    return db.session.query(Criteria).first()

if __name__ == "__main__":
    # db.create_all()
    c = Criteria()
    c.price_from = 550000
    c.price_to = 850000
    save(c)
    pass