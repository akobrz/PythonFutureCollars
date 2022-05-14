STR_API_ERROR = "Błąd API"
STR_DB_ERROR = "Błąd DB"

g = (i for i in range(1, 10000))

CRM_EXCEPTION = next(g)
EXCEPT_ACCOUNT = next(g)
EXCEPT_API = next(g)
EXCEPT_API_TIMEOUT = next(g)
EXCEPT_API_406 = next(g)
EXCEPT_APPROVAL = next(g)
EXCEPT_APPROVAL_BLOCK = next(g)
EXCEPT_BAD_ADDRESS = next(g)
EXCEPT_BILL = next(g)
EXCEPT_CHECKBOX_DISABLED = next(g)
EXCEPT_CLOSE_REQUEST = next(g)
EXCEPT_CONFIG_1 = next(g)
EXCEPT_CONFIG_2 = next(g)
EXCEPT_CONFIG_3 = next(g)
EXCEPT_CONFIG_3_V = next(g)
EXCEPT_CONFIG_4 = next(g)
EXCEPT_CONFIG_5 = next(g)
EXCEPT_CONFIG_6 = next(g)
EXCEPT_CONF_SAVE = next(g)
EXCEPT_CONSENT_VERIFI = next(g)
EXCEPT_CREATE_EDF = next(g)
EXCEPT_CUSTOMER = next(g)
EXCEPT_CUSTOMER_NOT_FOUND = next(g)
EXCEPT_DELIVERY = next(g)
EXCEPT_DOCUMENTS = next(g)
EXCEPT_DOCUMENTS_MISSING = next(g)
EXCEPT_DOCUMENT_ARCH = next(g)
EXCEPT_EMAIL = next(g)
EXCEPT_INV = next(g)
EXCEPT_INV_CANCELLED = next(g)
EXCEPT_INV_WRONG_TEL = next(g)
EXCEPT_LOGIN_ALERT_NOT_FOUND = next(g)
EXCEPT_LOGIN_CRMF = next(g)
EXCEPT_PHONE = next(g)
EXCEPT_PRECONFIG = next(g)
EXCEPT_PRECONFIG_NO_ADDRESS = next(g)
EXCEPT_PRECONFIG_NO_PARTNER = next(g)
EXCEPT_PRECONFIG_NO_SALON = next(g)
EXCEPT_RADIOBOX_DISABLED = next(g)
EXCEPT_TIMEOUT = next(g)
EXCEPT_VERIFI = next(g)
EXCEPT_VERIFI_MANY_NEO = next(g)
EXCEPT_VERIFI_NEGATIVE = next(g)
EXCEPT_VERIFI_NO_NEO = next(g)
EXCEPT_VERIFI_TIMEOUT = next(g)
EXCEPT_WRONG_STATUS = next(g)
KWM_EXCEPTION = next(g)
KWM_ID_NOT_FOUND = next(g)


OTHER_EXCEPTION = next(g)


