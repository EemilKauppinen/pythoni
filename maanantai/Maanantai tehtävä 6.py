print("mikä on bensan hinta tänään")
bensanhintatanaan = float(input())
bensanhintahuhtikuussa =float(1.65)
nousu =(bensanhintatanaan/bensanhintahuhtikuussa*100.0)-100.0
print("Bensiinin hinta tänään",bensanhintatanaan)
print("Bensiinin hinta huhtikuussa 2021 oli",bensanhintahuhtikuussa)
print("Hinta on noussut vuodessa siis",nousu,"%")
print("Siis pyöristettynä",int(nousu),"%")