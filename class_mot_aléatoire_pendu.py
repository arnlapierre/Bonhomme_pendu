import pandas as pd
from random import choice


class MotAleatoire:

    def __init__(self):
        self.dt = pd.read_csv("Lexique_modifié.csv", sep=";")

    def set_categorie(self, gram):
        catégorie_df = self.dt[self.dt["classe"].str[0:3] == gram]
        return catégorie_df

    def set_premlettre(self, lettre, dataframe):
        première_lettre_df = dataframe[dataframe.orthographe.str[:1] == lettre]
        return première_lettre_df

    def set_nblettres(self, nb, dataframe):
        # Détermine un mot en fonction du nb de lettres (entre 1 et 25 lettres).
        nblettres_df = dataframe[dataframe.nblettres == nb]
        return nblettres_df

    def freq_films_greater_than(self, freq, dataframe):
        rarete_films_df = dataframe[dataframe.freqfilms >= float(freq)]
        return rarete_films_df

    def freq_films_lower_than(self, freq, dataframe):
        rarete_films_df = dataframe[dataframe.freqfilms <= float(freq)]
        return rarete_films_df

    def set_all(self, *, cat=None, premlettre=None, nblettres=None,
                freq_lt=None, freq_ut=None):
        # catégories :
        # ['NOM', 'AUX', 'VER', 'ADV', 'PRE', 'ADJ', 'ONO', 'CON', 'ART', 'PRO']
        if cat:
            df = self.set_categorie(cat)
        else:
            df = self.dt
        if premlettre:
            df = self.set_premlettre(premlettre, df)
        if nblettres:
            df = self.set_nblettres(nblettres, df)
        if freq_lt or freq_ut:
            if freq_ut:
                df = self.freq_films_greater_than(freq_ut, df)
            if freq_lt:
                df = self.freq_films_lower_than(freq_lt, df)

        # if len(df) == 0:
            # return "Aucun mot ne correspond à ces critères de recherche."
        return choice(list(df.orthographe))
