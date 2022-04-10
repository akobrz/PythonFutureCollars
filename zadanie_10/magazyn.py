import sys
from accountant import manager

if __name__ == "__main__":
    o = manager.execute("odczytaj", sys.argv[1])
    _, m = manager.execute("magazynuj", o)
    manager.execute("drukuj_magazyn", m, sys.argv[2:])
