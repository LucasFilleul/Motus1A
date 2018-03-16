#--------------------------------ameliorations---------------------------------#
#------------------------------------------------------------------------------#
#                             un peu mieux ecrit
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#


liste='liste.txt'
import random, pygame
from pygame.locals import *
pygame.mixer.init()


#---------------------------------mot--aleatoire-------------------------------#

# fonction qui creer une liste a partir d'un fichier contenant des mots
def laListe(nomFic):
    fic=open(nomFic,'r')
    listemots=[]
    for ligne in fic:
        listemots.append(ligne[0:len(ligne)-1])     # pour enlever le \n
    return listemots

# fonction qui genere un mot        
def motAleatoire(nomFic):
    liste=laListe(nomFic)
    tailleListe=len(liste)
    numero=random.randrange(0,tailleListe,1)
    motadeviner=liste[numero]
    return motadeviner



#----------------------------entree-de--l'utilisateur--------------------------#

# fonction qui permet a un joueur d'entrer un mot
def entreeUser(rentrecequetuveux):
    entreeUtilisateur=input('Entrez un mot : ' )
    return entreeUtilisateur


#-------------------------------------lettres----------------------------------#

# fonction qui indique les lettres bien placees 
# le motadeviner et entree auront la meme taille
def lettresBienPlacees(motadeviner,entree):
    bonneplace=motadeviner[0]               # la premiere lettre sera donnee
    for i in range(1,len(entree)):
        if entree[i]==motadeviner[i]:
            bonneplace=bonneplace+entree[i]
        else:
            bonneplace=bonneplace+'X'
    return bonneplace

assert(lettresBienPlacees('bonjour','bondour')=='bonXour')
assert(lettresBienPlacees('maire','meres')=='mXXXX')


# fonction qui indique les lettres mal placees
# le motadeviner et entree auront la meme taille

# le probleme, c'est que si une lettre revient plusieurs fois, on ne pourra pas
# indiquer precisement si 2 t sont mal places, ou si il y a un autre e si on en
# a deja trouve un bien place

def lettresMalPlacees(motadeviner,entree):
    bonneplace=lettresBienPlacees(motadeviner,entree)   
    mauvaiseplace=[]
    for i in range(len(entree)):
        if entree[i] in motadeviner and entree[i]!=motadeviner[i]:
        # si la lettre est dans motadeviner et qu'elle n'est pas bien placee
            if entree[i] not in bonneplace and entree[i] not in mauvaiseplace:
            # si la lettre n'est ni dans bonneplace, ni deja dans mauvaise place
                mauvaiseplace.append(entree[i])
    return mauvaiseplace
    
assert(lettresMalPlacees('bonjour','nourrir')==['n','u'])



# fonction qui donne les lettres bien placees d'un mot ainsi que les lettres mal
# placees, lors d'une tentative
def unetentative(motadeviner,entree):
    if len(motadeviner)==len(entree):
        bonneplace=lettresBienPlacees(motadeviner,entree)
        print('Lettres bien placees : '+bonneplace)
        mauvaiseplace=lettresMalPlacees(motadeviner,entree)
        print('Lettres mal placees : '+str(mauvaiseplace)+'\n')

#----------------------------------motus----------------------------------------        
# une partie de motus
def motusUnePartie(nomFic):
    pygame.mixer.stop()
    Musique()
    motadeviner=motAleatoire(nomFic)
    
    print('Nombre de lettres : '+str(len(motadeviner)))
    print('Mot a deviner : '+motadeviner[0]+'X'*(len(motadeviner)-1)+'\n')

    entreeJoueur=''
    cpt=1    
    while cpt<11 and entreeJoueur!=motadeviner:
        print('Numero de la tentative : '+str(cpt))
        entreeJoueur=entreeUser(nomFic)
        unetentative(motadeviner,entreeJoueur)
        cpt+=1
        if entreeJoueur==motadeviner:
            pygame.mixer.music.stop()
            bruitage2()
            bruitage3()
            print('C\'EST GAGNE')
            cpt=cpt-1
    if cpt==11:
        print('PERDU')
        pygame.mixer.music.stop()
        bruitage()
        print(motadeviner)
        


# version finale pour jouer a Motus indefiniment       
def motus(nomFic):
    reponse='O'
    while reponse=='O':
        motusUnePartie(nomFic)
        reponse=input('Voulez-vous rejouer ? (O/N) ' )


def Musique():
        pygame.mixer.music.load("motus.mp3")
        pygame.mixer.music.play()

def bruitage():
    pygame.mixer.Sound('perdu.wav').play()

def bruitage2():
    pygame.mixer.Sound('clapclap.wav').play()

def bruitage3():
    pygame.mixer.Sound('feudart.wav').play()

motus(liste)

