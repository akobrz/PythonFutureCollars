import sys

class Operacja:
    def __init__(self):
        self.kwota = 0
        self.opis = ""
        self.produkt = ""
        self.cena = 0
        self.sztuk = 0
        self.produkty = []
        self.typ = ""

class Firma:
    def __init__(self):
        self.saldo = 0
        self.magazyn = {}
        self.operacje = []

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
                print("Bład - brak towaru")
            if e.id == 4:
                print("Błąd - cena ujemna")
            if e.id == 5:
                print("Błąd - ilość towaru ujemna")
        return
    return wrapper

@BladObsluga
def accountant(args):

    f = Firma()

    while True:
        o = Operacja()
        o.typ = input().encode('windows-1250').decode('utf8')
        if o.typ in ("saldo", "sprzedaż", "zakup"):
            if o.typ == "saldo":
                o.kwota = int(input())
                o.opis = input().encode('windows-1250').decode('utf8')
            elif o.typ == "zakup":
                o.produkt = input().encode('windows-1250').decode('utf8')
                o.cena = int(input())
                o.sztuk = int(input())
            elif o.typ == "sprzedaż":
                o.produkt = input().encode('windows-1250').decode('utf8')
                o.cena = int(input())
                o.sztuk = int(input())
            f.operacje.append(o)
        elif o.typ in ("stop",):
            break
        else:
            break

    if args[0] in ("saldo", "sprzedaż", "zakup"):
        o = Operacja()
        o.typ = args[0]
        if o.typ == "saldo":
            o.kwota, o.opis = int(args[1]), args[2]
        if o.typ in ("sprzedaż", "zakup"):
            o.produkt, o.cena, o.sztuk = args[1], int(args[2]), int(args[3])
        f.operacje.append(o)

    for o in f.operacje:
        if o.typ == "saldo":
            f.saldo += o.kwota
        elif o.typ in ("zakup", "sprzedaż"):
            if o.kwota < 0:
                raise Blad(4)
            if o.sztuk < 0:
                raise Blad(5)
            if o.typ == "zakup":
                f.saldo -= o.kwota * o.sztuk
                if f.saldo < 0:
                    raise Blad(2)
                f.magazyn[o.produkt] = f.magazyn.get(o.produkt, 0) + o.sztuk
            elif o.typ == "sprzedaż":
                f.saldo += o.kwota * o.sztuk
                f.magazyn[o.produkt] = f.magazyn.get(o.produkt, 0) - o.sztuk
                if f.magazyn[o.produkt] < 0:
                    raise Blad(3)

    if args[0] in ("konto", "magazyn", "przegląd"):
        if args[0] == "konto":
            print(f"Saldo: {f.saldo}")
        if args[0] == "magazyn":
            for n, v in f.magazyn.items():
                if v > 0:
                    print(f"{n}: {v}")
        if args[0] == "przegląd":
            DrukujOperacje(f.operacje, int(args[1]), int(args[2]))
    else:
        DrukujOperacje(f.operacje)


def DrukujOperacje(operacje, min=0, max=sys.maxsize):
    for i, o in enumerate(operacje):
        if min <= i <= max:
            print(o.typ)
            if o.typ == "saldo":
                print(f"{o.kwota}\n{o.opis}")
            elif o.typ in ("zakup", "sprzedaż"):
                if o.typ in ("zakup", "sprzedaż"):
                    print(f"{o.produkt}\n{o.cena}\n{o.sztuk}")
    print("stop")




if __name__ == "__main__":
    accountant(sys.argv[1:])

