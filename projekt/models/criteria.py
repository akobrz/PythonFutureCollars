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

    def save(self):
        db.session.add(self)
        db.session.commit()

    def load(self):
        return db.session.query(Criteria).first()

    def update_after_edit(self):
        m = db.session.query(Criteria).filter(Criteria.id==1).first()
        m.price_min = self.price_min
        m.price_max = self.price_max
        m.area = self.area
        db.session.add(m)
        db.session.commit()

if __name__ == "__main__":
    db.create_all()
    c = Criteria()
    c.area = 75
    c.price_min = 500000
    c.price_max = 900000
    c.save()
    pass