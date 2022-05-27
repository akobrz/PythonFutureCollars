from projekt.models import offer
from datetime import date, datetime

class OfferDTO:

    date_format = "%Y-%m-%d"

    def __init__(self):
        self.id = None
        self.region = ""
        self.city = ""
        self.district = ""
        self._price = 0
        self.ref = ""
        self.img = ""
        self.title = ""
        self._first = date.today()
        self._last = date.today()
        self._read = 1
        self._active = 1
        self.street = ""
        self.info = ""

    @property
    def first(self):
        return self._first

    @first.setter
    def first(self, f):
        self._first = f

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, p):
        if isinstance(p, str):
            self._price = int("0"+"".join([d for d in p if d.isdigit()]))
        else:
            self._price = p

    @property
    def active(self):
        return self._active

    @active.setter
    def active(self, a):
        self._active = a

    @property
    def last(self):
        return self._last

    @last.setter
    def last(self, l):
        self._last = l

    @property
    def read(self):
        return self._read

    @read.setter
    def read(self, r):
        self._read = r

    def set_last(self):
        self.last = datetime.today()

    def set_read(self):
        self.read = (self.last - self.first).days + 1

    def set_priority(self):
        self.active = 2

    def to_offer(self):
        o = offer.Offer()
        o.id = self.id
        o.region = self.region
        o.city = self.city
        o.district = self.district
        o.price = self.price
        o.ref = self.ref
        o.img = self.img
        o.title = self.title
        o.first = self.first.strftime(self.date_format)
        o.read = self.read
        o.last = self.last.strftime(self.date_format)
        o.active = self.active
        o.street = self.street
        o.info = self.info
        return o

    def from_offer(self, offer):
        record = OfferDTO()
        record.id = offer.id
        record.region = offer.region
        record.city = offer.city
        record.district = offer.district
        record.price = offer.price
        record.ref = offer.ref
        record.img = offer.img
        record.title = offer.title
        record.first = datetime.strptime(offer.first, self.date_format)
        record.read = offer.read
        record.last = datetime.strptime(offer.last, self.date_format)
        record.active = offer.active
        record.street = offer.street
        record.info = str(offer.info)
        return record

    def __eq__(self, other):
        return self.price == other.price and self.title == other.title

    def is_in_db(self):
        for o in offer.Offer().load_all():
            if self.from_offer(o) == self:
                return True
        return False

    def get_from_db(self):
        for o in offer.Offer().load_all():
            if self.from_offer(o) == self:
                return self.from_offer(o)
        return None




if __name__ == "__main__":
    olx = OfferDTO()
    olx.price = "900 000 zł"
    print(olx.price)
