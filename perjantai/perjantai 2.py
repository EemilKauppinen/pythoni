from ast import Break
import random
# Haulikko ruletti
haulikonammukset = [0,0,0,0,0,0]
paikka = random.randrange(len(haulikonammukset))
haulikonammukset[paikka] = 1
rahamaara = 0
while True:
    print("rahasi:",rahamaara)
    print("haluatko jatkaa, y/n")
    jatko = input()
    if jatko == 'n':
        break
    elif jatko != 'y':
        continue
    luku = haulikonammukset.pop()
    if luku == 0:
        print("clikc")
        rahamaara = rahamaara + 10
    elif luku == 1:
        print("boom")
        break
