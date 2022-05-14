from projekt.hunter import xpaths, tools
from projekt.models import olx, criteria, offer


class Portal_Olx:

    def __init__(self):
        self.sel = tools.Sel()

    def open(self, page):
        self.sel.open(self.open_url(page))

    def close(self):
        self.sel.close()

    def open_url(self, page):
        self.crit = criteria.load()
        self.url = f"https://www.olx.pl/nieruchomosci/domy/lodz/?search%5Bfilter_float_price%3Afrom%5D={self.crit.price_from}&search%5Bfilter_float_price%3Ato%5D={self.crit.price_to}&search%5Bfilter_float_m%3Afrom%5D=90&page={page}"
        return self.url

    def load_page(self, page):
        self.open(page)
        self.sel.locate_and_click_xpath_repeater(xpaths.olx_akceptuj, 0)

        if self.sel.locate_and_count_repeater(xpaths.olx_wrap1) > 0:
            o = offer.Offer().load_all()
            wraps1_ref = self.sel.locate_and_get_xpaths_repeater(xpaths.olx_wrap1_ref)
            wraps1_img = self.sel.locate_and_get_xpaths_repeater(xpaths.olx_wrap1_img)
            wraps1_price = self.sel.locate_and_get_xpaths_repeater(xpaths.olx_wrap1_price)
            wraps1 = zip(wraps1_ref, wraps1_img, wraps1_price)

            for w in wraps1:
                record = olx.Olx(None, None, None, None, w[2].text, w[0].get_attribute("href"), w[1].get_attribute("src"), w[1].get_attribute("alt"))
                if not record.is_in_db():
                    print(record)
                    offer.Offer().save(record.transfer_to_offer())

                # print(w[0].get_attribute("href"), w[1].get_attribute("src"), w[1].get_attribute("alt"), w[2].text)
                # x = w.findElement(By.XPATH, "//td[@class='offer']/div/table/tbody/tr[1]/td[1]/a/img")
                # print(w.findElement(by=By.XPATH, value=xpaths.olx_wrap1_ref).getAttribute("href"))
                # print(self.sel.locate_and_get_attribute_repeater(xpaths.olx_wrap1_img, "src"))
                # print(self.sel.locate_and_get_attribute_repeater(xpaths.olx_wrap1_img, "alt"))
                # print(self.sel.locate_and_get_text_repeater(xpaths.olx_wrap1_price))

        wrap2_no = self.sel.locate_and_count_repeater(xpaths.olx_wrap2)
        # wraps2 = self.sel.locate_and_get_xpaths_repeater(xpaths.olx_wrap2)

        # for w in wraps2:
        #     j = json.loads(w.get_attribute("data-features"))
        #     print(j.get("ad_id"), j.get("ad_price"), j.get("region_name"), j.get("city_name"), j.get("district_name"))

        # sel.send_text_and_check_repeater(xpaths.olx_cena_od, "650000 zł", 0)
        self.close()

if __name__ == "__main__":
    olx = olx.Olx(0, "", "", "", "900 000 zł", "", "", "test")
    print(olx.price)
