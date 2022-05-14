from projekt.models import offer
from datetime import date, datetime

class Olx:

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
        self.date = date.today()
        self.last = date.today()
        self.read = 1
        self._active = 1

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, p):
        if isinstance(p, str):
            self._price = int("".join([d for d in p if d.isdigit()]))
        else:
            self._price = p

    @property
    def active(self):
        return bool(self._active)

    @active.setter
    def active(self, a):
        self._active = 1 if a else 0

    @property
    def last(self):
        return self._last

    @last.setter
    def last(self, l):
        self._last = l

    def set_last(self):
        self.last = datetime.today()

    def set_read(self):
        self.read = (self.last - self.date).days + 1

    def transfer_to_offer(self):
        o = offer.Offer()
        o.id = self.id
        o.region = self.region
        o.city = self.city
        o.district = self.district
        o.price = self.price
        o.ref = self.ref
        o.img = self.img
        o.title = self.title
        o.date = self.date.strftime(self.date_format)
        o.read = self.read
        o.last = self.last.strftime(self.date_format)
        o.active = self.active
        return o

    def transfer_from_offer(self, offer):
        record = Olx()
        record.id = offer.id
        record.region = offer.region
        record.city = offer.city
        record.district = offer.district
        record.price = offer.price
        record.ref = offer.ref
        record.img = offer.img
        record.title = offer.title
        record.date = datetime.strptime(offer.date, self.date_format)
        record.read = offer.read
        record.last = datetime.strptime(offer.last, self.date_format)
        record.active = offer.active
        return record

    def __eq__(self, other):
        return self.price == other.price and self.title == other.title

    def is_in_db(self):
        for o in offer.Offer().load_all():
            if self.transfer_from_offer(o) == self:
                return True
        return False

    def get_from_db(self):
        for o in offer.Offer().load_all():
            if self.transfer_from_offer(o) == self:
                return self.transfer_from_offer(o)
        return None


if __name__ == "__main__":
    olx = Olx()
    olx.price = "900 000 zł"
    print(olx.price)
