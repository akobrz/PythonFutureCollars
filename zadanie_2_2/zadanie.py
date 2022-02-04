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
def oblicz_collatza():
    min_dlugosc, maks_dlugosc, liczba = 0, 100, int(input("Podaj liczbę naturalną, większą od 0 i mniejszą od 100: "))
    if maks_dlugosc < liczba or liczba <= min_dlugosc:
        raise AttributeError
    print(f"Długość ciągu Collatza dla liczby {liczba} wynosi: {oblicz(liczba)}")


def oblicz(liczba, ilosc=1):
    if liczba == 1:
        return ilosc
    elif liczba % 2:
        return oblicz(3*liczba+1, ilosc+1)
    else:
        return oblicz(liczba/2, ilosc+1)


if __name__ == "__main__":
    oblicz_collatza()
