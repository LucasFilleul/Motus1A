def lexiqueMotus(nomFic="./liste_francais6A10.txt"):
    fic=open(nomFic)
    res=[]
    for ligne in fic:
        res.append(ligne[:len(ligne)-1])
    fic.close()
    return res
