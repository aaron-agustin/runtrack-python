def verifier_pair_impair(nombre):
    if isinstance(nombre, int) and nombre >= 0:
        if nombre % 2 == 0:
            return f"{nombre} est un nombre pair."
        else:
            return f"{nombre} est un nombre impair."
    else:
        return "Veuillez entrer un nombre entier positif."


resultat1 = verifier_pair_impair(4)
resultat2 = verifier_pair_impair(7)
resultat3 = verifier_pair_impair(0)
resultat4 = verifier_pair_impair(-5)
resultat5 = verifier_pair_impair(10.5)


print(resultat1)
print(resultat2)
print(resultat3)
print(resultat4)
print(resultat5)
