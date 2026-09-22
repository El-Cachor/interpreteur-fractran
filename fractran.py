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
        a=1
        for k in range(len(exposants)):
            a *= self.facteurs[k] ** exposants[k]
        return a

    def décomposition(self, n):
        exposants = []
        for k in range(len(self.facteurs)):
            exposants.append(0)
        while n != 1:
            for k in range(len(self.facteurs)):
                if n % self.facteurs[k] == 0:
                    exposants[k] += 1
                    n //= self.facteurs[k]
        return exposants

class Fractran:
    def __init__(self, fractions):
        self.programme = fractions

    def run(self, n):
        i = 0
        while i < len(self.programme):
            if self.programme[i].est_entier(n):
                n = self.programme[i].valeur(n)
                i = 0
            else:
                i += 1
        return n

def somme(i, j):
    a = [Fraction(3, 2)]
    b = Facteur([2, 3, 5])
    c= Fractran(a).run(b.nombre([i, j]))
    for k in range(len(b.décomposition(c))):
        if b.décomposition(c)[k] != 0:
            return b.décomposition(c)[k]

def produit(i, j):
    a=0
    for k in range(j):
        a = somme(i, a)
    return a
