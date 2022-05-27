from projekt.application import db

class Offer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.String(254), unique=False, nullable=True)
    city = db.Column(db.String(254), unique=False, nullable=True, default="")
    district = db.Column(db.String(254), unique=False, nullable=True)
    price = db.Column(db.Integer, unique=False, nullable=True, default=0)
    ref = db.Column(db.String(1024), unique=False, nullable=True)
    img = db.Column(db.String(1024), unique=False, nullable=True)
    title = db.Column(db.String(254), unique=False, nullable=True)
    first = db.Column(db.TEXT, unique=False, nullable=True)
    read = db.Column(db.Integer, unique=False, nullable=True, default=1)
    last = db.Column(db.TEXT, unique=False, nullable=True)
    active = db.Column(db.Integer, unique=False, nullable=True, default=True)
    street = db.Column(db.String(254), unique=False, nullable=True)
    info = db.Column(db.String(2048), unique=False, nullable=True)
    area = db.Column(db.Integer, unique=False, nullable=True, default=0)

    def __repr__(self):
        return f"({self.id}, {self.city}, {self.district}, {self.price}, {self.title}, {self.first}, {self.read}, {self.last}, {self.active})"

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        m = db.session.query(Offer).filter(Offer.id==self.id).first()
        m.read = self.read
        m.last = self.last
        db.session.add(m)
        db.session.commit()

    def update_after_edit(self):
        m = db.session.query(Offer).filter(Offer.id==self.id).first()
        m.price = self.price
        m.area = self.area
        m.city = self.city
        m.district = self.district
        m.street = self.street
        m.info = self.info
        db.session.add(m)
        db.session.commit()

    def disable_by_id(self, id):
        m = db.session.query(Offer).filter(Offer.id==id).first()
        m.active = 0
        db.session.add(m)
        db.session.commit()

    def enable_by_id(self, id):
        m = db.session.query(Offer).filter(Offer.id==id).first()
        m.active = 1
        db.session.add(m)
        db.session.commit()

    def priority_by_id(self, id):
        m = db.session.query(Offer).filter(Offer.id==id).first()
        m.active = 2
        db.session.add(m)
        db.session.commit()

    def load_by_id(self, id):
        return db.session.query(Offer).filter(Offer.id==id).first()

    def load_all(self):
        return db.session.query(Offer).all()

    def load_priority_all(self):
        return db.session.query(Offer).filter(Offer.active==2).all()

    def load_active_all(self):
        return db.session.query(Offer).filter(Offer.active==1).all()

    def load_disabled_all(self):
        return db.session.query(Offer).filter(Offer.active==0).all()

    def __lt__(self, other):
        return int(self.price) < int(other.price)

if __name__ == "__main__":
    db.create_all()
    pass