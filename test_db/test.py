from application import db

class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.String(254), unique=False, nullable=True)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def load_by_id(self, id):
        return db.session.filter(Test.id==id).first()

    def load_all(self):
        return db.session.query(Test).all()

if __name__ == "__main__":
    # db.create_all()
    # test = Test()
    # test.region = "ZGIERZ"
    # test.save()

    t = Test().load_all()

    print([x.region for x in t])
