from random import choice, randint
from class_mot_aléatoire_pendu import MotAleatoire

""" Ce module utilise la classe MotAleatoire afin de déterminer
un mot pour le jeu de Bonhomme pendu en fonction de 5 niveaux de 
difficulté.

Ces niveaux changent la longueur du mot à deviner et sa rareté.
Les difficultés élevées feront deviner un mot long et rare dans 
la langue française.

Si aucun niveau de difficulté n'est sélectionné, le mot sera 
complètement choisi au hasard.

"""

# TODO problème quand il n'y a aucun mot qui correspond au nb de lettre et à la fréquence

def generer_mot(*, difficulté=None):
    # L'argument optionnel «difficulté» prend les 5 valeurs suivantes:
    # très_facile, facile, normal, difficile, très_difficile

    catégories = ['NOM', 'VER', 'ADV', 'ADJ', 'PRO']

    mot = MotAleatoire()

    # Difficulté très facile
    # Catégorie aléatoire, mot de 3 à 5 lettres, freq upper than 5
    if difficulté == 1:
        cat = choice(catégories)
        nblettres = randint(3, 6)
        freq_ut = 5
        return mot.set_all(cat=cat, nblettres=nblettres, freq_ut=freq_ut)

    elif difficulté == 2:
        cat = choice(catégories)
        nblettres = randint(4, 8)
        freq_ut = 2
        freq_lt = 5
        return mot.set_all(cat=cat, nblettres=nblettres, freq_ut=freq_ut, freq_lt=freq_lt)

    elif difficulté == 3:
        cat = choice(catégories)
        nblettres = randint(6, 12)
        freq_ut = 0.1
        freq_lt = 2
        return mot.set_all(cat=cat, nblettres=nblettres, freq_ut=freq_ut, freq_lt=freq_lt)

    elif difficulté == 4:
        cat = choice(catégories)
        nblettres = randint(8, 14)
        freq_ut = 0.01
        freq_lt = 0.2
        return mot.set_all(cat=cat, nblettres=nblettres, freq_ut=freq_ut, freq_lt=freq_lt)

    elif difficulté == 5:
        cat = choice(catégories)
        nblettres = randint(11, 25)
        freq_lt = 0.01
        return mot.set_all(cat=cat, nblettres=nblettres, freq_lt=freq_lt)