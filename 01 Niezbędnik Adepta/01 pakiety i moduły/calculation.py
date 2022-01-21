def kalkulacja (kwota, oprocentowanie, okres):
    wartosc = kwota * (1 + oprocentowanie / 100) ** okres
    return wartosc