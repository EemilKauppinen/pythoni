
kokonaisluvut = open('integers.txt','w',encoding='UTF-8')
desimaaliluvut = open('floats.txt','w',encoding='UTF-8')

while True:
    syote = input("Anna luku ")
    if syote =='':
        break
    elif syote.find(".") > 0:
        print("Syötteessä on pilkku, joten se on desimaaliluku")
        desimaaliluvut.writelines(syote + '\n')
    else:
        print("Syötteessä ei ole pilkkua, joten olisiko se kokonaisluku")
        kokonaisluvut.writelines(syote + '\n')
    
kokonaisluvut.close()
desimaaliluvut.close()