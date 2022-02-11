from tools import Blad, BladObsluga
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


@BladObsluga
def accountant(args):

    f = Firma()

    while True:
        o = Operacja()
        o.typ = input().encode('windows-1250').decode('utf8').strip()
        if o.typ in ("saldo", "sprzedaż", "zakup"):
            if o.typ == "saldo":
                o.kwota = int(input())
                o.opis = input().encode('windows-1250').decode('utf8').strip()
            elif o.typ == "zakup":
                o.produkt = input().encode('windows-1250').decode('utf8').strip()
                o.cena = int(input())
                o.sztuk = int(input())
            elif o.typ == "sprzedaż":
                o.produkt = input().encode('windows-1250').decode('utf8').strip()
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
            if o.cena < 0:
                raise Blad(4)
            if o.sztuk < 0:
                raise Blad(5)
            if o.typ == "zakup":
                f.saldo -= o.cena * o.sztuk
                if f.saldo < 0:
                    raise Blad(2)
                f.magazyn[o.produkt] = f.magazyn.get(o.produkt, 0) + o.sztuk
            elif o.typ == "sprzedaż":
                f.saldo += o.cena * o.sztuk
                f.magazyn[o.produkt] = f.magazyn.get(o.produkt, 0) - o.sztuk
                if f.magazyn[o.produkt] < 0:
                    raise Blad(3)

    if args[0] in ("konto", "magazyn", "przegląd"):
        if args[0] == "konto":
            print(f"Saldo: {f.saldo}")
        if args[0] == "magazyn":
            for v in args[1:]:
                print(f"{v}: {f.magazyn.get(v, 0)}")
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

