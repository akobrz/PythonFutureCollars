
def error_handler(func):
    def wrapper():
        try:
            func()
        except ValueError:
            print("Brak danych lub niepoprawne dane")
        return
    return wrapper

@error_handler
def drukuj_oprocentowanie():

    print("Podaj początkową wysokość kredytu:")
    kredyt = float(input())
    print("Podaj oprocentowanie kredytu:")
    procent = float(input())
    print("Podaj kwotę raty miesięcznej:")
    rata = float(input())

    inflacja = (1.592824484, -0.453509101, 2.324671717, 1.261254407, 1.782526286, 2.329384541,
                1.502229842, 1.782526286, 2.328848994, 0.616921348, 2.352295886, 0.337779545,
                1.577035247, -0.292781443, 2.48619659, 0.267110318, 1.417952672, 1.054243267,
                1.480520104, 1.577035247, -0.07742069, 1.165733399, -0.404186718, 1.499708521)

    for i in inflacja:
        poprzedni = kredyt
        kredyt = (1+((i+procent)/1200))*kredyt-rata
        if kredyt <= 0:
            print("Twoja pozostała kwota kredytu to {:.6f}, to {:.6f} mniej niż w poprzednim miesiącu."
                  .format(0.0, poprzedni))
            break
        else:
            print("Twoja pozostała kwota kredytu to {:.6f}, to {:.6f} mniej niż w poprzednim miesiącu."
                  .format(kredyt, poprzedni-kredyt))

if __name__ == "__main__":
    drukuj_oprocentowanie()

