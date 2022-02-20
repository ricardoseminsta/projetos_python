nota1 = int(input("digite a primeira nota "))
nota2 = int(input("digite a segunda nota "))
nota3 = int(input("digite a terceira nota "))
nota4 = int(input("digite a quarta nota "))

lista = []

lista.append(nota1)
lista.append(nota2)
lista.append(nota3)
lista.append(nota4)

media = sum(lista) / len(lista)

print("as notas são {} e a média é {}".format(lista,media))
