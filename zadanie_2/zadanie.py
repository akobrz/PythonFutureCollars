class Paczka:
    def __init__(self):
        self.id = 0
        self.waga = 0

def obsluga_bledow(func):
    def wrapper():
        try:
            func()
        except ValueError:
            print("Błąd. Brak danych lub niepoprawne dane")
        except AttributeError:
            print("Błąd. Nieprawidłowa wartość parametru")
        except RecursionError:
            print("Nie wysłano żadnej paczki")
        return
    return wrapper


@obsluga_bledow
def wyslij_paczki():
    maks_waga_paczki, maks_liczba_paczek = 20, float(input("Podaj ile paczek ma zostać wysłanych:"))

    paczki = []

    if maks_liczba_paczek == 0:
        raise RecursionError

    while len(paczki) <= maks_liczba_paczek:
        element = float(input("Dodajesz element do paczki. Podaj jego wagę:"))
        if element > 10 or 1 > element > 0:
            raise AttributeError
        if len(paczki) == 0 or paczki[-1].waga + element > maks_waga_paczki and len(paczki) < maks_liczba_paczek:
            paczki.append(Paczka())
        if element == 0 or paczki[-1].waga + element > maks_waga_paczki and len(paczki) == maks_liczba_paczek:
            break
        paczki[-1].waga += element

    for i, _ in enumerate(paczki):
        paczki[i].id = i+1

    najbardziej_pusta = sorted(paczki, key=lambda v: v.waga)[0]

    print(f"Wysłano {len(paczki)} paczek")
    print(f"Wysłano łącznie {sum(x.waga for x in paczki)} kilogramów")
    print(f"Wysłano łącznie {sum(maks_waga_paczki-x.waga for x in paczki)} pustych kilogramów")
    print(f"Paczka nr {najbardziej_pusta.id} miała najwięcej pustych kilogramów: {maks_waga_paczki - najbardziej_pusta.waga}")


if __name__ == "__main__":
    wyslij_paczki()
