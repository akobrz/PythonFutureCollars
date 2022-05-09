import sys
from accountant import manager

if __name__ == "__main__":
    o = manager.execute("odczytaj", sys.argv[1])
    manager.execute("drukuj_przeglad", o)