import abc


class Conta(abc.ABC):
    def __init__(self, numero, titular, tipo, saldo=0, limite=1000):
        self._numero = numero
        self._titular = titular
        self._tipo = tipo
        self._saldo = saldo
        self._limite = limite


    @abc.abstractmethod
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa
        return self._saldo

    def __str__(self):
        imprime = '\n\nnumero da conta: {}\n' \
                  'titular da conta: {}\n' \
                  'tipo da conta: {}\n' \
                  'saldo da conta: {}\n' \
                  'limite da conta: {}\n\n'.format(self._numero, self._titular, self._tipo, self._saldo, self._limite)
        return imprime


class ContaCorrente(Conta):
    def __init__(self, numero, titular, tipo, saldo, limite):
        super().__init__(numero, titular, tipo, saldo, limite)

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa + 456
        return self._saldo


class ContaPoupanca(Conta):
    def __init__(self, numero, titular, tipo, saldo, limite):
        super().__init__(numero, titular, tipo, saldo, limite)

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa + 123
        return self._saldo


class ContaInvestimento(Conta):
    def __init__(self, numero, titular, tipo, saldo, limite):
        super().__init__(numero, titular, tipo, saldo, limite)

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa + 5
        return self._saldo


if __name__ == '__main__':

    # c = Conta('123-4', 'Ricardo', 100)
    cc = ContaCorrente('111-1', 'Ricardo', 'corrente', 1000, 1000)
    cp = ContaPoupanca('222-2', 'Joana', 'poupanca', 5000, 10000)
    ci = ContaInvestimento('333-3', 'Vick', 'investimento', 1000, 50000)

    cc.atualiza(0.01)
    cp.atualiza(0.01)
    ci.atualiza(0.01)

    print('saldo conta corrente: {}'.format(cc._saldo))
    print('saldo conta poupanca: {}'.format(cp._saldo))
    print('saldo conta Investimentos: {}'.format(ci._saldo))
    print(cc)
    print(cp)
    print(ci)
