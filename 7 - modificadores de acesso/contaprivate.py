class Conta:

    def __init__(self, titular, saldo=0.0):
        self._titular = titular
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):

        if saldo < 0:
            print('saldo não pode ser negativo setter')

        else:
            self._saldo = saldo

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, titular):
        self._titular = titular


conta = Conta('ricardo')
print(conta.saldo)

conta.saldo = -300.5
print(conta.saldo)
