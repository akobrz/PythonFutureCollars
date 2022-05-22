import json
from projekt.services import xpaths, tools
from projekt.models import offer_dto, criteria, offer

class Portal_otodom:

    def __init__(self):
        self.sel = tools.Sel()

    def open(self, page, target):
        self.sel.open(self.open_url(page, target))

    def close(self):
        self.sel.close()

    def open_url(self, page, target):
        self.crit = criteria.Criteria().load()
        self.url = f"https://www.otodom.pl/pl/oferty/sprzedaz/{target}/lodz?priceMin={self.crit.price_min}" \
                   f"&priceMax={self.crit.price_max}" \
                   f"&areaMin={self.crit.area}" \
                   f"&limit=100&page={page}"
        return self.url

    def load_number(self, target):
        self.open(1, target)
        self.sel.locate_and_click_xpath_repeater(xpaths.oto_akceptuj, 0)
        number = self.sel.locate_and_get_text_repeater(xpaths.oto_number)
        return int(number)

    def load_page(self, page, target):
        self.open(page, target)
        self.sel.locate_and_click_xpath_repeater(xpaths.oto_akceptuj, 0)

        if self.sel.locate_and_count_repeater(xpaths.oto_wrap1_ref) > 0:
            wraps1_ref = self.sel.locate_and_get_xpaths_repeater(xpaths.oto_wrap1_ref)
            wraps1_img = self.sel.locate_and_get_xpaths_repeater(xpaths.oto_wrap1_img)
            wraps1_price = self.sel.locate_and_get_xpaths_repeater(xpaths.oto_wrap1_price)
            wraps1 = zip(wraps1_ref, wraps1_img, wraps1_price)

            for w in wraps1:
                record = offer_dto.OfferDTO()
                record.ref = w[0].get_attribute("href")
                record.img = w[1].get_attribute("src")
                record.title = w[1].get_attribute("alt")
                record.price = w[2].text
                record.region = "lodzkie"
                record.city = "lodz"
                if record.is_in_db():
                    new_record = record.get_from_db()
                    new_record.set_last()
                    new_record.set_read()
                    new_record.to_offer().update()
                else:
                    record.to_offer().save()

        self.close()

    def load(self, target):
        number = self.load_number(target)
        if number > 0:
            pages = number // 100
            print(pages)
            for page in range(1, pages+1):
                self.load_page(page, target)

if __name__ == "__main__":
    oto = offer_dto.OfferDTO()
    oto.price = "900 000 zł"
    print(oto.price)