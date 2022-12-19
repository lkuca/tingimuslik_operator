from math import *
from pickle import TRUE

#try:
#    nimi=input("Mis su nimi on?")


#    if nimi.upper()=="JUKU":
#        print("lähme kinno")
#        vanus=int(input("kui vana sa oled?"))
#        if vanus>=0 or vanus<=100:
#            print("VIGA")
#        elif vanus<6:
#            print("tasuta!")
#        elif vanus>=6 and vanus<=14:
#            print("Lapse pilet")
#        elif vanus>=15 and vanus<=65:
#            print("täispilet")
#        elif vanus>=65:
#            print("soodus pilet")
#    else:
#        print("Otsime Juku")
#except:
#    print("vale andmetüüp")
##teine ülesanne
#nimi1=input("mis sinu nimi on?")
#nimi2=input("mis sinu nimi on?")
#if nimi1.isalpha()==True and nimi2.isalpha():
#    if nimi1==("oleg") and nimi2==("sanja"):
#        print(f"{nimi1} ja {nimi2} te olete täna pinginaabrid")
#    else:
#        print()
#else:
#    print("välja Andmetüüp")
#kolmas ülesanne
#try:
#    pikkus=float(input("Mis pikkus on?"))
#    laius=float(input("Mis laius on?"))
#    if pikkus>0 and laius>0:
#        print("lean pindala!")
#        Pindala=laius*pikkus
#        print(f"Pindala on : {Pindala}")
#        print("Kas teeme remondi või ei tee?")
#        vastus=input("")
#        if vastus.lower()=="jah":
#            hind=float(input("kui palju maksab ruutmeeter?"))
#            if hind<0:
#                print("vale vastus, palun sisesta positiivne arv.")
#            else:
#                põrand=hind*Pindala
#                print(f"remondi summa on: {põrand}")           
#except:
#    print("Andmetüüp on vale, peab olema ujumiskomaga")
try:
    hind=float(input("mis on hind?"))
    if hind>0:

        if hind>700:
            print(f"sul on soodus 30%, {hind-hind*0.3}")
        else:
            print(f"{hind}")
except:
    print("andmetüüp on vale")
