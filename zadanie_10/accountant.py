from tools import Blad

class Operacja:

    def __init__(self):
        self.typ = ""
        self.kwota = 0
        self.opis = ""
        self.produkt = ""
        self.cena = 0
        self.sztuk = 0

    def __repr__(self):
        return f"({self.typ}, {self.kwota}, {self.opis}, {self.produkt}, {self.cena}, {self.sztuk})"

class Manager:

    def __init__(self):
        self.actions = {}

    def assign(self, name):
        def decorate(func):
            self.actions[name] = func
        return decorate

    def execute(self, name, *args):
        if name not in self.actions:
            print("Action not defined")
        else:
            return self.actions[name](*args)

manager = Manager()

@manager.assign("odczytaj")
def odczytaj(file):
    operacje = []
    with open(file, 'r') as plik:
        while True:
            o = Operacja()
            o.typ = plik.readline().encode('windows-1250').decode('utf8').strip()
            if o.typ == "saldo":
                o.kwota = int(plik.readline())
                o.opis = plik.readline().encode('windows-1250').decode('utf8').strip()
                operacje.append(o)
            elif o.typ == "zakup" or o.typ == "sprzedaż":
                o.produkt = plik.readline().encode('windows-1250').decode('utf8').strip()
                o.cena = int(plik.readline())
                o.sztuk = int(plik.readline())
                operacje.append(o)
            else:
                break
    return operacje

@manager.assign("magazynuj")
def magazynuj(operacje):
    saldo = 0
    magazyn = {}
    for o in operacje:
        if o.typ == "saldo":
            saldo += o.kwota
        elif o.typ in ("zakup", "sprzedaż"):
            if o.cena < 0:
                raise Blad(4)
            if o.sztuk < 0:
                raise Blad(5)
            if o.typ == "zakup":
                saldo -= o.cena * o.sztuk
                if saldo < 0:
                    raise Blad(2)
                magazyn[o.produkt] = magazyn.get(o.produkt, 0) + o.sztuk
            elif o.typ == "sprzedaż":
                saldo += o.cena * o.sztuk
                magazyn[o.produkt] = magazyn.get(o.produkt, 0) - o.sztuk
                if magazyn[o.produkt] < 0:
                    raise Blad(3)
    return saldo, magazyn

@manager.assign("drukuj_konto")
def drukuj_konto(saldo):
    print(f"Saldo: {saldo}")

@manager.assign("drukuj_magazyn")
def drukuj_magazyn(magazyn, args):
    for m in [(k, v) for (k, v) in magazyn.items() if k in args]:
        print(f"{m[0]}: {m[1]}")

@manager.assign("drukuj_przeglad")
def drukuj_przeglad(operacje):
    for operacja in operacje:
        print(f"{operacja.typ}")
        if operacja.typ == "saldo":
            print(f"{operacja.kwota}\n{operacja.opis}")
        if operacja.typ in ("zakup", "sprzedaż"):
            print(f"{operacja.produkt}\n{operacja.cena}\n{operacja.sztuk}")
    print("stop")

@manager.assign("zapisz")
def zapisz(operacje, file):
    with open(file, 'w') as plik:
        for operacja in operacje:
            plik.write(f"{operacja.typ}\n".encode('utf8').decode('windows-1250'))
            if operacja.typ == "saldo":
                plik.write(f"{operacja.kwota}\n{operacja.opis}\n".encode('utf8').decode('windows-1250'))
            if operacja.typ in ("zakup", "sprzedaż"):
                plik.write(f"{operacja.produkt}\n{operacja.cena}\n{operacja.sztuk}\n".encode('utf8').decode('windows-1250'))
        plik.write("stop".encode('utf8').decode('windows-1250'))

@manager.assign("dodaj_saldo")
def dodaj_saldo(operacje, args):
    o = Operacja()
    o.typ = "saldo"
    o.kwota, o.opis = int(args[0]), args[1]
    operacje.append(o)
    return operacje

@manager.assign("dodaj_sprzedaz")
def dodaj_sprzedaz(operacje, args):
    o = Operacja()
    o.typ = "sprzedaż"
    o.produkt, o.cena, o.sztuk = args[0], int(args[1]), int(args[2])
    operacje.append(o)
    return operacje

@manager.assign("dodaj_kupno")
def dodaj_kupno(operacje, args):
    o = Operacja()
    o.typ = "zakup"
    o.produkt, o.cena, o.sztuk = args[0], int(args[1]), int(args[2])
    operacje.append(o)
    return operacje

if __name__ == "__main__":
    pass


