from module1 import *

hinnad=[]
ostud=[]
ostetud=[]

while True:
    print("-----------------------") 
    print("0- loe failist \n1- ostude lisamine \n2- salvestame failisse \n3- kustuta ja lisa listisse -Ostetud- \n4- tähestikuline sorteerimine \n5- kõige kallim ost \n6- soovin leida ostu hind \n7- kas ost on listis? ")
    v=int(input())
    if v==0:
        hinnad=[]
        ostud=[]
        hinnad=loe_list("Hinnad_file.txt")
        ostud=loe_list("Ostud_file.txt")
        print(hinnad)
        print(ostud)
    elif v==1:
        hinnad,ostud=elem_listisse(hinnad,ostud)
        print(hinnad)
        print(ostud)
    elif v==2:
        list_failisse(hinnad,"Hinnad_file.txt")
        list_failisse(ostud,"Ostud_file.txt")
    elif v==3:
        hinnad,ostud=kustutamine(input("Sisesta ostude nimetus: "),hinnad,ostud)
        ostud=loe_list("Ostetud_file.txt")
        print(hinnad)
        print(ostud)
    elif v==4:
        hinnad,ostud=alfavit(ostud)
        print(ostud)
    elif v==5:
        maksimaalne_hind(hinnad,ostud)
    elif v==6:
        hinnad,ostud=poisk(input("Sisesta ostude nimetus: "),hinnad,ostud)
        ostud=loe_list("Ostud_file.txt")
        hinnad=loe_list("Hinnad_file.txt")
        print(hinnad)
        print(ostud)
    elif v==7:
        ostud=ne_v_spiske(ostud)
        print(ostud)
