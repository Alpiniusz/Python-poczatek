from shop1.Zamowienia import generuj_zamowienie
from shop1.Zamowienia import Zamowienia


def run_homework():
    pierwsze_zamowienie = generuj_zamowienie()
    pierwsze_zamowienie.wypisz_zamowienie()
    drugie_zamowienie = generuj_zamowienie()
    drugie_zamowienie.wypisz_zamowienie()


if __name__ == '__main__':
    run_homework()