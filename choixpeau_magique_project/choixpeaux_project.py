# QUESTION 1

def nombre_eleve(tab):
     """
     Retourne le nombre d'élèves ayant répondu au questionnaire.
     """
     return len(tab) / 5 # /5 car tous les noms vont de 5 en 5. Le reste, sont les réponses aux questions
     return nb_eleve



def test_nombre_eleve():
     assert nombre_eleve(["Harry Potter", 10, 5, 8, 1, "Cedric Diggory",
6, 7, 9, 4, "Drago Malefoy", 1, 3, 2, 10]) == 3
     assert nombre_eleve([]) == 0
     assert nombre_eleve(["Harry Potter", 10, 5, 8, 1, "Cedric Diggory",
6, 7, 9, 4, "Drago Malefoy", 1, 3, 2, 10, "Hermione Granger", 10, 4, 9,
3]) == 4
     print("Nombre d'eleves correct!!!")



# QUESTION 2

def eleves(tab):
     """
     Fonction permettant de retourner la liste des prénoms ayant répondu
questionnaire.
     """
     eleves = []
     i = 0
     while i< len(tab):
         if type(tab[i]) == str:
             eleves.append(tab[i])

         i = i + 5
     return eleves

def test_eleves():
     assert eleves(["Harry Potter", 10, 5, 8, 1, "Cedric Diggory", 6, 7,
9, 4, "Drago Malefoy", 1, 3, 2, 10])==["Harry Potter", "Cedric Diggory",
"Drago Malefoy"]
     assert eleves(["Amel", 8, 10, 8, 9, "Souheila", 6, 7, 10, 9]) ==
["Amel", "Souheila"]
     assert eleves([]) == []
     print("Test d'eleves correct!!! ")



# QUESTION 3
def lecture_reponses(file):
     """
     Retourne le tableau des scores d'un fichier
     """
     tab_reponses = []

     # On défini comment on veut ouvrir le fichier.
     path = file
     mode = "r"
     f = open(path, mode)
     # on ouvre la premiere ligne
     ligne = f.readline().strip()
     while ligne != '':

         # on retire les motifs ":" des lignes
         ligne_split = ligne.split(":")

         # on retire les "/" du deuxieme element (entre les nombres)
         ele = ligne_split[1]
         ele = ele.split("/")

         # on rajoute le nom de la personne dans le tableau de score.
         tab_reponses.append(ligne_split[0])

         # on parcourt le deuxieme element de la liste (qui sont les
chiffres)
         j = 0
         while j < len(ele):
             # pour chaque element de cette liste, on le transforme en
"int" puis le rajoute au tableau des scores.
             chiffre = ele[j]
             tab_reponses.append(int(chiffre))
             j = j + 1

         ligne = f.readline().strip()

     f.close()
     return tab_reponses


from random import *




# QUESTION 4
reponses = ["Harry Potter", 10, 5, 8, 1, "Cedric Diggory", 6, 7, 9, 4, "Drago Malefoy", 1, 3, 2, 10, 'Amel', 10, 7, 10, 8]

def maison(tab, indice):

    liste_maison = ["Gryffondor", "Serdaigle", "Poufsouffle", "Serpentard"]

    # On recupere les notes de l'eleve d'indice donne
    notes = [ tab[ indice + 1 ], tab[ indice + 2 ], tab[ indice + 3 ], tab[ indice + 4] ]
    maxi = notes[0] # on initialise le max avec la premiere note

    # On recupere la note max
    i = 0
    while i < 4 :
        if notes[i] > maxi :
            maxi = notes[i]
        i = i + 1

    #- On cree la liste des maisons possibles d'apres les notes max
    maison_possibles = []

    #- On recupre les maisons ayant les notes max
    i = 0
    while i < 4 :
        if notes[i] == maxi :
            maison_possibles.append(liste_maison[i])
        i = i + 1

    if len(maison_possibles) == 1 :
        return maison_possibles[0]
    else :
        return maison_possibles[randint(0, len(maison_possibles)-1)]

# QUESTION 5

def repartition(tab_reponses):
     """
     Fonction permettant de retourner un dictionnaire du prénom ainsi que
son école attribuée
     """
     # on crée un dictionnaire vide

     dico_res = {}

     #- On regarde le nombre d'élèves que contient le tableau et on fait
une boucle while en fonction de cela.
     nb_eleve = nombre_eleve(tab_reponses)
     i = 0
     while i < nb_eleve:
         # On crée une variable qui stocke la liste des noms
         liste_eleve = eleves(tab_reponses)
         # On crée une variable qui stocke la liste des maisons selon
l'indice où on est dans la boucle
         home = maison(tab_reponses, i)
         # On ajoute dans le dictionnaire les noms et les maisons.
         dico_res[liste_eleve[i]] = home
         i = i + 1
     return dico_res


