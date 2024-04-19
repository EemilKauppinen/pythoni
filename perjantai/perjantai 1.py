import random

rahamaara = 10
for x in range(10):
    numero = input("Anna numero väliltä 1-36: ")
    oikeanumero = random.randrange(0,36)
    if numero == oikeanumero:
        rahamaara = rahamaara + 35
    elif numero != oikeanumero:
        rahamaara = rahamaara - 1
    print("Ruletti: ", oikeanumero, " Raha: ",rahamaara)
print("Sinulla on rahaa pelin jälkeen:", rahamaara,"e")