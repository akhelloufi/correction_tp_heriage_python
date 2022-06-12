from Magasin import Magasin
from produit import produit
import datetime
from Vetement import Vetement

x=Magasin()
x.nom=input("quel est nom du magasin")
x.ville=input("quel est ville du magasin")
x.adresse=input("quel est l adresse  du magasin")
x.telephone=input("quel est telephone du magasin")
x.Listprod=[]#list d objet

y=int(input("donne anne de debut"))
m=int(input("donne mois de debut"))
d=int(input("donne jour de mois de debut"))

debut=datetime.datetime(y,m,d)
y1=int(input("donne anne de fin"))
m1=int(input("donne mois de fin"))
d1=int(input("donne jour de mois de fin"))
fin=datetime.datetime(y1,m1,d1)

p1=produit("samsungalasy",100,1000.00,True,debut,fin,0.10)

x.Listprod.append(p1)

print("date pour l objet vetement costume")
y=int(input("donne anne de debut"))
m=int(input("donne mois de debut"))
d=int(input("donne jour de mois de debut"))

debut=datetime.datetime(y,m,d)
y1=int(input("donne anne de fin"))
m1=int(input("donne mois de fin"))
d1=int(input("donne jour de mois de fin"))
fin=datetime.datetime(y1,m1,d1)


v1=Vetement("costune1",50,2000.00,True,debut,fin,0.10,"XL","Blue")
x.Listprod.append(v1)


print("date pour l objet vetement chemise v2")
y=int(input("donne anne de debut"))
m=int(input("donne mois de debut"))
d=int(input("donne jour de mois de debut"))

debut=datetime.datetime(y,m,d)
y1=int(input("donne anne de fin"))
m1=int(input("donne mois de fin"))
d1=int(input("donne jour de mois de fin"))
fin=datetime.datetime(y1,m1,d1)


v2=Vetement("chemise",70,500.00,True,debut,fin,0.10,"XL","Blue")
x.Listprod.append(v2)

print("-------- affichage de informations du magasin----->")

print(x.nom,end="\t")
print(x.ville,end="\t")
print(x.adresse,end="\t")
print(x.telephone,end="\t")
#---produit vetement

for i in range(0,len(x.Listprod)):
    if(isinstance(x.Listprod[i],produit)==True):
        print(x.Listprod[i].getLibelle()," " ,x.Listprod[i].getQuantite())
    if(isinstance(x.Listprod[i],Vetement)==True):
        print(x.Listprod[i].getTaille()," " ,x.Listprod[i].getCouleur())
    










    
