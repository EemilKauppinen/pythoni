import random
# Tämä ohjelma on peli, jossa pelaaja taistelee vihollisia, tässä yhteydessä joka luurankoa, karhua tai lohikäärmettä vastaan.
# Pelaaja aloittaa pelin valitsemalla vihollisen ja lyö painamalla enteriä. Peli arpoo pelaajalle aseen, jolla on eri ominaisuuksia. 
# Pelissä pelaaja aloittaa ja vihollinen lyö takaisin, tätä jatketaan niin kauan kunnes jonpi kumpi häviää eli hänen elämänsä tippuvat nollaan.


# Valitaan vihollinen, funktio ottaa sisään listan vihollisista. Se palauttaa valitun vihollisen.
def valitsevihollinen(viholliset):

    while True:
        for vihollinen in viholliset:
            print(vihollinen[0])
        vastaus = input("Ketä vastaan haluat taistella: ")
        for vihollinen in viholliset:
            if vastaus == vihollinen[0]:
                return vihollinen
# Itse taistelu pelaajan ja vihollisen välillä, funktio ottaa sisään vihollisen, aseen jolla taistellaan ja pelaajan elämän.
def taistele(vihollinen,ase,elama):
    while True:
        print("*****************************")
        input("Paina enter lyödäksesi")
        print()
        osuma = random.randrange(0,100) * 0.01
        if osuma <= ase[3]:
            vahinko = random.randrange(ase[1],ase[2])
            vihollinen[1] = vihollinen[1] - vahinko
            print("Osuit!", vihollinen[0],"otti vahinkoa",vahinko,"aseena",ase[0])
            print(vihollinen[0], "elämää jäljellä: ", vihollinen[1])
        else:
            print("Löit ohi, aseena", ase[0])
        if vihollinen[1] <= 0:
            print(vihollinen[0],"kuoli")
            print("Voitit pelin")
            break
        print("")
        vihollisenosuma = random.randrange(0,100) * 0.01
        if vihollinen[4] >= vihollisenosuma:
            vahinko = random.randrange(vihollinen[2],vihollinen[3])
            print(vihollinen[0],"teki sinuun vahinkoa",vahinko)
            elama = elama - vahinko
            print("Sinulla elämää jäljellä: ", elama)
            if elama <= 0:
                print("Kuolit, hävisit pelin")
                break
        else:
            print(vihollinen[0],"Löi ohi")
        print("")

# [nimi, elämä, minimivahinko, maksimivanhinko, osuma tarkkuus]
luuranko = ['luuranko',15,1,4,0.75]
lohikaarme = ['lohikaarme',100,3,8,0.45]
karhu = ['karhu',35,2,6,0.50]
viholliset = [luuranko, lohikaarme, karhu]
# [aseen nimi, minimivahinko, maksimivahinko, osuma tarkkuus]
keppi = ['keppi',0,3,0.80]
kirves = ['kirves',2,5,0.60]
jousi = ['jousi',4,7,0.50]
megakirves = ['megakirves',10,20,0.35]
# Lista aseista
aseet = [keppi, kirves, jousi, megakirves]
# Arvotaan ase
aseennumero = random.randrange(0,len(aseet) - 1)
# Suoritetaan peli
taistele(valitsevihollinen(viholliset), aseet[aseennumero],40)

            
        


