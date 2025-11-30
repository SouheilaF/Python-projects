## Le jeu du 7 se joue à deux joueurs avec deux dés. Les joueurs jouent à tour de rôle, 5 tours chacun. On a donc 1er tour joueur A, 1er tour joueur B, 2e tour joueur A, etc.

## À chaque tour, le joueur lance les dés.

##    S'il fait 7, il marque 7 points puis s'arrête ;
##    sinon il peut choisir de relancer les dés.
##        À chaque relance,
##            si le joueur fait 7, son tour est terminé et il ne marque aucun point,
##            sinon il ajoute au score du tour le résultat du lancer. S'il décide de s'arrêter, il ajoute le score du tour à son score total.from random import *

def jet_des():
    somme = randint(1, 6) + randint(1, 6)
    return somme

def Tour_Jeu():
    relancer = True
    res = jet_des()
    if res == 7:
        print("Tu as fais 7! +7 à ton score...")
        print("fin du tour! Joueur 1, +7!")
        return 7

    while relancer == True:
        print("Tu as fais", res, " . Relancer? (oui ou o, n ou non)")
        choix = input()
        if choix == 'o' or choix == 'oui':
            res = jet_des()
            if res == 7:
                print("Tu as fais 7, tu ne gagnes donc aucun point...\nTour terminé!")
                return 0
        else:
            print("Donc pas de relances... Tu gagnes", res, "! Au tour de l'autre joueur!")
            relancer = False
            return res

def jeu_du7():
    j1 = 0
    j2 = 0
    i = 0
    tour_j1 = True
    nb_tour = 1.0
    print("Commençons le jeu du 7! Premier joueur...")
    while i < 10:
        nb_tour = nb_tour + 0.5
        res = Tour_Jeu()
        if tour_j1:
            j1 = j1 + res
            print("Deuxième joueur, à toi de jouer!")
            tour_j1 = False
        else:
            j2 = j2 + res
            if nb_tour < 6.0 :
                print("Premier joueur, à toi de jouer! Tour numéro", nb_tour,"...")
            tour_j1 = True
        i = i + 1
    win = j1
    winner = "Joueur A"
    if j1 < j2:
        win = j2
        winner = "Joueur B"
    print("C'est terminé... Premier joueur fini avec", j1, "points, et deuxième joueur avec", j2, "points! Gagnant...", winner, "avec ", win, " points!!")

jeu_du7()
