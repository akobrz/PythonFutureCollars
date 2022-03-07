import sys
from accountant import Firma

def wykonaj(args):
    f = Firma('saldo', args)
    f.odczytaj()
    f.argumenty()
    f.magazynuj()
    f.drukuj()
    f.zapisz()


if __name__ == "__main__":
    wykonaj(sys.argv[1:])