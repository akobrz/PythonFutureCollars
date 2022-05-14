from projekt.hunter import myjson
import os

# DB server and user
# DB_SERVER, DB_NAME, DB_USER, DB_PASSWORD = read_json("private\\db.private")
# CRM_USER_LOGIN, CRM_USER_PASSWORD = read_json("private\\crmf.private")
# KWM_USER_LOGIN, KWM_USER_PASSWORD = read_json("private\\kwm.private")

DB_SERVER, DB_NAME, DB_USER, DB_PASSWORD = myjson.read_json("private\\db.json")
# CRM_USER_LOGIN, CRM_USER_PASSWORD = read_json("private\\crmf.private")
# KWM_USER_LOGIN, KWM_USER_PASSWORD = read_json("private\\kwm.private")

OS_USERNAME = os.getlogin()
DOWNLOAD_DIRECTORY = f"C:\\Users\\{OS_USERNAME}\\Downloads\\"

API_RESPONSE_200 = 200
API_RESPONSE_204 = 204
API_RESPONSE_406 = 406

WAIT_ITER_3 = 3
WAIT_MIN_10 = 600
WAIT_MIN_20 = 1200
WAIT_MIN_30 = 1800
WAIT_SEC_1 = 1
WAIT_SEC_10 = 10
WAIT_SEC_120 = 120
WAIT_SEC_180 = 180
WAIT_SEC_2 = 2
WAIT_SEC_30 = 30
WAIT_SEC_5 = 5
WAIT_SEC_60 = 60

STATUS_ZAPARKOWANO = 'Zaparkowano'
STATUS_PODPISANA = "Podpisana"
STATUS_ODRZUCONE = 'odrzucone'
STATUS_UMOWA = 'umowa do podpisu'
STATUS_PARKOWANIE = 'Zaparkowano'
STATUS_ZWROT = 'zwrot do poprawy'
STATUS_WPROWADZONE = 'wprowadzone'
STATUS_MANUAL = "Manual"
STATUS_ANULOWANE = 'Anulowane'
STATUS_PRZEKAZANO = 'Przekazano do robota'
STATUS_NOWE_KONTO = 'Nowe konto'

DECYZJA_ODRZUCONE = 'odrzucone'
DECYZJA_UMOWA = 'dokumenty do podpisu'
DECYZJA_PARKOWANIE = 'zaparkowane'
DECYZJA_ZWROT = 'zwrot do poprawy'
DECYZJA_WPROWADZONE = 'wprowadzone'
DECYZJA_ANULOWANE = 'anulowane'
DECYZJA_MANUAL = 'manual'

WERYFIKACJA_POZYTYWNA = 'Pozytywny'
WERYFIKACJA_NEGATYWNA = 'Negatywny'
WERYFIKACJA_NIEUDANA = 'Nieudana'
WERYFIKACJA_WARUNKOWA = 'Warunkowo pozytywny'
WERYFIKACJA_TIMEOUT = 'Czas przekroczony'
WERYFIKACJA_ZADLUZENIE = 'Zadluzenie'
WERYFIKACJA_ZAMOWIENIE = 'Zamowienie'

ZALACZNIKI_1P_NOWA_TAB = ("RODO_Obowiazek_Informacyjny", "Neostrada_Umowa", "Neostrada_Podsumowanie")
ZALACZNIKI_1P_NOWA_PDF = ("obowiazek_informacyjny.pdf", "umowa.pdf", "wyciag.pdf")
ZALACZNIKI_1P_NOWA_TXT = ("obowiazek_informacyjny.txt", "umowa.txt", "wyciag.txt")

ZALACZNIKI_1P_MIG_TAB = ("Neostrada_Podsumowanie", "Neostrada_Aneks")
ZALACZNIKI_1P_MIG_PDF = ("neostrada_podsumowanie.pdf", "neostrada_aneks.pdf")
ZALACZNIKI_1P_MIG_TXT = ("neostrada_podsumowanie.txt", "neostrada_aneks.txt")

ZALACZNIKI_1P_BEZ_ZMIANY_TAB = ("Neostrada_Podsumowanie", "Neostrada_Aneks")
ZALACZNIKI_1P_BEZ_ZMIANY_PDF = ("neostrada_podsumowanie.pdf", "neostrada_aneks.pdf")
ZALACZNIKI_1P_BEZ_ZMIANY_TXT = ("neostrada_podsumowanie.txt", "neostrada_aneks.txt")

MIGRACJE = ['VIDPTN2RPT', 'VIDPTNABN6', 'VIDPTNEELS']

DOST_FAKTURY_EMAIL = "Na adres email Klienta"
DOST_FAKTURY_PORTAL = "Portal Orange"
DOST_FAKTURY_PAPIER = "Nie zamawia"
DOST_BRAK = "Brak"
DOST_PT = "Partner Techniczny"
DOST_SALON = "Osobisty"
DOST_KURIER = "Kurier"

CRM_ID_ROBOTA = "26625356"

TYP_REKORDU_MIGRACJA = "Migruję posiadaną usługę"

PROCES_NOWA = "Nowa aktywacja"
PROCES_MIGR_BEZ_ZMIANY = "Migracja w ramach obowiązującej lojalki bez zmiany technologii"
PROCES_MIGR_ZMIANA = "Migracja w ramach obowiązującej lojalki z zmianą technologii"
PROCES_UTRZYM_BEZ_ZMIANY = "Przedłużenie umowy bez zmiany technologii"
PROCES_UTRZYM_ZMIANA = "Przedłużenie umowy z zmianą technologii"
PROCES_ROZBUNDLOWIENIE = "Rozbundlowienie usług"

KONTO_AKTYWNE = "Konto aktywne"
KONTO_NIEAKTYWNE = "Konto nieaktywne"