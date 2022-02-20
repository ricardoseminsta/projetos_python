from testecontainer import FuncionariosDois

import csv


class Funcionarios:
    def __init__(self, nome, cpf, saldo):
        self.nome = nome
        self.cpf = cpf
        self.saldo = saldo


arquivo = open('funcionarios.txt', 'r')
leitor = csv.reader(arquivo)

funcionarios = FuncionariosDois()

for linha in leitor:
    funcionario = FuncionariosDois(linha[0], linha[1], linha[2])
    funcionarios.append(funcionario)

for f in funcionarios:
    print(f.saldo)

arquivo.close()

#funcionarios[0] = 'Python'