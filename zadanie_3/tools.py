class Blad(Exception):
    def __init__(self, id):
        self.id = id

def BladObsluga(func):
    def wrapper(args):
        try:
            func(args)
        except ValueError:
            print("Błąd - niepoprawne dane")
        except Blad as e:
            if e.id == 1:
                print("Błąd - brak poprawnych argumentów")
            if e.id == 2:
                print("Błąd - saldo ujemne")
            if e.id == 3:
                print("Błąd - brak towaru")
            if e.id == 4:
                print("Błąd - cena ujemna")
            if e.id == 5:
                print("Błąd - ilość towaru ujemna")
        return
    return wrapper
