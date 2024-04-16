print("Kerro kolme kokonaislukua")
luku1 = int(input())
luku2 = int(input())
luku3 = int(input())

suurinluku = luku1
if suurinluku < luku2:
    suurinluku = luku2
if suurinluku < luku3:
    suurinluku = luku3
print("Tässä on suurin luku kolmesta",suurinluku )
