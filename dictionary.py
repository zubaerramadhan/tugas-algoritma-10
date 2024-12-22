def dictionarylist(lista, listb):
    dictionarywarna = dict(zip(lista, listb))
    return dictionarywarna

lista = ['red', 'green', 'blue']
listb = ['#FF0000', '#008000', '#0000FF']

hasil = dictionarylist(lista, listb)
print(hasil)