class produit:
    def __init__(self,a,b,c,d,e,f,g):
        self._libelle=a
        self._quantite=b
        self._prix=c
        self._sold=d
        self._datedebut=e
        self._datefin=f
        self._pourcentageSolde=g
    def getLibelle(self):
        return self._libelle
    def setLibelle(self,a):
        self._libelle=a
    def getQuantite(self):
        return self._quantite
    def setQuantite(self,a):
        self._quantite=a
    def getPrix(self):
        return self._prix
    def setPrix(self,a):
        self._prix=a
    def getSold(self):
        return self._sold
    def setSold(self,a):
        self._sold=a
    def getDatedebut(self):
        return self._datedebut
    def setDatedebut(self,a):
        self._datedebut=a
    def getDatefin(self):
        return self._datefin
    def setDatefin(self,a):
        self._datefin=a
    def getPourcentageSolde(self):
        return self._pourcentageSolde
    def setPourcentageSolde(self,a):
        self._pourcentageSolde=a

    def __str__(self):
        return self._libelle+","+str(self._quantite)+","+str(self._prix)+","+str(self._sold)+","+str(self._datedebut)+","+str(self._datefin)+","+str(self._pourcentageSolde)

    def calculerPrixSolde(self):
        if(self._sold==True):
            prix2=self._prix-self._prix*self._pourcentageSolde
        else:
            prix2=self._prix
        return prix2

#-------------------
            

    
