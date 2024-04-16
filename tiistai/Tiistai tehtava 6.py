

print("Arvistelutuomari 1:")
tyylipiste1 = int(input())
print("Arvistelutuomari 2:")
tyylipiste2 = int(input())
print("Arvistelutuomari 3:")
tyylipiste3 = int(input())
print("Arvistelutuomari 4:")
tyylipiste4 = int(input())
print("Arvistelutuomari 5:")
tyylipiste5 = int(input())

pieni = tyylipiste1
if tyylipiste2 < pieni:
    pieni = tyylipiste2

if tyylipiste3 < pieni:
    pieni = tyylipiste3

if tyylipiste4 < pieni:
    pieni = tyylipiste4

if tyylipiste5 < pieni:
    pieni = tyylipiste5

suuri = tyylipiste1
if tyylipiste2 > suuri:
    suuri = tyylipiste2

if tyylipiste3 > suuri:
    suuri = tyylipiste3

if tyylipiste4 > suuri:
    suuri = tyylipiste4

if tyylipiste5 > suuri:
    suuri = tyylipiste5

print("Pisteet yhteensä", tyylipiste1 + tyylipiste2 + tyylipiste3 + tyylipiste4 + tyylipiste5 - pieni - suuri)