import datetime
class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf


class Historico:
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprime(self):
        print('data da abertura {}'.format(self.data_abertura))
        print('transações')
        for t in self.transacoes:
            print('-', t)


class Conta:
    def __init__(self, numero, cliente, saldo, limite):
        self.numero = numero
        self.titular = cliente
        self.saldo = saldo
        self.limite = limite
        self.histotico = Historico()

    def deposita(self, valor):
        self.saldo += valor
        self.histotico.transacoes.append('depósito de: {}'.format(valor))

    def saca(self, valor):
        if self.saldo < valor:
            print('saldo insuficiente')
            return False
        else:
            self.saldo -= valor
            self.histotico.transacoes.append('saque de: {}'.format(valor))
            return True

    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if not retirou:
            return False
        else:
            destino.deposita(valor)
            self.histotico.transacoes.append('transferiu: {} para a conta {}'.format(valor, destino.numero))

    def extrato(self):
        print('numero: {}\nsaldo: {}'.format(self.numero, self.saldo))
        self.histotico.transacoes.append('tirou um extrato - saldo de: {}'.format(self.saldo))


cliente1 = Cliente('Ricardo', 'Silva', '111111111-11')
cliente2 = Cliente('Joana', 'Siqueira', '222222222-22')

conta1 = Conta('123-4', cliente1, 120.0, 1000.0)
conta2 = Conta('123-5', cliente2, 120.0, 1000.0)
print(vars(conta1))
print(vars(conta2))

conta1.extrato()
conta2.extrato()

conta1.deposita(200)
conta1.extrato()

conta2.saca(100)
conta2.extrato()

conta1.transfere_para(conta2, 100)
conta2.extrato()
conta1.extrato()

conta1.histotico.imprime()
