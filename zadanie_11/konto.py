import sys
from accountant import manager

if __name__ == "__main__":
    o = manager.execute("odczytaj", sys.argv[1])
    s, _ = manager.execute("magazynuj", o)
    manager.execute("drukuj_konto", s)

