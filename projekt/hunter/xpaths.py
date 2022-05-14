# Olx
olx_akceptuj = "//button[@id='onetrust-accept-btn-handler']"
olx_cena_od = "//li[@id='param_price']/div[2]/div[1]/a[1]/span[1]"
olx_cena_do = "//li[@id='param_price']/div[2]/div[2]/a[1]/span[1]"
olx_pages = "//ul[@data-testid='pagination-list']/li"
olx_offers = "//table[@summary='Ogłoszenie']"
olx_wrap1 = "//tr[@class='wrap' and @rel='']"
# href
olx_wrap1_ref = olx_wrap1 + "/td/div/table/tbody/tr[1]/td[1]/a"
# src, alt
olx_wrap1_img = olx_wrap1 + "/td/div/table/tbody/tr[1]/td[1]/a/img"
# text()
olx_wrap1_price = olx_wrap1 + "/td/div/table/tbody/tr[1]/td[3]/div/p/strong"
olx_wrap2 = "//tr[@class='wrap' and @rel='external']"