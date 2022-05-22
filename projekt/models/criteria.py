from projekt.application import db
from projekt.services import variables

class Criteria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(254), unique=False, nullable=True)
    district = db.Column(db.String(254), unique=False, nullable=True)
    price_min = db.Column(db.Integer, unique=False, nullable=True)
    price_max = db.Column(db.Integer, unique=False, nullable=True)
    area = db.Column(db.Integer, unique=False, nullable=True)
    target = db.Column(db.String(10), unique=False, nullable=True)

    def __repr__(self):
        return f"({self.id}, {self.city}, {self.district}, {self.price_min}, {self.price_max}, {self.area}, {self.target})"

    def save(self):
        db.session.add(self)
        db.session.commit()

    def load(self, target):
        return db.session.query(Criteria).filter(Criteria.target==target).first()

    def update_after_edit(self, target):
        m = db.session.query(Criteria).filter(Criteria.target==target).first()
        m.price_min = self.price_min
        m.price_max = self.price_max
        m.area = self.area
        db.session.add(m)
        db.session.commit()

if __name__ == "__main__":
    db.create_all()
    h = Criteria()
    h.area = 110
    h.price_min = 600000
    h.price_max = 850000
    h.target = variables.TARGET_HOUSE
    h.save()
    f = Criteria()
    f.area = 75
    f.price_min = 500000
    f.price_max = 650000
    f.target = variables.TARGET_FLAT
    f.save()

    pass