from fractran import Facteur, Fraction, Fractran, produit, somme

if __name__ == "__main__":
    tableau_somme = []
    for i in range(1, 11):
        for j in range(1, 11):
            tableau_somme.append(somme(i, j))
    #print(tableau_somme)

    tableau_produit = []
    for i in range(1, 11):
        for j in range(1, 11):
            tableau_produit.append(produit(i, j))
    #print(tableau_produit)

    print("Fibonacci rend les couples (F(n), F(n+1)) :")
    fibonacci = [Fraction(23, 95), Fraction(57, 23), Fraction(17, 39), Fraction(130, 17), Fraction(11, 14),
              Fraction(35, 11), Fraction(19, 13), Fraction(1, 19), Fraction(35, 2), Fraction(13, 7),
              Fraction(7, 1)]

    sortie_brute = Fractran(fibonacci).suite(3, 10)
    sortie = []
    for n in sortie_brute:
        if n == Facteur([2, 3]).nombre(Facteur([2, 3]).décomposition(n)):
            sortie.append(Facteur([2, 3]).décomposition(n))

    print(sortie)

    print("Nombres premiers :")
    premiers = [Fraction(17, 91), Fraction(78, 85), Fraction(19, 51),
            Fraction(23, 38), Fraction(29, 33), Fraction(77, 29),
            Fraction(95, 23), Fraction(77, 19), Fraction(1, 17),
            Fraction(11, 13), Fraction(13, 11), Fraction(15, 14),
            Fraction(15, 2), Fraction(55, 1)]

    sortie_brute = Fractran(premiers).suite(2, 100000)
    sortie = []
    for n in sortie_brute:
        if n == Facteur([2]).nombre(Facteur([2]).décomposition(n)) and Facteur([2]).décomposition(n)[0] > 1:
            sortie.append(Facteur([2]).décomposition(n)[0])
    print(sortie)
