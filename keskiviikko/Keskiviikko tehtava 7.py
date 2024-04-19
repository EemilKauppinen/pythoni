def laskekulutus(matka):
    return (7.5/100)*matka*2.29
print("Mikä on matkan pituus?")
matka = int(input())
print(laskekulutus(matka),"e")