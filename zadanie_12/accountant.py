from tools import Blad
from manager import Manager
from baza import Operation, save, load

manager = Manager()

@manager.assign("odczytaj")
def odczytaj():
    return load()

@manager.assign("zapisz")
def zapisz(operacje):
    for operacja in operacje:
        save(operacja)

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

@manager.assign("dodaj_saldo")
def dodaj_saldo(operacje, args):
    o = Operation()
    o.typ = "saldo"
    o.kwota, o.opis = int(args[0]), args[1]
    operacje.append(o)
    return operacje

@manager.assign("dodaj_sprzedaz")
def dodaj_sprzedaz(operacje, args):
    o = Operation()
    o.typ = "sprzedaż"
    o.produkt, o.cena, o.sztuk = args[0], int(args[1]), int(args[2])
    o.kwota = o.cena * o.sztuk
    operacje.append(o)
    return operacje

@manager.assign("dodaj_kupno")
def dodaj_kupno(operacje, args):
    o = Operation()
    o.typ = "zakup"
    o.produkt, o.cena, o.sztuk = args[0], int(args[1]), int(args[2])
    o.kwota = -o.cena * o.sztuk
    operacje.append(o)
    return operacje

if __name__ == "__main__":
    pass


