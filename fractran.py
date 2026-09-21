class Fraction:
    def __init__(self, numérateur, dénominateur):
        self.numérateur = numérateur
        self.dénominateur = dénominateur

    def est_entier(self):
        return self.numérateur % self.dénominateur == 0

    def valeur(self):
        return self.numérateur / self.dénominateur
