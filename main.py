"""Ce fichier contient les deux fonctions suivantes:
une fonction qui implante le fonctionnement du jeu en altérant
l'état de jeu
et une fonction argparse qui implante des commandes au terminal.
"""
import unidecode    #permet de retourner un string sans les accents.
import time
from mot_aléatoire_pendu import mot_aléatoire


print("Bonhomme Pendu")
Difficulté = int(input("Entrez le niveau de difficulté auquel vous désirez jouer :\n"
        "1 - Très facile\n2 - Facile\n3 - Normal\n4 - Difficile\n5 - Très difficile\n"))

state = Difficulté
mot = mot_aléatoire(difficulté=Difficulté)

def potence_ascii(état):

    # État prend une valeur de 0 à 8
    # État est toujours initialisé à 0 et augmente
    # de 1 lorque le joueur se trompe.
    #TODO ajouter des raises ou un try / else ? pour si l'état est invalide? ou traité ailleurs?
    base = "██████████████▄\n" + "████████████████▄"
    a = 6*"\n" + base
    b = "\n" + "     ║\n"*5 + base
    c = "     ╔╦════╗\n" + "     ║/\n" + 4*"     ║\n" + base
    d = "     ╔╦════╗\n" + "     ║/    o\n" + 4*"     ║\n" + base
    e = "     ╔╦════╗\n" + "     ║/   \o\n" + 4*"     ║\n" + base
    f = "     ╔╦════╗\n" + "     ║/   \o/\n" + 4*"     ║\n" + base
    g = ("     ╔╦════╗\n" + "     ║/   \o/\n" +
        "     ║     ║\n" + 3*"     ║\n" + base)
    h = ("     ╔╦════╗\n" + "     ║/   \o/\n" +
        "     ║     ║\n" + "     ║    /\n" + 2*"     ║\n" + base)
    i = ("     ╔╦════╗\n" + "     ║/   \o/\n" +
        "     ║     ║\n" + "     ║    / \ \n" + 2*"     ║\n" + base)
    états= [a, b, c, d, e, f, g, h, i]
    for i, j in enumerate(états):
        if état == i:
            print(j)
            break

def jeu_bonhomme_pendu(mot):

    """ cette fonction implante le jeu
    elle accepte en argument le mot aléatoire pigé.
    """
    global state

    # TODO gérer les espaces (a capella p.ex) et les accents
    # TODO niveaux de difficulté avec le nombre de lettres (0-5), (5-10), (10-15), (15-20), (20,25)
    mot = mot.lower()                               # mettre le mot en minuscule
    mot_sans_accents = unidecode.unidecode(mot)     # avoir une copie du mot sans les accents
    sep = " "
    tentatives = []
    affichage = list((len(mot)*"_"))                # affichage pendant le jeu. Initialise au début avec des cases vides
    affichage_tentatives = sep.join(tentatives)
    for indice, values in enumerate(mot_sans_accents):
        if values == "-" or values == " ":
            affichage[indice] = mot[indice]
    affichage_mot = sep.join(affichage)

    print(f"Lettres tentées : {affichage_tentatives}")
    print(f"Mot à trouver : {affichage_mot}")
    potence_ascii(state)

    while True:

        essai = input("Entrez une lettre qui n'a pas encore été choisie :")
        for i, j in enumerate(mot_sans_accents):
            if essai == j:
                affichage[i] = mot[i]
                potence_ascii(state)
        if essai not in mot_sans_accents:
            tentatives += [essai]
            state += 1
            potence_ascii(state)
        affichage_mot = sep.join(affichage)
        affichage_tentatives = sep.join(tentatives)
        if state == 8:
            # TODO Try / except? Gérer ça dans la boucle?
            raise StopIteration(f"Vous avez perdu! Le mot était : {mot}.")
        if "_" not in affichage_mot:
            raise StopIteration(f"Vous avez gagné! Le mot était : {mot}.")

        print(f"Lettres tentées : {affichage_tentatives}")
        print(f"Mot à trouver : {affichage_mot}")

jeu_bonhomme_pendu(mot)
