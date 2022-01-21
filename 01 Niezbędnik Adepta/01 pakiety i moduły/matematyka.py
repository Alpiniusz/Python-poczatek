import math

a = float(input("podaj długość pierwszej przyprostokątenj: "))
b = float(input("podaj długość drugiej przyprostokątnej: "))

c = math.sqrt(math.pow(a,2) + math.pow(b,2))

print(f"długość przeciwprostokątnej to {c}")