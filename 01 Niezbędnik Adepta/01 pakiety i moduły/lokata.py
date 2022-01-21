kwota = float(input("podaj kwotę jaką chcesz wpłacić: "))
oprocentowanie = float(input("podaj oprocentowanie: "))
okres = float(input("na ile lat: "))

import calculation

print(calculation.kalkulacja(kwota, oprocentowanie, okres))