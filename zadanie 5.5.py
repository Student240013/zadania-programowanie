#zadanie 5

#5
cena = float(input('Podaj cene:'))
procent_przeceny = float(input('Podaj znizke %: '))
ilosc_przeceny = cena * (procent_przeceny / 100)
przeceniona = cena - ilosc_przeceny
print(f'Cena ze znizka: {przeceniona:.2f}')
print(f'zaoszczedzone: {ilosc_przeceny:.2f}')