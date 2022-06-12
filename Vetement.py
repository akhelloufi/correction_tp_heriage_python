from produit import produit
import datetime

class Vetement(produit):

    def __init__(self,a,b,c,d,e,f,g,t1,c1):
        super().__init__(a,b,c,d,e,f,g)
        self._taille=t1
        self._couleur=c1
    def getTaille(self):
        return self._taille
    def setTaille(self,a):
        self._taille=a
    def getCouleur(self):
        return self._couleur
    def setCouleur(self,a):
        self._couleur=a
    def calculerPrixSolde(self):
        facteur=0
        if(self._taille=="S"):
            facteur=1.1
        if(self._taille=="M"):
            facteur=1.2
        if(self._taille=="XL"):
            facteur=1.3
        if(self._taille=="XXL"):
            facteur=1.4
        Prixsoldevêtement=super().calculerPrixSolde(self)*facteur
        return Prixsoldevêtement
    def __str__(self):
        return super().__str__(self)+","+self._taille+","+self._couleur

