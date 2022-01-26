from shop.Jablka import Jablka
from shop.Ziemniaki import Ziemniaki
from shop.Zamowienia import Zamowienia
from shop.Zamowienia import wypisz_zamowienie
from shop.Produkt import Produkt
from shop.Produkt import wypisz_produkt




def run_homework():
    ciasteczka = Produkt(nazwa="Ciasteczka", kategoria="Jedzenie", cena=4)
    puste_zamowienie = Zamowienia(imie="Zbyszek", nazwisko="Cybulski")
    zamowienie = Zamowienia(imie="Zbyszek", nazwisko="Cybulski", lista_produktow=[ciasteczka, ciasteczka, ciasteczka])

    wypisz_zamowienie(puste_zamowienie)
    wypisz_zamowienie(zamowienie)


if __name__== '__main__':
    run_homework()

