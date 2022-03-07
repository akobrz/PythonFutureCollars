from tools import Blad


class Firma:

    class Operacja:
        def __init__(self):
            self.typ = ""
            self.kwota = 0
            self.opis = ""
            self.produkt = ""
            self.cena = 0
            self.sztuk = 0


    def __init__(self, polecenie, args=None):
        self.saldo = 0
        self.magazyn = {}
        self.operacje = []
        self.plik = args[0]
        self.args = args[1:]
        self.polecenie = polecenie


    def drukuj(self):
        if self.polecenie == "konto":
            print(f"Saldo: {self.saldo}")
        if self.polecenie == "magazyn":
            for m in [(k, v) for (k, v) in self.magazyn.items() if k in self.args]:
                print(f"{m[0]}: {m[1]}")
        if self.polecenie == "przegląd":
            for operacja in self.operacje:
                print(f"{operacja.typ}")
                if operacja.typ == "saldo":
                    print(f"{operacja.kwota}\n{operacja.opis}")
                if operacja.typ in ("zakup", "sprzedaż"):
                    print(f"{operacja.produkt}\n{operacja.cena}\n{operacja.sztuk}")
            print("stop")


    def zapisz(self):
        with open(self.plik, 'w') as plik:
            for operacja in self.operacje:
                plik.write(f"{operacja.typ}\n".encode('utf8').decode('windows-1250'))
                if operacja.typ == "saldo":
                    plik.write(f"{operacja.kwota}\n{operacja.opis}\n".encode('utf8').decode('windows-1250'))
                if operacja.typ in ("zakup", "sprzedaż"):
                    plik.write(f"{operacja.produkt}\n{operacja.cena}\n{operacja.sztuk}\n".encode('utf8').decode('windows-1250'))
            plik.write("stop".encode('utf8').decode('windows-1250'))


    def odczytaj(self):
        with open(self.plik, 'r') as plik:
            while True:
                o = self.Operacja()
                o.typ = plik.readline().encode('windows-1250').decode('utf8').strip()
                if o.typ == "saldo":
                    o.kwota = int(plik.readline())
                    o.opis = plik.readline().encode('windows-1250').decode('utf8').strip()
                    self.operacje.append(o)
                elif o.typ == "zakup":
                    o.produkt = plik.readline().encode('windows-1250').decode('utf8').strip()
                    o.cena = int(plik.readline())
                    o.sztuk = int(plik.readline())
                    self.operacje.append(o)
                elif o.typ == "sprzedaż":
                    o.produkt = plik.readline().encode('windows-1250').decode('utf8').strip()
                    o.cena = int(plik.readline())
                    o.sztuk = int(plik.readline())
                    self.operacje.append(o)
                elif o.typ == "stop":
                    break
        self.magazynuj()


    def argumenty(self):
        if self.polecenie in ("saldo", "sprzedaż", "zakup"):
            o = self.Operacja()
            o.typ = self.polecenie
            if o.typ == "saldo":
                o.kwota, o.opis = int(self.args[0]), self.args[1]
            if o.typ in ("sprzedaż", "zakup"):
                o.produkt, o.cena, o.sztuk = self.args[0], int(self.args[1]), int(self.args[2])
            self.operacje.append(o)


    def magazynuj(self):
        for o in self.operacje:
            if o.typ == "saldo":
                self.saldo += o.kwota
            elif o.typ in ("zakup", "sprzedaż"):
                if o.cena < 0:
                    raise Blad(4)
                if o.sztuk < 0:
                    raise Blad(5)
                if o.typ == "zakup":
                    self.saldo -= o.cena * o.sztuk
                    if self.saldo < 0:
                        raise Blad(2)
                    self.magazyn[o.produkt] = self.magazyn.get(o.produkt, 0) + o.sztuk
                elif o.typ == "sprzedaż":
                    self.saldo += o.cena * o.sztuk
                    self.magazyn[o.produkt] = self.magazyn.get(o.produkt, 0) - o.sztuk
                    if self.magazyn[o.produkt] < 0:
                        raise Blad(3)


if __name__ == "__main__":
    pass


