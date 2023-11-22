def moyenne():
    
    note1 = float(input('Veuillez saisir la première note: '))
    note2 = float(input('Veuillez saisir la deuxième note: '))
    note3 = float(input('Veuillez saisir la troisième note: '))

    moyenne_etudiant = (note1 + note2 + note3) / 3

   
    if 15 < moyenne_etudiant <= 20:
        print('Très bon élève')
    elif 11 < moyenne_etudiant <= 15:
        print('Bon élève')
    elif 8 < moyenne_etudiant <= 10:
        print('Élève moyen')
    elif 0 <= moyenne_etudiant <= 7:
        print('Élève devant faire des efforts')
    else:
        print('Veuillez saisir des notes valides entre 0 et 20.')


moyenne()



