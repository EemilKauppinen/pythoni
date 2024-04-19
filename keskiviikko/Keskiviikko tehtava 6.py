
def kysy():
    print("Jos haluat muuttaa farenheiti celsiukseksi vastaa 1, jos haluat celsiukset farenheiteksi vastaa 2")
    vastaus = int(input())
    print("Kunika monta astetta?")
    aste = int(input())
    if vastaus == 1:
        print((aste - 32)/1.8)

    else:
        print((aste*1.8) + 32)

kysy()

