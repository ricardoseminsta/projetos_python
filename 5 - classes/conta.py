from historico import Historico


class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf


class Conta:
    def __init__(self, numero, cliente, saldo, limite=1000):
        print('inicializando uma conta')''
        self.numero = numero
        self.titular = cliente
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()

    def deposita(self, valor):
        self.saldo += valor
        self.historico.trasacoes.append('deposito de {}'.format(valor))

    def saca(self, valor):
        if self.saldo < valor:
            print('impossível sacar')
            return False
        else:
            self.saldo -= valor
            self.historico.trasacoes.append('saque de {}'.format(valor))
            return True

    def extrato(self):
        print('numero: {}\nsaldo: {}'.format(self.numero, self.saldo))
        self.historico.trasacoes.append('tirou extrato - saldo de {}'.format(self.saldo))

    def transfere(self, destino, valor):
        # self.saldo -= valor
        # destino.saldo += valor

        retirou = self.saca(valor)
        if not retirou:
            print('saldo insuficiente para concluir operação')
            return False
        else:
            destino.deposita(valor)
            self.historico.trasacoes.append('transferencia de {} para conta {}'.format(valor, destino.numero))
            return True
