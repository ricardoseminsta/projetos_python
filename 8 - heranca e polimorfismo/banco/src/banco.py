from conta import Conta, ContaCorrente, ContaPoupanca, Cliente, Historico
from atualizador import AtualizadorContas


class Banco:
    def __init__(self):
        self.lista_contas = []

    def adiciona(self, conta):
        self.lista_contas.append(conta)

    def pega_conta(self, index):
        return self.lista_contas[index]

    def pega_total_contas(self):
        return 'o total de contas é: {}'.format(len(self.lista_contas))


cliente1 = Cliente('ricardo', 'emanuel', '777777777-77')
cliente2 = Cliente('Joana', 'vitoria', '888888888-88')
c = Conta('123-4', cliente1, 100, 1000)
cc = ContaCorrente('222-2', cliente1, 200, 1000)
cp = ContaPoupanca('333-3', cliente2, 200, 1000)
banco = Banco()

banco.lista_contas.append(c)
banco.lista_contas.append(cc)
banco.lista_contas.append(cp)

print(banco.lista_contas[0].titular.nome)
print(banco.lista_contas[1].titular.nome)
print(banco.lista_contas[2].titular.nome)
print(banco.pega_conta(0).numero)
print(banco.pega_total_contas())

adc = AtualizadorContas(0.01)

for conta in banco.lista_contas:
    adc.roda(conta)

print('o saldo total das contas é: {}'.format(adc.saldo_total))

