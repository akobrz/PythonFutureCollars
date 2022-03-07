import sys
from accountant import Firma

def wykonaj(args):
    f = Firma('magazyn', args)
    f.odczytaj()
    f.magazynuj()
    f.drukuj()


if __name__ == "__main__":
    wykonaj(sys.argv[1:])