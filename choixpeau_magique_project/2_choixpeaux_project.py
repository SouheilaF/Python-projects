

# ## IMPORTATION DE BIBLIOTHEQUES



from math import *
from json import *
from s101 import nb_erreurs


# # VARIABLES UTILES



rep1_Lisa=[7, 4, 8, 5, 7, 10, 3, 7, 8, 5]
rep2_Donna=[4, 6, 2,10, 2, 10, 4, 8, 7, 9]
rep3_Justin = [6, 5, 9, 2, 2, 7, 6, 7, 8, 4]


dico_reponses = {
    "Lisa Fischer"   : [7, 4, 8, 5, 7, 10, 3, 7, 8, 5],
    "Donna Weiss"    : [4, 6, 2,10, 2, 10, 4, 8, 7, 9],
    "Justin Sanchez" : [6, 5, 9, 2, 2, 7, 6, 7, 8, 4]
}


reference_fondateurs = [   
    {
        "house": "Serpentard", 
        "answer": [4, 6, 5, 9, 1, 7, 3, 10, 9, 8]
    },
    {
        "house": "Poufsouffle", 
        "answer": [3, 4, 9, 3, 6, 5, 10, 1, 9, 9]
    }, 
    {
        "house": "Serdaigle", 
        "answer": [2, 10, 4, 5, 2, 10, 4, 3, 7, 3]
    }, 
    {
        "house": "Gryffondor", 
        "answer": [9, 3, 6, 2, 10, 2, 5, 1, 8, 2]
    } 
]


answer_10 = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
ref_10 =  { "house" : "TEST_10",
        "answer" : [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]}

