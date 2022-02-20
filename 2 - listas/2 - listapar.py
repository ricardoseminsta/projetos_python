lista = [12,-2,4,8,29,45,78,36,-17,2,12,8,3,3,-52]
listapar = []

cont = 0

while cont < len(lista):

    if lista[cont] % 2 == 0:
        #print(lista[cont], end=" ")
        listapar.append(lista[cont])

    cont += 1
print("os numeros pares são {} ".format(listapar))