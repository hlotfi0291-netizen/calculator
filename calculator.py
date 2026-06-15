n1=float(input("donner un nombre:"))
op=(input("choisir(+,-,*,/):"))
n2=float(input("donner un nombre:"))
if op=="+":
    print("resultat:",n1+n2)
elif op=="-":
    print("resultat:",n1-n2)
elif op=="*":
    print("resultat:",n1*n2)
elif op=="/":
    if n2 != 0:
        print("resultat:",n1/n2)
    else: print("erreur")
else: print("erreur")

