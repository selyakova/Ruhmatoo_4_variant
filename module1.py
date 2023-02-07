#B-4 Pood 
def loe_list(file:str)->list:
    f=open(file,'r',encoding="utf-8-sig")
    mas=[]
    for rida in f:
        mas.append(rida.strip())
    f.close()
    return mas
def list_failisse(mas:list,file:str):
    f=open(file,"w",encoding="utf-8-sig")
    for item in mas:
        f.write(item+"\n")
    f.close()
def elem_listisse(hinnad:list,ostud:list):
    n=int(input("Mitu oste lisame?"))
    for j in range(n):
        nimetus=input("Nimetus: ")
        ostud.append(nimetus)
        hind=input("Hind: ")
        hinnad.append(hind)
    return hinnad,ostud
#Удалить из списка купленный товар и добавить в список купил[] и составить чек
def kustutamine(nimetus:str,hinnad:list,ostud:list):
    n=ostud.count(nimetus)
    pos=0
    for j in range(n):
        ind=ostud.index(nimetus,pos)
        pos=ind
        ostud.remove(nimetus)
        hinnad.pop(ind)
        ostud.append(nimetus)
    return hinnad,ostud
#Отобразить в алфавитном порядке список покупок и их цены
def alfavit(hinnad,ostud):
    ostud.sort()
    print(ostud)
#Найти самый дорогой товар
def maksimaalne_hind(hinnad:list,ostud:list):
    p=list(map(int,hinnad))
    max_hind=max(ostud)
    n=hinnad.count(max_hind)
    pos=0
    print(f"Suurem palk on {max_hind} eur\n Inimeste nimed: ")
    for j in range(n):
        ind=hinnad.index(max_hind,pos)
        nimi=ostud[ind]
        print(f"{nimi}")
        pos=ind+1   
#Найти цену запрашиваемого товара
def poisk(hinnad:list,ostud:list):
    for i in ostud:
        for j in hinnad:
            if i==j:
                print(j)
#Свой вариант
def ne_v_spiske(ostud:list):
    nimetus=input("Sisesta oste nimetus: ",nimetus)
    if nimetus not in ostud:
        print("Not in list!")
    else:
        print("OK")

