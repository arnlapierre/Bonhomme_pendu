""" Ce module importe le contenu d'un fichier csv 'Lexique_modifié.csv'."""
"""À partir de la colonne 'orthographe de ce fichier, on choisit un mot au hasard parmi les 146000+"""
"""entrées."""

import class_mot_aléatoire_pendu
from random import choice, randint


def generer_mot(*, difficulté=None):
    # L'argument optionnel «difficulté» prend les 5 valeurs suivantes:
    # très_facile, facile, normal, difficile, très_difficile

    catégories = ['NOM', 'VER', 'ADV', 'ADJ', 'ONO', 'PRO']


    # Difficulté très facile
    # Catégorie aléatoire, mot de 3 à 5 lettres, freq upper than 5
    # TODO rétablir le csv avec freq
    if difficulté == str(1):
        cat = choice(catégories)
        nblettres = randint(3, 6)
        freq_ut = 5

    #si la fonction est appelée sans arguments, elle retourne un mot au hasard,
    #toute catégorie confondue
