class Paczka:
    def __init__(self):
        self.waga = 0

def obsluga_bledow(func):
    def wrapper():
        try:
            func()
        except ValueError:
            print("Błąd. Brak danych lub niepoprawne dane")
        except AttributeError:
            print("Błąd. Nieprawidłowa wartość parametru")
        return
    return wrapper


@obsluga_bledow
def wyslij_paczki():
    maks_waga_paczki = 20
    maks_liczba_paczek = float(input("Podaj ile paczek ma zostać wysłanych:"))

    if maks_liczba_paczek == 0:
        print("Nie wysłano żadnej paczki")
        return

    paczki = []

    while len(paczki) <= maks_liczba_paczek:
        element = float(input("Dodajesz element do paczki. Podaj jego wagę:"))
        if element > 10 or 1 > element > 0:
            raise AttributeError
        if len(paczki) == 0:
            paczki.append(Paczka())
        if element == 0 or paczki[-1].waga + element > maks_waga_paczki and len(paczki) == maks_liczba_paczek:
            break
        elif paczki[-1].waga + element > maks_waga_paczki and len(paczki) < maks_liczba_paczek:
            paczki.append(Paczka())
        paczki[-1].waga += element

    najbardziej_pusta_paczka_waga = sorted(paczki, key=lambda v: v.waga, reverse=True)[0].waga
    najbardziej_pusta_paczka_id = 0

    for i, v in enumerate(paczki):
        if v.waga < najbardziej_pusta_paczka_waga:
            najbardziej_pusta_paczka_id = i

    print(f"Wysłano {len(paczki)} paczek")
    print(f"Wysłano łącznie {sum(x.waga for x in paczki)} kilogramów")
    print(f"Wysłano łącznie {sum(maks_waga_paczki-x.waga for x in paczki)} pustych kilogramów")
    print(f"Paczka nr {najbardziej_pusta_paczka_id+1} miała najwięcej pustych kilogramów: {maks_waga_paczki - paczki[najbardziej_pusta_paczka_id].waga}")


if __name__ == "__main__":
    wyslij_paczki()
