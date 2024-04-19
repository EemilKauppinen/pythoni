import random
from colorama import Fore
from colorama import init

voitettu = False
while True:

    numero = int(random.randrange(2,21))
    for x in range(3):
        print("Arvaa luku")
        uusiluku = int(input())
        if uusiluku == numero:
            print(Fore.GREEN + "Onnittelut, osuit oikeaan")
            voitettu = True
            break
        elif abs(uusiluku - numero) > 5:
            print(Fore.RED + "Viileetä, arvaa uudelleen")
        elif abs(uusiluku - numero) <= 5:
            print(Fore.YELLOW + "Lähellä, arvaa uudelleen")
    print("Haluatko jatkaa","Kyllä/Ei")
    jatkaa = input()
    if jatkaa == 'Ei':
        break

    

    