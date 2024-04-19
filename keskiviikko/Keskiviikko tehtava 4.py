
print("Anna luku")
luku = int(input())

def itseisarvo(luku):
    if luku < 0:
        return -1*luku
    else:
        return luku
    
print(itseisarvo(luku))
