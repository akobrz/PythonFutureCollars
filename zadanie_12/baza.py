from aplikacja import db

class Operation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    typ = db.Column(db.String(100), unique=False, nullable=False)
    kwota = db.Column(db.Integer, unique=False, nullable=True)
    opis = db.Column(db.String(1024), unique=False, nullable=True)
    produkt = db.Column(db.String(100), unique=False, nullable=True)
    cena = db.Column(db.Integer, unique=False, nullable=True)
    sztuk = db.Column(db.Integer, unique=False, nullable=True)

    def __repr__(self):
        return f"({self.id}, {self.typ}, {self.kwota}, {self.opis}, {self.produkt}, {self.cena}, {self.sztuk})"

def save(operation):
    db.session.add(operation)
    db.session.commit()

def load():
    return db.session.query(Operation).all()

if __name__ == "__main__":
    # db.create_all()
    pass