def test_repartition():

     assert repartition(["Souheila", 2, 5, 8, 1, "Amel", 10, 7, 9, 4,
"Dragon", 1, 3, 2, 10]) == {'Souheila': 'Poufsouffle', 'Amel':
'Gryffondor', 'Dragon': 'Serpentard'}
     assert repartition(["Harry Potter", 10, 5, 8, 1, "Cedric Diggory",
6, 7, 9, 4, "Drago Malefoy", 1, 3, 2, 10]) == {'Harry Potter':
'Gryffondor', 'Cedric Diggory': 'Poufsouffle', 'Drago Malefoy':
'Serpentard'}
     print("Test de la fonction repartition OKK!!!!")


# QUESTION 6
def nb_erreurs(dic1, dic2):
     '''
     Fonction qui retourne le nombre de differences sur 2 differences
entre 2 dictionnaire
     '''
     erreurs = 0
     #on crée une variable permettant de faire une liste des cles du
dictionnaire
     cles = list(dic1)
     i = 0

     #on parcours la liste des cles du dictionnaire
     while i < len(cles):
         #si la valeur (maison) du deuxieme dictionnaire est differente
alors il y a une erreur
         if dic1[cles[i]] != dic2[cles[i]]:
             erreurs = erreurs + 1
         i = i + 1

     print(erreurs)
     return erreurs

def test_nb_erreurs():
     assert nb_erreurs({"Harry Potter": "Gryffondor", "Cedric Diggory":
"Poufsouffle", "Drago Malefoy": "Serpentard"},{"Cedric Diggory":
"Serdaigle", "Drago Malefoy": "Gryffondor", "Harry Potter":
"Gryffondor"}) == 2
     assert nb_erreurs({"Harry Potter": "Gryffondor", "Cedric Diggory":
"Poufsouffle", "Drago Malefoy": "Serpentard", "Hermione Granger":
'Gryffondor'}, {"Cedric Diggory": "Serdaigle", "Drago Malefoy":
"Gryffondor", "Harry Potter": "Gryffondor", "Hermione Granger":
'Poufsouffle'}) == 3
     print("Test de la fonction nombre d'erreurs : ok!!!")


#- On prend le fichier questionnaire premiere annee et on le convertit en
dictionnaire

#- Grâce à la fonction lecture reponses on transforme le fichier en liste
liste_questionnaire =
lecture_reponses('questionnaire_premiere_annee.txt')
dico_questionnaire = repartition(liste_questionnaire)


#- On prend le fichier affectation premiere annee et on le convertit en
dictionnaire
import json
file_affectation = open("affectation_premiere_annee.json", "r")
#- On lit le fichier
file_read = file_affectation.read()
#- On le convertit en dictionnaire
dico_affectation = json.loads(file_read)




#On comptabilise le nombre d'erreurs
erreurs = nb_erreurs(dico_affectation, dico_questionnaire)
#On compte le nombre d'eleves dans le fichier questionnaire
total = nombre_eleve(liste_questionnaire)

#- On fait un produit en croix permettant que calculer le pourcentage
d'erreurs du dictionnaire

pourcentage = erreurs * 100 // total
#Le resultat peut varier selon ce que le random fait : il peut
attribuer une maison différente si les scores sont identiques.
print("Il y a ",pourcentage, "% d'erreurs dans le fichier.")


# QUESTION 7

def aleatoire_maison(path):
 """Fonction qui retourne un dictionnaire qui attribue au hasard pour chaque élève une maison parmi les 4 de Poudlard."""

#on fera un appel de fichier
import json
file = open(path, "r")
dico_nom = json.load(file)
file.close()
dico_aleatoire_maison = {}\
maison = ["Gryffondor", "Serpentard",  "Poufsouffle", "Serdaigle"]
keys_dico = list(dico_nom.keys())
for keys in keys_dico :
indice_maison = randint(0, 3)
maison_choisie = maison[indice_maison]
dico_aleatoire_maison[keys] = maison_choisie
return dico_aleatoire_maison

#- on fait la moyenne pour 100
import json
    file_affectation = open("affectation_premiere_annee.json", "r")
    # On lit le fichier
    file_read = file_affectation.read()
    # On le convertit en dictionnaire
    dico_affectation_premiere_annee = json.loads(file_read)



#- On fait un produit en croix permettant que calculer le pourcentage d'erreurs du dictionnaire


    somme_erreurs = 0

    i = 0
    while i < 100:
        dictio_aleatoire = aleatoire_maison('affectation_premiere_annee.json')
        somme_erreurs = somme_erreurs + nb_erreurs(dictio_aleatoire, dico_affectation_premiere_annee)
        i = i + 1

    moyenne_100 = somme_erreurs / 100

    print("La moyenne des erreurs sur 100 essais est de :", moyenne_100)
    total = nombre_eleve(liste_questionnaire)
    pourcentage_2 = moyenne_100 * 100 // total
    print("Ce qui signifie qu'il y a ", pourcentage_2, "% d'erreurs dans le fichier.")

    # Conclusion :
    print("Avec le questionnaire, il y a moins d'erreurs : ce qui veut dire que cette méthode est meilleure que le hasard.")
