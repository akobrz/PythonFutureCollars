from projekt.models import criteria

crit = criteria.Criteria()

portal_olx_conf_path = f'https://www.olx.pl/nieruchomosci/domy/lodz/?search%5Bfilter_float_price%3Afrom%5D={crit.price_from}&search%5Bfilter_float_price%3Ato%5D={crit.price_to}&search%5Bfilter_float_m%3Afrom%5D=90'
portal_olx_page1 = f'https://www.olx.pl/nieruchomosci/domy/lodz/?search%5Bfilter_float_price%3Afrom%5D={crit.price_from}&search%5Bfilter_float_price%3Ato%5D={crit.price_to}&search%5Bfilter_float_m%3Afrom%5D=90&page=1'
portal_olx_page2 = f'https://www.olx.pl/nieruchomosci/domy/lodz/?search%5Bfilter_float_price%3Afrom%5D={crit.price_from}&search%5Bfilter_float_price%3Ato%5D={crit.price_to}&search%5Bfilter_float_m%3Afrom%5D=90&page=2'

WAIT_SEC_2 = 2
WAIT_SEC_120 = 120

districts = {
    295: "Polesie",
    297: "Widzew",
    301: "Bałuty",
    303: "Górna"
}