class Fraction:
    def __init__(self, numerateur, denominateur):
        self.numerateur = numerateur
        self.denominateur = denominateur

    def est_entier(self):
        return self.numerateur % self.denominateur == 0

    def valeur(self):
        return self.numerateur / self.denominateur
