import json
from projekt.services import xpaths, tools
from projekt.models import offer_dto, criteria, offer


class Portal_Olx:

    def __init__(self):
        self.sel = tools.Sel()

    def open(self, page):
        self.sel.open(self.open_url(page))

    def close(self):
        self.sel.close()

    def open_url(self, page):
        self.crit = criteria.Criteria().load()
        self.url = f"https://www.olx.pl/nieruchomosci/domy/lodz/?search%5Bfilter_float_price%3Afrom%5D={self.crit.price_min}" \
                   f"&search%5Bfilter_float_price%3Ato%5D={self.crit.price_max}" \
                   f"&search%5Bfilter_float_m%3Afrom%5D=90&page={page}"
        return self.url

    def load_page(self, page):
        self.open(page)
        self.sel.locate_and_click_xpath_repeater(xpaths.olx_akceptuj, 0)

        if self.sel.locate_and_count_repeater(xpaths.olx_wrap1) > 0:
            wraps1_ref = self.sel.locate_and_get_xpaths_repeater(xpaths.olx_wrap1_ref)
            wraps1_img = self.sel.locate_and_get_xpaths_repeater(xpaths.olx_wrap1_img)
            wraps1_price = self.sel.locate_and_get_xpaths_repeater(xpaths.olx_wrap1_price)
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

        if self.sel.locate_and_count_repeater(xpaths.olx_wrap2) > 0:
            wraps2_json = self.sel.locate_and_get_xpaths_repeater(xpaths.olx_wrap2)
            wraps2_ref = self.sel.locate_and_get_xpaths_repeater(xpaths.olx_wrap2_ref)
            wraps2_img = self.sel.locate_and_get_xpaths_repeater(xpaths.olx_wrap2_img)
            wraps2 = zip(wraps2_ref, wraps2_img, wraps2_json)

            for w in wraps2:
                record = offer_dto.OfferDTO()
                record.ref = w[0].get_attribute("href")
                record.img = w[1].get_attribute("src")
                record.title = w[1].get_attribute("alt")
                j = json.loads(w[2].get_attribute("data-features"))
                record.price = j.get("ad_price")
                record.region = j.get("region_name")
                record.city = j.get("city_name")
                record.district = j.get("district_name")

                if record.is_in_db():
                    new_record = record.get_from_db()
                    new_record.set_last()
                    new_record.set_read()
                    new_record.to_offer().update()
                else:
                    record.to_offer().save()

        self.close()

if __name__ == "__main__":
    olx = offer_dto.OfferDTO()
    olx.price = "900 000 zł"
    print(olx.price)
