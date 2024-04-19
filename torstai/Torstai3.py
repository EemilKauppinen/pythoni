
nimet = []
while True:
    nimi = input()
    nimet.append(nimi)
    if nimi =='':
        break

tiedosto = open('nimet.txt','w',encoding='UTF-8')
for x in nimet:
    tiedosto.write(x)
tiedosto.close()
