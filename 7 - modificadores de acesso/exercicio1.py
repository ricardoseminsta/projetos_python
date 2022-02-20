class Conta:
    __slots__ = ['_numero','_titular','_saldo', '_limite']

    _identificador = 0

    def __init__(self, numero, titular, saldo, limite=1000):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite
        Conta._identificador += 1

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        if saldo < 0:
            print('saldo não pode ser negativo')
        else:
            self._saldo = saldo
    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, limite):
        if limite != 1000:
            print('limite não pode ser alterado')
        else:
            print('tudo ok com o limite')

    @staticmethod
    def get_id():
        return Conta._identificador


conta1 = Conta('123-4', 'ricardo', 500)
conta2 = Conta('123-5', 'Joana', 700)
conta1.saldo = -200

print(conta1.saldo)
conta1.limite = 1000
print(conta1.limite)
conta1.saldo = 600
print(conta1.saldo)
conta2.saldo = -100
print('saldo conta 2 {}'.format(conta2.saldo))
print(Conta.get_id())