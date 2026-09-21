from logging import raiseExceptions


class Fraction:
    def __init__(self, numérateur, dénominateur):
        self.numérateur = numérateur
        self.dénominateur = dénominateur

    def est_entier(self, n):
        return n % self.dénominateur == 0

    def valeur(self, n):
        return self.numérateur * n // self.dénominateur

class Facteur:
    def __init__(self, facteurs):
        self.facteurs = facteurs
    def nombre(self, exposants):
        a=0
        for k in range(len(exposants)):
            a *= self.facteurs[k] ** exposants[k]
        return a
