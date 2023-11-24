def draw_triangle():
    try:
        height = int(input("Entrez la hauteur du triangle : "))
    except ValueError:
        print("Veuillez entrer un nombre entier.")
        return

    for i in range(height):
        spaces = ' ' * (height - i - 1)
        if i == 0:
            print(spaces + '_')
        elif i == height - 1:
            print('_' * (2 * height - 1))
        else:
            print(spaces + '/' + ' ' * (2 * i - 1) + '\\')


draw_triangle()
