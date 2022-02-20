class Conta:

    __slots__ = ['_numero', '_titular', '_saldo', '_limite']

    def __init__(self, numero, titular, saldo, limite=1000):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo


conta = Conta('123-4', 'ricardo', 500)
print(vars(conta))
'''conta.nome = 'minha conta'
print(conta.nome)'''