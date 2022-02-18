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

        return
    return wrapper
