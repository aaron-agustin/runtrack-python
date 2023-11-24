def my_sort(lst):
    
    nombre_coups = 0

    
    echanges_effectues = True

    
    while echanges_effectues:
        
        echanges_effectues = False

        
        for i in range(len(lst) - 1):
            
            if lst[i] > lst[i + 1]:
                
                lst[i], lst[i + 1] = lst[i + 1], lst[i]

                
                nombre_coups += 1

                
                echanges_effectues = True

    
    print("Liste triée:", lst)
    print("Nombre total de coups:", nombre_coups)

    
    return lst


ma_liste = [4, 2, 7, 1, 9, 3]
resultat = my_sort(ma_liste)
