from fractran import produit, somme

if __name__ == "__main__":
    tableau_somme = []
    for i in range(1, 11):
        for j in range(1, 11):
            tableau_somme.append(somme(i, j))
    print(tableau_somme)

    tableau_produit = []
    for i in range(1, 11):
        for j in range(1, 11):
            tableau_produit.append(produit(i, j))
    print(tableau_produit)
