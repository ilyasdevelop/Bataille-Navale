# coding: utf-8
'''
Voici la fonction qui va exécuter une partie de bataille navale et
retourner le nombre de points obtenus. Le nom de cette fonction est
partie()
'''
from random import randint

def partie():
    bateaux = []
    nb_bateaux = 2
    for _ in range(nb_bateaux):
        essai = (randint(1, 5), randint(1, 5))
        while essai in bateaux:
            essai = (randint(1, 5), randint(1, 5))
        bateaux.append(essai)
    nb_coups = 3
    points = 0
    coups_deja_joues = []
    while nb_coups > 0 and points < 5*nb_bateaux:
        nb_coups += -1
        coup = (randint(1, 5), randint(1, 5))
        while coup in coups_deja_joues:
            coup = (randint(1, 5), randint(1, 5))
        coups_deja_joues.append(coup)
        if coup in bateaux:
            points += 10
            bateaux.remove(coup)
        else:
            en_vue = False
            i = 0
            while i < len(bateaux) and not en_vue:
                j = 0
                while  j < 2 and not en_vue:
                    if coup[0] == bateaux[i][j] or coup[1] == bateaux[i][j]:
                        en_vue = True
                    j += 1
                i += 1
            if en_vue:
                points += 2
    return(points)


'''
Ce programme sert à importer les personnages du fichier Charactere.csv
'''

with open("Characters.csv", mode='r', encoding='utf-8') as f:
    lignes_du_CSV = f.readline()
    tableau_eleves = []
    for ligne in f:
        tableau_eleves.append(ligne.split(';')[1])
#print(tableau_eleves)

'''
Ce programme permet de faire jouer tout les personnage 10 fois et de stocker leur résultat
'''

#Initialisation de la liste pour stocker les scores
scores = []

#Simulation de 10 parties
for _ in range(10):
    scores_partie = {}  # Dictionnaire pour stocker les scores de cette partie
    for eleve in tableau_eleves:
        scores_partie[eleve] = partie()  # Ajout du score au dictionnaire de la partie en cours
    scores.append(scores_partie)  # Ajout du dictionnaire des scores de cette partie à la liste principale

#Calcul du score total pour chaque personnage
total_scores = {eleve: sum(scores[partie][eleve] for partie in range(10)) for eleve in tableau_eleves}

#Classement des personnages par score décroissant
classement_final = sorted(total_scores.items(), key=lambda item: item[1], reverse=True)


#Affichage du classement final
for i, (personnage, score) in enumerate(classement_final, 1):
    print(f"{i}. {personnage} : {score}")


# Calcul de la moyenne des scores de tous les personnages
moyenne_generale = sum(total_scores.values()) / len(total_scores)

# Affichage de la moyenne générale
print(f"La moyenne générale des scores est : {moyenne_generale}")

