from mot_aléatoire_pendu import mot_aléatoire
import unidecode


class ErreurPendu(Exception):
    """Erreurs qui seront générées pendant le traitement du programme"""

class Pendu:

    def __init__(self):

        Difficulté = int(input("Entrez le niveau de difficulté auquel vous désirez jouer :\n"
        "1 - Très facile\n2 - Facile\n3 - Normal\n4 - Difficile\n5 - Très difficile\n"))
        self.mot = (mot_aléatoire(difficulté=Difficulté)).lower()
        self.état = Difficulté - 1
        self.mot_sans_accents = unidecode.unidecode(self.mot)
        self.tentatives = []
        self.affichage = list((len(self.mot)*"_"))
        self.affichage_tentatives = " ".join(self.tentatives)
        for indice, values in enumerate(self.mot_sans_accents):
            if values == "-" or values == " ":
                self.affichage[indice] = self.mot[indice]
        self.affichage_mot = " ".join(self.affichage)

    def __str__(self):
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
            if self.état == i:
                return( j + "\n" +
                    f"Mot à trouver : {self.affichage_mot}" + "\n" +
                    f"Lettres tentées : {self.affichage_tentatives}")

    #TODO faire une méthode pour demander_coup, et ajouter dans les arg de jouer_lettre une lettre
    def jouer_lettre(self):
        self.lettre = input("Entrez une lettre qui n'a pas encore été choisie:")
        for i, j in enumerate(self.mot_sans_accents):
            if self.lettre == j:
                self.affichage[i] = self.mot[i]
                self.affichage_mot = " ".join(self.affichage)
        if self.lettre not in self.mot_sans_accents:
            self.tentatives += [self.lettre]
            self.état += 1
            self.affichage_tentatives = " ".join(self.tentatives)

