""" Ce module importe le contenu d'un fichier csv 'Lexique_modifié.csv'."""
"""À partir de la colonne 'orthographe de ce fichier, on choisit un mot au hasard parmi les 146000+"""
"""entrées."""

import pandas as pd
import random

#TODO ajouter préposition, conjonction, pronom, article (ART:def)
def mot_aléatoire(*, difficulté=None):
    # L'argument optionnel «difficulté» prend les 5 valeurs suivantes:
    # très_facile, facile, normal, difficile, très_difficile

    fichier = ("Lexique_modifié.csv")
    data = pd.read_csv(fichier, sep=";") # data est un dataframe
    #conditions de recherche
    très_faciles, faciles, normaux, difficiles, très_difficiles = [], [], [], [], []
    for i in data.itertuples():
        # i[3] donne directement le nombre de lettres
        if i[3] > 0 and i[3] <= 5:
            très_faciles += [i[1]]
        elif i[3] >= 6 and i[3] <= 10:
            faciles += [i[1]]
        elif i[3] >= 11 and i[3] <= 15:
            normaux += [i[1]]
        elif i[3] >= 16 and i[3] <= 20:
            difficiles += [i[1]]
        elif i[3] >= 21 and i[3] <= 25:
            très_difficiles += [i[1]]

    #si la fonction est appelée sans arguments, elle retourne un mot au hasard,
    #toute catégorie confondue
    if difficulté == 1:
        return random.choice(très_faciles)
    elif difficulté == 2:
        return random.choice(faciles)
    elif difficulté == 3:
        return random.choice(normaux)
    elif difficulté == 4:
        return random.choice(difficiles)
    elif difficulté == 5:
        return random.choice(très_difficiles)
    else:
        return random.choice(data['orthographe'])