from projekt.models import offer
from datetime import date

class Olx:

    def __init__(self, id, region, city, district, price, ref, img, title):
        self.id = id
        self.region = region
        self.city = city
        self.district = district
        self.price = int("".join([d for d in price if d.isdigit()]))
        self.ref = ref
        self.img = img
        self.title = title
        self.date = date.today().strftime("%Y-%m-%d")
        self.read = 0

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
        o.date = self.date
        o.read = self.read
        return o

    def transfer_from_offer(self, offer):
        record = Olx(None, "", "", "", "0", "", "", "")
        record.id = offer.id
        record.region = offer.region
        record.city = offer.city
        record.district = offer.district
        record.price = offer.price
        record.ref = offer.ref
        record.img = offer.img
        record.title = offer.title
        record.date = offer.date
        record.read = offer.read
        return record

    def __eq__(self, other):
        return self.price == other.price and self.title == other.title

    def is_in_db(self):
        for o in offer.Offer().load_all():
            if self.transfer_from_offer(o) == self:
                return True
        return False



if __name__ == "__main__":
    olx = Olx(0, "", "", "", "900 000 zł", "", "", "test")
    print(olx.price)
