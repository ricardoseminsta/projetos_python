lista = [12,-2,4,8,29,45,78,36,-17,2,12,8,3,3,-52]

cont = 0
oco = 0

while cont < len(lista):
    if lista[-1] == lista[cont]:
        oco += 1

    cont += 1
print("as ocorrencias do valor {}, foram {}".format(lista[-1],oco))