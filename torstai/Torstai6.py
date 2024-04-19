
import random
nimet1 = open("etunimet.txt",'r',encoding='UTF-8')
nimet2 = open("sukunimet.txt",'r',encoding='UTF-8')

etunimet = nimet1.readlines()
sukunimet = nimet2.readlines()
numero = random.randrange(0,9)
numero2 = random.randrange(0,9)
print(etunimet[numero].rstrip('\n') + " " + sukunimet[numero2].rstrip('\n'))




