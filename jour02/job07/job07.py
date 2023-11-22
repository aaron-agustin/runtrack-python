chaine = "abcdefghijklmnopqrstuvwxyz"
rows = 10

for i in range(rows):
    for j in range(i + 1):
        print(chaine[j], end=" ")

    print("\n")