nom = "ordinateur"
prix = 600
quantite = 3
print(nom)
print(prix)
print(quantite)
quantite = quantite + 1
print('produit: '+nom)
print('prix: '+ str(prix),'euro')
print('quantité de stock '+str(quantite))
question = int(input('combien en voulez vous? '))
quantite -= question
print('nombre en stock: '+str(quantite))
prix += prix*10/100
print('prix apres inflation de 10%: '+str(prix),'euro')