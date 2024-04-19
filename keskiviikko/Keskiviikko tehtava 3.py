arvosanat = []

print("Anna arvosanat")
for x in range(10):
    luku = int(input())
    arvosanat.append(luku)
minimi = arvosanat[0]
maksimi = arvosanat[0]
summa = 0
for x in arvosanat:
    if minimi > x:
        minimi = x
    if maksimi < x:
        maksimi = x
    summa = summa + x

print("Listan pienin arvo on", minimi, "Listan suurin arvo on", maksimi, "arvosanojen keskiarvo on", summa/len(arvosanat))