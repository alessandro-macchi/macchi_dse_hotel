#x è la lista da pulire, y è la lista pulita
def list_cleaner(lista_da_pulire, lista_pulita):
    for j in lista_da_pulire:
        for i in j:
            lista_pulita.append(i)
