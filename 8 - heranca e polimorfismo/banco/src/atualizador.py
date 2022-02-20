from conta import Conta, ContaCorrente, ContaPoupanca, Cliente, Historico


class AtualizadorContas():
    def __init__(self, selic, saldo_total=0):
        self._selic = selic
        self._saldo_total = saldo_total

    @property
    def saldo_total(self):
        return self._saldo_total

    @saldo_total.setter
    def saldo_total(self, saldo_total):
        self._saldo_total = saldo_total

    def roda(self, conta):
        print('O saldo anterior da conta: {}'.format(conta.saldo))
        conta.saldo += conta.saldo * self._selic
        print('O novo saldo  da conta: {}'.format(conta.saldo))
        self.saldo_total += conta.saldo

"""
cliente1 = Cliente('ricardo', 'emanuel', '777777777-77')
cliente2 = Cliente('Joana', 'vitoria', '888888888-88')
c = Conta('123-4', cliente1, 100, 1000)
cc = ContaCorrente('222-2', cliente2, 200, 1000)
cp = ContaPoupanca('333-3', cliente1, 200, 1000)

adc = AtualizadorContas(0.01)

adc.roda(c)
adc.roda(cc)
adc.roda(cp)

print('saldo total: {}'.format(adc.saldo_total))
"""