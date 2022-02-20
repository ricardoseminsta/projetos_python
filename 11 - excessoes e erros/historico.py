import datetime


class Historico:
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.trasacoes = []

    def imprime(self):
        print('data da abertura: {}'.format(self.data_abertura))
        print('transações: ')
        for t in self.trasacoes:
            print('-', t)
