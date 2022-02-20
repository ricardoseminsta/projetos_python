cont = 0
cont2 = 0

lista = []
qtd = int(input('digite quantas pessoas na lista'))

while cont < qtd:
    nome = input("digite o nome: ")
    idade = input("digite a idade: ")
    cidade = input("digite a cidade: ")

    pessoa = {'nome': nome, 'idade': idade, 'cidade':cidade}
    lista.append(pessoa)

    cont += 1

while cont2 < qtd:
    print(lista[cont2])
    cont2 += 1


