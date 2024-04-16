print("Mikä on ikäsi?")

ika = int(input())

if ika < 13 and ika >= 0:
    print("child")

elif ika >= 13 and ika <= 19:
    print("teen")

elif ika >= 20 and ika <= 65:
    print("adult")

elif ika > 65:
    print("senior")
