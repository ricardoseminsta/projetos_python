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
        self._saldo = saldo
        self.limite = limite
        self.histotico = Historico()

    def __str__(self):
        imprima = 'Informações da sua conta\nnumero da conta:' \
                  ' {}\nnome do titular: {}\nsaldo da conta: {}\nlimite da conta: {}\ntipo da conta: {}'.format(self.numero, self.titular.nome, self._saldo, self.limite, self.__class__.__name__)
        return imprima
    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo

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

    def atualiza(self):
        taxa = float(input('digite a taxa de atualização da conta: '))
        self.saldo += self._saldo * taxa
        return self.saldo


class ContaCorrente(Conta):
    def __init__(self,  numero, cliente, saldo, limite):
        super().__init__(numero, cliente, saldo, limite)

    def atualiza(self):
        #taxa = float(input('digite a taxa de atualização da conta corrente: '))
        return super().atualiza() * 2
        #super().atualiza() * 2

    def deposita(self, valor):
        self.saldo += valor - 0.10


class ContaPoupanca(Conta):
    def __init__(self,  numero, cliente, saldo, limite):
        super().__init__(numero, cliente, saldo, limite)

    def atualiza(self):
        taxa = float(input('digite a taxa de atualização da conta poupança: '))
        self.saldo += self.saldo * taxa * 3


cliente1 = Cliente('Ricardo', 'Silva', '111111111-11')
cliente2 = Cliente('Joana', 'Siqueira', '222222222-22')

conta1 = ContaCorrente('123-4', cliente1, 120.0, 1000.0)
conta2 = ContaPoupanca('123-5', cliente2, 120.0, 1000.0)

print(vars(conta1))
print(vars(conta2))
print('saldo conta 1 {}'.format(conta1.saldo))
conta1.atualiza()
print('saldo conta 1 atualizado {}'.format(conta1.saldo))
print('saldo conta 2 {}'.format(conta2.saldo))
conta2.atualiza()
print('saldo conta 2 atualizado {}'.format(conta2.saldo))
conta1.deposita(100)
print(conta1.saldo)
print(conta1)
print(conta2)