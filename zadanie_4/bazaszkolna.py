import sys
from tools import Blad, BladObsluga

class Klasa:
    def __init__(self):
        self.wychowawca = ""
        self.nauczyciele = []
        self.uczniowie = []

class Nauczyciel:
    def __init__(self, nazwa, przedmiot):
        self.nazwa = nazwa
        self.przedmiot = przedmiot

def odczytaj_tekst():
    return input().encode('windows-1250').decode('utf8').strip()

def odczytaj_liczbe():
    return int(input().encode('windows-1250').decode('utf8').strip())

@BladObsluga
def bazaszkolna(args):

    szkola = {}

    while True:
        typ = odczytaj_tekst()
        if typ == "wychowawca":
            wychowawca = odczytaj_tekst()
            while True:
                t = odczytaj_tekst()
                if t:
                    k = szkola.get(t, Klasa())
                    k.wychowawca = wychowawca
                    szkola[t] = k
                else:
                    break
        if typ == "nauczyciel":
            nauczyciel = odczytaj_tekst()
            przedmiot = odczytaj_tekst()
            while True:
                t = odczytaj_tekst()
                if t:
                    k = szkola.get(t, Klasa())
                    k.nauczyciele.append(Nauczyciel(nauczyciel, przedmiot))
                    szkola[t] = k
                else:
                    break
        if typ == "uczen":
            uczen = odczytaj_tekst()
            klasa = odczytaj_tekst()
            k = szkola.get(klasa, Klasa())
            k.uczniowie.append(uczen)
        if typ == "koniec":
            break

    if not len(args):
        Blad(1)

    phrase = args[0]

    if phrase in szkola.keys():
        print(szkola.get(phrase).wychowawca)
        for uczen in szkola.get(phrase).uczniowie:
            print(uczen)
    elif phrase in [k.wychowawca for k in szkola.values()]:
        for uczen in [uczen for klasa in szkola.values() for uczen in klasa.uczniowie if phrase == klasa.wychowawca]:
            print(uczen)
    elif phrase in [nauczyciel.nazwa for klasa in szkola.values() for nauczyciel in klasa.nauczyciele]:
        wychowawcy = []
        for wychowawca in [k.wychowawca for k in szkola.values() if phrase in [n.nazwa for n in k.nauczyciele]]:
            if wychowawca not in wychowawcy and len(wychowawca):
                print(wychowawca)
                wychowawcy.append(wychowawca)
    elif phrase in [uczen for klasa in szkola.values() for uczen in klasa.uczniowie]:
        for p, n in [(nauczyciel.przedmiot, nauczyciel.nazwa) for klasa in szkola.values()
                      for nauczyciel in klasa.nauczyciele if phrase in klasa.uczniowie]:
            print(f"{p}\n{n}")

if __name__ == "__main__":
    bazaszkolna(sys.argv[1:])

