lista = [12,-2,4,8,29,45,78,36,-17,2,12,8,3,3,-52]

maior = -1000
menor = 1000
cont = 0

while cont < len(lista):

    if maior < lista[cont]:
        maior = lista[cont]

    elif menor > lista[cont]:
        menor = lista[cont]

    cont += 1

print('\no maior valor é {} '.format(maior))

print('o menor valor é {} '.format(menor))

print(max(lista))
print(min(lista))