d = {
    CRM_EXCEPTION : ("WARNING, CRMF unknown exception", "Błąd aplikacji CRMF"),
    EXCEPT_ACCOUNT : ("WARNING, problem during account creation", "Błąd zakładania rachunku"),
    EXCEPT_API : ("WARNING, problem with API", "Błąd komunikacji API"),
    EXCEPT_API_TIMEOUT : ("WARNING, api timeout", "Błąd komunikacji API"),
    EXCEPT_API_406 : ("WARNING, api 406", "Zajęty rekord"),
    EXCEPT_APPROVAL : ("WARNING, problem with approval", "Błąd zatwierdzania zamówienia"),
    EXCEPT_APPROVAL_BLOCK : ("WARNING, problem with approval - blocked", "Blokada zamówienia"),
    EXCEPT_CONSENT_VERIFI : ("WARNING, problem during consents verification", "Błąd weryfikacji zgód"),
    EXCEPT_BAD_ADDRESS : ("WARNING, problem with incorrect address", "Niezgodność adresu"),
    EXCEPT_BILL : ("WARNING, problem during bill account verification", "Błąd weryfikacji rachunku"),
    EXCEPT_CHECKBOX_DISABLED : ("WARNING, checkbox disabled", "Ogólny błąd procesu"),
    EXCEPT_CLOSE_REQUEST : ("WARNING, problem during closing request", "Błąd zamykania projektu"),
    EXCEPT_CONFIG_1 : ("WARNING, problem during configuration step 1", "Błąd konfiguracji etap 1/6"),
    EXCEPT_CONFIG_2 : ("WARNING, problem during configuration step 2", "Błąd konfiguracji etap 2/6"),
    EXCEPT_CONFIG_3 : ("WARNING, problem during configuration step 3", "Błąd konfiguracji etap 3/6"),
    EXCEPT_CONFIG_3_V : ("WARNING, problem during configuration voucher in step 3", "Błąd konfiguracji Vouchera"),
    EXCEPT_CONFIG_4 : ("WARNING, problem during configuration step 4", "Błąd konfiguracji etap 4/6"),
    EXCEPT_CONFIG_5 : ("WARNING, problem during configuration step 5", "Błąd konfiguracji etap 5/6"),
    EXCEPT_CONFIG_6 : ("WARNING, problem during configuration step 6", "Błąd konfiguracji etap 6/6"),
    EXCEPT_CONF_SAVE : ("WARNING, problem during configuration saving", "Błąd zapisu konfiguracji"),
    EXCEPT_CREATE_EDF : ("WARNING, problem during EDF creation", "Błąd zmiany formy faktury"),
    EXCEPT_CUSTOMER : ("WARNING, problem during customer search", "Błąd wyszukania Klienta"),
    EXCEPT_CUSTOMER_NOT_FOUND : ("WARNING, client not located", "Błąd wyszukania Klienta"),
    EXCEPT_DELIVERY : ("WARNING, problem during selection of delivery type", "Błąd metody dostarczania"),
    EXCEPT_DOCUMENTS : ("WARNING, problem during documents generation", "Błąd generowania dokumentów"),
    EXCEPT_DOCUMENT_ARCH : ("WARNING, document has been archived", "Dokument zarchiwizowany"),
    EXCEPT_EMAIL : ("WARNING, problem dufing email verification", "Błąd weryfikacji emaila"),
    EXCEPT_INV : ("WARNING, problem during invoice search", "Błąd wyszukania TEL"),
    EXCEPT_INV_CANCELLED : ("WARNING, problem during invoice search", "Anulowany TEL"),
    EXCEPT_INV_WRONG_TEL : ("WARNING, problem during invoice search", "Nieprawidłowy TEL"),
    EXCEPT_LOGIN_ALERT_NOT_FOUND : ("WARNING, login alert not located", "Błąd logowania do CRM F"),
    EXCEPT_LOGIN_CRMF : ("WARNING, problem during login to CRMF", "Błąd logowania do CRM F"),
    EXCEPT_DOCUMENTS_MISSING : ("WARNING, not all attachments saved", "Błąd zapisu dokumentów"),
    EXCEPT_PHONE : ("WARNING, problem during phone verification", "Błąd weryfikacji telefonu"),
    EXCEPT_PRECONFIG : ("WARNING, problem during pre-configuration", "Błąd wstępnej konfiguracji"),
    EXCEPT_PRECONFIG_NO_PARTNER : ("WARNING, partner not found during pre-configuration", "Nie znaleziono przedstawiciela partnera"),
    EXCEPT_PRECONFIG_NO_SALON : ("WARNING, salon not found during pre-configuration", "Nie znaleziono salonu sprzedawcy"),
    EXCEPT_PRECONFIG_NO_ADDRESS : ("WARNING, problem during pre-configuration with address", "Niezgodność adresu"),
    EXCEPT_RADIOBOX_DISABLED : ("WARNING, radio box disabled", "Ogólny błąd procesu"),
    EXCEPT_TIMEOUT : ("WARNING, timeout exception", "Przekroczony czas operacji"),
    EXCEPT_VERIFI : ("WARNING, problem during verification", "Błąd weryfikacji"),
    EXCEPT_VERIFI_NEGATIVE : ("WARNING, negative verification", "Negatywna weryfikacja"),
    EXCEPT_VERIFI_MANY_NEO : ("WARNING, problem with too many neo during verification", "Klient posiada wiele NEO"),
    EXCEPT_VERIFI_NO_NEO : ("WARNING, no neo detected during verification", "Klient nie posiada NEO"),
    EXCEPT_VERIFI_TIMEOUT : ("WARNING, timeout verification", "Przekroczony czas weryfikacji"),
    EXCEPT_WRONG_STATUS : ("WARNING, problem with request status", "Nieprawidłowy status zamówienia"),
    KWM_EXCEPTION : ("WARNING, problem with KWM", "Błąd aplikacji KWM"),
    KWM_ID_NOT_FOUND : ("WARNING, reservation not found", "Brak poprawnego nr rezerwacji"),
    OTHER_EXCEPTION : ("", ""),
}

def getWarning(key):
    return d.get(key, ("WARNING, unknown exception", "Ogólny Błąd Procesu"))[0]

def getStatus(key):
    return d.get(key, ("WARNING, unknown exception", "Ogólny Błąd Procesu"))[1]