print("Kerro kaikkien kurssien arvosanasi välillä 4-10, kun olet ilmoittanut kaikki arvosanat laita arvosanaksi nolla.")

# arvosanat yhteen laskettuna
summa = 0
# kurssien lukumäärä yhteenlaskettuna
kurssienmaara = 0

# kysyy arvosanan, jos arvosana on eri kuin nolla niin se arvosana lisätään summaan, sekä kurssienlukumäärää kasvatetaan yhdellä. 
# jos arvosan on nolla, niin lopetaan kysely.
while True:
    arvosana = int(input())

    if arvosana != 0:
        kurssienmaara = kurssienmaara + 1
        summa = summa + arvosana


    else:
        print("Näin monta kurssia kävit", kurssienmaara,"niiden keskiarvo oli", summa/kurssienmaara)
        break
     
