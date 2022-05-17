# Olx
olx_akceptuj = "//button[@id='onetrust-accept-btn-handler']"
olx_cena_od = "//li[@id='param_price']/div[2]/div[1]/a[1]/span[1]"
olx_cena_do = "//li[@id='param_price']/div[2]/div[2]/a[1]/span[1]"
olx_pages = "//ul[@data-testid='pagination-list']/li"
olx_offers = "//table[@summary='Ogłoszenie']"
olx_wrap1 = "//tr[@class='wrap' and @rel='']"
olx_wrap1_ref = olx_wrap1 + "/td/div/table/tbody/tr[1]/td[1]/a"
olx_wrap1_img = olx_wrap1 + "/td/div/table/tbody/tr[1]/td[1]/a/img"
olx_wrap1_price = olx_wrap1 + "/td/div/table/tbody/tr[1]/td[3]/div/p/strong"
olx_wrap2 = "//tr[@class='wrap' and @rel='external']"
olx_wrap2_ref = olx_wrap2 + "/td/div/table/tbody/tr[1]/td[1]/a"
olx_wrap2_img = olx_wrap2 + "/td/div/table/tbody/tr[1]/td[1]/a/img"

# Oto dom
oto_akceptuj = "//button[@id='onetrust-accept-btn-handler']"
# href
oto_wrap1_ref = "//a[@data-cy='listing-item-link']"
# src, alt
oto_wrap1_img = oto_wrap1_ref + "/aside/picture/img"
# text()
oto_wrap1_info = oto_wrap1_ref + "/article/p"
oto_wrap1_price = oto_wrap1_ref + "/article/div[2]/span[1]"
oto_wrap1_m2 = oto_wrap1_ref + "/article/div[2]/span[2]"
oto_wrap1_rooms = oto_wrap1_ref + "/article/div[2]/span[3]"
oto_wrap1_area = oto_wrap1_ref + "/article/div[2]/span[4]"