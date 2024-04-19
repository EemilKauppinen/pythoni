import random
luvut = []

while True:
    numero = random.randrange(1,40)
    if numero in luvut:
        continue
    else:
        luvut.append(numero)
     
    if len(luvut) == 7:
        break

luvut.sort()
print(luvut)
tiedostonnimi = input("Anna tiedoston nimi")
tiedosto = open(tiedostonnimi,'w',encoding='UTF-8')
for x in luvut:
    tiedosto.write(str(x))
    tiedosto.write('\n')
tiedosto.close()