STR_API_ERROR = "Błąd API"
STR_DB_ERROR = "Błąd DB"

g = (i for i in range(1, 10000))

EXCEPT_API = next(g)
EXCEPT_API_TIMEOUT = next(g)
EXCEPT_API_406 = next(g)
EXCEPT_TIMEOUT = next(g)
OTHER_EXCEPTION = next(g)

d = {
    EXCEPT_API : ("WARNING, problem with API", "Błąd komunikacji API"),
    EXCEPT_API_TIMEOUT : ("WARNING, api timeout", "Błąd komunikacji API"),
    EXCEPT_API_406 : ("WARNING, api 406", "Zajęty rekord"),
    EXCEPT_TIMEOUT : ("WARNING, timeout", "Timeout"),
    OTHER_EXCEPTION : ("", ""),
}

def getWarning(key):
    return d.get(key, ("WARNING, unknown exception", "Ogólny Błąd Procesu"))[0]

def getStatus(key):
    return d.get(key, ("WARNING, unknown exception", "Ogólny Błąd Procesu"))[1]