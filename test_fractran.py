from fractran import Facteur, Fraction, Fractran, produit, somme


def test_Fraction_init():
    assert Fraction(1, 2).numérateur == 1
    assert Fraction(1, 2).dénominateur == 2


def test_Fraction_est_entier():
    assert Fraction(1, 2).est_entier(2)
    assert not Fraction(1, 3).est_entier(2)

def test_Fraction_valeur():
    assert Fraction(3, 2).valeur(4) == 3 * (4 // 2)

def test_Facteur_init():
    assert Facteur([2, 3, 7]).facteurs == [2, 3, 7]


def test_Facteur_nombre():
    assert Facteur([2, 3, 7]).nombre([1, 2]) == (2 ** 1) * (3 ** 2)
    assert Facteur([2, 3, 7]).nombre([1, 2, 3]) == (2 ** 1) * (3 ** 2) * (7 ** 3)


def test_Facteur_décomposition():
    assert Facteur([2, 3, 7]).décomposition(1) == [0, 0, 0]
    assert Facteur([2, 3, 7]).décomposition((2**3) * (3**2) * (7)) == [3, 2, 1]


def test_Fractran_init():
    programme = [Fraction(3, 10), Fraction(4, 3)]
    assert Fractran(programme).programme == programme


def test_Fractran_run():
    programme = Fractran([Fraction(3, 10), Fraction(4, 3)])

    assert programme.run(14) == 14
    assert programme.run(15) == 8


def test_somme():
    assert somme(3, 4) == 7
    assert somme(10, 6) == 16


def test_produit():
    assert produit(3, 4) == 12
    assert produit(10, 6) == 60


def test_tableau_somme():
    tableau_somme = [somme(i, j) for i in range(1, 11) for j in range(1, 11)]
    attendu = [i + j for i in range(1, 11) for j in range(1, 11)]

    assert tableau_somme == attendu


def test_tableau_produit():
    tableau_produit = [produit(i, j) for i in range(1, 11) for j in range(1, 11)]
    attendu = [i * j for i in range(1, 11) for j in range(1, 11)]

    assert tableau_produit == attendu
