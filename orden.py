import csv


# ----------------- FUNCTION FOR READ THE CSV FILE ---------------------------------------------

def alphabetic_order():
    my_order = []
    my_row = []
    with open('People_list.csv', 'r') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            name = str(row[0])
            id = str(row[1])
            nacion = str(row[2])
            phone = str(row[3])
            my_row = [name, id, nacion, phone]
            my_order.append(my_row)
    alphabetic_order_list = ordenamiento_por_mezcla(my_order)
    return alphabetic_order_list


# ----------------- FUNCTION FOR ORDER THE LIST ALPHABETICLY---------------------------------------------

def ordenamiento_por_mezcla(lista):
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[: medio]
        derecha = lista[medio:]
        # --------------- Recursive call in each middle ---------------------------
        ordenamiento_por_mezcla(izquierda)
        ordenamiento_por_mezcla(derecha)
        # --------------- Iterators for read the two sublists ---------------------
        i = 0
        j = 0
        # --------------- Iterator for read the main list -------------------------
        k = 0
        # --------------- Main loop of the function -------------------------------
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = derecha[j]
                j += 1
            else:
                lista[k] = izquierda[i]
                i += 1
            k += 1
        # --------------- left loop of the function -------------------------------
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1
        # --------------- Rigth loop of the function -------------------------------
        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1
    # --------------- End of the function return ordered list ------------------
    return lista