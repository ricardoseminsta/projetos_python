lista = [12,-2,4,8,29,45,78,36,-17,2,12,8,3,3,-52]
#lista = [2,6]

cont = 0
soma = 0
media = 0

while cont < len(lista):
   soma += lista[cont]

   cont += 1

media = soma / len(lista)

print("a media é {}".format(media))