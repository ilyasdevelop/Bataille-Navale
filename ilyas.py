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
scores = []
for _ in range(10):
    score_partie = []  # Liste pour stocker les scores de cette partie
    for eleves in tableau_eleves:
        score_partie.append(partie())  # Ajout du score à la liste de la partie en cours
    scores.append(score_partie)  # Ajout de la liste des scores de cette partie à la liste principale
'''
# Calcul de la moyenne pour chaque personnage
for score_list in scores:
    moyenne = sum(score_list) / len(score_list)
    moyenne.append(moyenne)
print(score_list)
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


'''#calcul moyenne 
for i in scores:
    moyenne = sum(i) / len(scores)
print(type(moyenne))
fusion_scores_tab = dict(zip(tableau_eleves, moyenne))
print(fusion_scores_tab)
'''




'''
tiens abde regarde

'''
'''
Ce programme va faire 
'''

'''
dictionnaire_fusion = dict(zip(tableau_eleves, scores))
print(dictionnaire_fusion)


# Dictionnaire pour stocker les scores de chaque personnage
scores_personnages = {personnage: [] for personnage in tableau_eleves}
print(scores_personnages)
'''

'''
# Ajouter les scores de chaque personnage dans le dictionnaire
for j in range(len(score)):
    for i in range(len(tableau_eleves)):
        scores_personnages[tableau_eleves[i]].append(score[j][i])
'''

'''
# Calcul de la moyenne pour chaque personnage
moyennes = {personnage: sum(score) / len(score) for personnage, score in scores_personnages.items()}

# Affichage des moyennes
for personnage, moyenne in moyennes.items():
    print(f"Moyenne de {personnage} : {moyenne}")
'''

'''
# Liste de scores pour chaque personnage
scores = [
    [5, 8, 9, 3, 6, 2, 8, 7, 4, 6],  # Scores du personnage 1
    [6, 7, 9, 2, 5, 3, 7, 6, 3, 4],  # Scores du personnage 2
    [8, 9, 9, 4, 7, 5, 9, 8, 

# Liste pour stocker les moyennes
moyennes = []

# Calcul de la moyenne pour chaque personnage
for score_list in scores:
    moyenne = sum(score_list) / len(score_list)
    moyennes.append(moyenne)

# Affichage des moyennes
for i, moyenne in enumerate(moyennes):
    print(f"Moyenne du personnage {i+1} : {moyenne}")
'''










