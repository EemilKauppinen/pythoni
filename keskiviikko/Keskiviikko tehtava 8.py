
def listasisaan(nimet):
    len(nimet)
    print(len(nimet))
    jono = ''
    for x in range(len(nimet)):
        if len(nimet) - 1 == x:
            jono = jono + nimet[x]
        else:
            jono = jono + nimet[x] + ','
    print(jono)


print("Laita nimiä listaa, jos haluat lopettaa laita listaan tyhjä")
nimet = []
nimi = 'x'

while nimi !="":
    nimi = input()
   
    if nimi == "":
        break
    nimet.append(nimi)


    
listasisaan(nimet)