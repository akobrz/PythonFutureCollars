from projekt.application import db

class Criteria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(254), unique=False, nullable=True)
    district = db.Column(db.String(254), unique=False, nullable=True)
    price_min = db.Column(db.Integer, unique=False, nullable=True)
    price_max = db.Column(db.Integer, unique=False, nullable=True)
    area = db.Column(db.Integer, unique=False, nullable=True)

    def __repr__(self):
        return f"({self.id}, {self.city}, {self.district}, {self.price_min}, {self.price_max}, {self.area})"

def save(criteria):
    db.session.add(criteria)
    db.session.commit()

def load():
    return db.session.query(Criteria).first()

if __name__ == "__main__":
    # db.create_all()
    c = Criteria()
    c.price_min = 550000
    c.price_max = 850000
    save(c)
    pass