answer_1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
ref_1 =  { "house" : "TEST_1",
        "answer" : [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}



retourne_gryffondor = [{
        "house": "Serpentard", 
        "answer": [4, 6, 5, 9, 1, 7, 3, 10, 9, 8]
    },
    {
        "house": "Gryffondor", 
        "answer": [3, 4, 9, 3, 6, 5, 10, 1, 9, 9]
    }, 
    {
        "house": "Serdaigle", 
        "answer": [2, 10, 4, 5, 2, 10, 4, 3, 7, 3]
    }, 
    {
        "house": "Gryffondor", 
        "answer": [9, 3, 6, 2, 10, 2, 5, 1, 8, 2]
    }]

retourne_serpentard =  [{
        "house": "Serpentard", 
        "answer": [4, 6, 5, 9, 1, 7, 3, 10, 9, 8]
    },
    {
        "house": "Gryffondor", 
        "answer": [3, 4, 9, 3, 6, 5, 10, 1, 9, 9]
    }, 
    {
        "house": "Serdaigle", 
        "answer": [2, 10, 4, 5, 2, 10, 4, 3, 7, 3]
    }, 
    {
        "house": "Gryffondor", 
        "answer": [9, 3, 6, 2, 10, 2, 5, 1, 8, 2]
    },
    {
        "house": "Serpentard", 
        "answer": [8, 6, 6, 10, 8, 5, 5, 6, 7, 8]
    }]


# ## QUESTION 1

# In[17]:


def create_answers_from_text_file(file_name):
    """
    Fonction qui retourne le dictionnaire des réponses des élèves,
    à partir du fichier json.
    """
    
    dico_rep_eleve = {}

    f = open(file_name)
    lignes = f.readlines()
    f.close()

    # Pour chaque ligne
    i = 0
    while i < len(lignes):
        # On retire les ":" et les "/"
        cut = lignes[i].split(":")        
        reponses_eleve = cut[1].split("/")
        
        # Parcourir le tableau pour ajouter les réponses
        j = 0
        tab_reponse = []
        while j < len(reponses_eleve):
            tab_reponse.append(int(reponses_eleve[j]))
            j += 1
            
        # On ajoute dans le dictionnaire :
        # clé : l'élève | valeur : son tableau des réponses
        dico_rep_eleve[cut[0]] = tab_reponse
        i += 1
    
    return dico_rep_eleve


# ## QUESTION 2

# In[18]:


def Euclidean_distance(rep1, rep2):
    """
    Fonction qui retourne la distance euclidienne entre deux réponses.
    """
    i = 0
    somme = 0
    
    # Pour chaque valeurs, on applique la formule de la distance euclidienne.
    while i < len(rep1):
        soustraction = (rep1[i] - rep2[i])** 2
        somme = somme + soustraction
        i = i + 1
    res = sqrt(somme)
    
    return res


# ## QUESTION 3

# In[20]:


def Euclidean_house(tab_reponse, tab_reference):
    """
    Fonction qui retourne la maison d'un élève en fonction :
    de son tableau de réponse, ainsi qu'un tableau de références.
    """
    
    # On pose une valeur de départ :
    maison = tab_reference[0]["house"]
    mini = Euclidean_distance(tab_reponse, tab_reference[0]["answer"])
    
    # On trouve la plus petite distance Euclidienne,
    # en parcourant le tableau de références.
    i = 1
    while i < len(tab_reference):
        curr_val = Euclidean_distance(tab_reponse, tab_reference[i]["answer"])

        if mini >= curr_val:
            # On remplace ainsi la nouvelle plus petite valeur,
            # Ainsi que sa maison.
            mini = curr_val
            maison = tab_reference[i]["house"]
        i = i + 1

    return maison


# ## QUESTION 4

# In[21]:


def Euclidean_repartition(dico_reponses, tab_reference):
    """
    Fonction qui retourne un dictionnaire avec :
    clé : le nom des élèves | valeur : maison attribuée."""
    
    prenom = list(dico_reponses)
    dico_nom_house = {}
    i = 0
    while i < len(dico_reponses) :
        
        # On cherche la maison de l'élève dans un premier temps.
        maison = Euclidean_house(dico_reponses[prenom[i]], tab_reference)
        
        # On ajoute dans un second temps dans le dictionnaire
        #en clé l'élève, avec sa maison en valeur.
        dico_nom_house[prenom[i]] = maison

        i = i + 1
    return dico_nom_house



 
## Seconde partie de la question : voir le nombre d'erreurs.
    
    # Récuperer dictionnaire (avec nos fonctions) :  
dico_rep_eleves = create_answers_from_text_file('questionnaire_premiere_annee_10q.txt')
dico_Euclidien = Euclidean_repartition(dico_rep_eleves, reference_fondateurs)

    # Récuperer le second dictionnaire (la prédiction du choipeau)
fichier = open("affectation_premiere_annee.json", "r")
dico_affect = load(fichier)
fichier.close
dico_affectation_choixpeau = dico_affect


# Calcul du nombre d'erreurs.

Q5_nombre_erreurs = nb_erreurs(dico_Euclidien, dico_affectation_choixpeau)
pourcentage = Q5_nombre_erreurs/124 * 100


print("Il y a ", Q5_nombre_erreurs, "erreurs :")
print("Cela fait donc ", pourcentage, "% d'erreurs.")
print("Ainsi, cette méthode est plus efficace que dans la première SAE.")
print("En effet, faire la distance euclidienne est plus précise que de faire la moyenne.")




# ## QUESTION 5

# In[22]:


# On récupere les 40 références.
file = open("houses_multiple_refs.json", "r")
tab_40_references = load(file)
file.close



repartition_40_refs = Euclidean_repartition(dico_rep_eleves, tab_40_references)

Q6_nombre_erreurs = nb_erreurs(repartition_40_refs, dico_affectation_choixpeau)
Q6_pourcentage = Q6_nombre_erreurs/124 * 100


print("Il y a", Q6_nombre_erreurs, " erreurs, ce qui fait", Q6_pourcentage, " %.")

print("Cela change en effet la précision de la répartition : en effet, le fait de mettre plus de valeurs rend le résultat plus représentatif.")


# ## QUESTION 6

# In[23]:


neighbors = reference_fondateurs

def insertion_position_NN(answer, ref, neighbors):
    """
    Fonction retournant l'indice d'insertion de la référence dans le tableau des plus proches voisins :
    ce tableau restea trié du plus proche au moins proche d'après cet indice.
    """
    
    mini = Euclidean_distance(answer, neighbors[0]["answer"])
    indice = 0
    
    i = 1
    while i < len(neighbors) :
        # Calcul de la distance euclidienne la plus proche entre la réponse de l'élève et un voisin.
        distance = Euclidean_distance(answer,  neighbors[i]["answer"])
        if mini >= distance:
            mini = distance
            indice = i
        i = i + 1
        
    distance = Euclidean_distance(answer,  neighbors[i - 1]["answer"])
    # Si reference correspond au moins proche, il sra après tous les autres.
    if mini >= distance:
        
        return len(neighbors)
        
    return indice


# ## QUESTION 7

# In[24]:


def insertion_NN(answer, ref, neighbors, k):
    """
    Fonction insérant la nouvelle réponse (ref)
    dans le tableau des plus proches voisins (neighbors)
    selon un nombre 'k' de voisins.
    """
    
    # Déterminer l'indice où insérer la réponse
    indice = insertion_position_NN(answer, ref, neighbors)
    
    # Si l'indice correspond à la longueur de la liste, cela signifie que cette valeur est moins proche de toutes.
    # Il faut vérifier si on peut l'insérer à la fin (uniquement si 'k' l'autorise.)
    # S'il n'y a pas de places, on retourne directement le tableau sans insertions.
    if indice == len(neighbors) and k < len(neighbors) :
        return neighbors

    # On insère la référence dans sa position déterminée grâce à l'indice.
    neighbors.insert(indice, ref)
    
    # Si le nombre de voisins après la modification dépasse k, on supprime le plus éloigné.
    if len(neighbors) > k:
        neighbors.pop()

    return neighbors


# ## QUESTION 8

# In[25]:


def NN(answer, tab_ref, k ):
    """
    Retourne la table des k plus proches voisins.
    """
    
    # On fait une copie du tableau pour ne pas perdre les informations lors de la modification de celui-ci.
    tab_ref_copy = tab_ref.copy()
    tab_neighbors = []
    taille_tab = len(tab_ref_copy)
    
    
    j = 0
    # tant qu'on n'a pas les 'k' plus proches voisins :
    while j < k and len(tab_neighbors) < k:
        
        # On retrouve la plus petite valeur afin de l'ajouter dans le tableau des plus proches voisins.
        mini = Euclidean_distance(answer, tab_ref_copy[0]["answer"])
        i = 1
        indice = i
        while i < len(tab_ref_copy):
            curr_val = Euclidean_distance(answer, tab_ref_copy[i]["answer"])

            if mini >= curr_val:
                mini = curr_val
                indice = i
            i = i + 1
            
        # Une fois trouvé, on l'ajoute au tableau des plus proches voisins.
        tab_neighbors.append(tab_ref_copy[indice])
        
        # On supprime celui-ci du tableau pour ne pas se répéter et toujours prendre le même minimum.
        tab_ref_copy.pop(indice)
        indice = 0
        j = j + 1
        
    return tab_neighbors


# ## QUESTION 9

# In[26]:


def NN_house(neighbors):
    """
    Fonction qui retourne la maison la plus fréquente de neighbors,
    qui sera donc la nouvelle maison où l'on affectera l'élève.
    """
    
    # Selon la maison qu'on retrouve, on ajoutera 1 au score de celle-ci dans le dictionnaire.
    dico_score_maison = {'Gryffondor': 0, 'Serpentard': 0, 'Poufsouffle': 0, 'Serdaigle': 0}
    tab_maison = ['Gryffondor', 'Serpentard', 'Poufsouffle', 'Serdaigle']
  
    i = 0
    while i < len(neighbors):
        # On rajoute au dictionnaire le score de la maison qu'on trouve.
        dico_score_maison[neighbors[i]["house"]] += 1
        i = i + 1
    # On récupère la liste des scores d'apparition des maisons.
    liste_score_maison = list(dico_score_maison.values())
  
    # Pour finir, on calcule qui a le plus d'apparitions.
    maxi = liste_score_maison[0]
    indice = 0
    j = 1
    while j < len(liste_score_maison):
        if liste_score_maison[j] > maxi:
            indice = j
            maxi = liste_score_maison[j]
    
        elif liste_score_maison[j] == maxi:
            return neighbors[indice]["house"]
      
        j = j + 1
  
    return tab_maison[indice]


# ## QUESTION 10

# In[29]:


def NN_repartition(dico_reponses, ref, k):
    """
    Fonction qui retourne les maisons des élèves en fonction de leurs réponses,
    grâce à la méthode NN.
    """
    dico_repartition = Euclidean_repartition(dico_reponses, ref)
    dico_repartition_NN = { }
    
    
    i = 0
    while i < len(dico_reponses):
        # On determine les plus proches voisins

        tab_nom_eleves = list(dico_repartition)
        tab_proche_voisins = NN(dico_reponses[tab_nom_eleves[i]], ref, k)
        
        # Puis, on vérifie quelle est la maison la plus récurrente dans ce tableau.
        maison_reccurrente = NN_house(tab_proche_voisins)

        # Pour finir, on affecte l'élève à la maison la plus présen

        dico_repartition_NN[tab_nom_eleves[i]] = maison_reccurrente
        i = i + 1
    return dico_repartition_NN


### COMPTER LES ERREURS PAR RAPPORT AU CHOIXPEAU

# On récupère le dictionnaire de la nouvelle répartition grâce à la fonction NN.
dico_rep_eleves = create_answers_from_text_file('questionnaire_premiere_annee_10q.txt')
repartition_NN = NN_repartition(dico_rep_eleves, tab_40_references, 5)

# On récipère le dictionnaire d'affectation grâce au choixpeau.
fichier = open("affectation_premiere_annee.json", "r")
dico_affect = load(fichier)
fichier.close
dico_affectation_premiere_annee = dico_affect

# On calcule le nombre d'erreurs.
nombre_erreurs = nb_erreurs(repartition_NN, dico_affectation_premiere_annee)



print("Avec la nouvelle fonction, voici le nombre d'erreurs (en utilisant les 40 references) : ")
nb_k = 1
while nb_k < 6:
    erreurs_finales = nb_erreurs(NN_repartition(dico_rep_eleves, tab_40_references, nb_k), dico_affectation_premiere_annee)
    print("Le nombre d'erreurs pour k = ", nb_k, " est de ", erreurs_finales,";")
    nb_k = nb_k + 1
    
print("Ainsi, on remarquer que cette méthode est meilleure que les précédentes.")
print("La valeur de 'k' la plus performante est k = 3.")



print("Fin de la SAE !")


# In[ ]:




