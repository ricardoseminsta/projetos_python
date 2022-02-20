import abc
from tributavel import Tributavel
from manipulador import ManipuladorDeTributaveis


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


# class ContaCorrente(Conta, Tributavel): com herança multipla
class ContaCorrente(Conta):  # registrar como subclasse virtual de Tributavel
    def __init__(self, numero, titular, tipo, saldo, limite=1000):
        super().__init__(numero, titular, tipo, saldo, limite)

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa + 456
        return self._saldo

    def get_valor_imposto(self):
        return self._saldo * 0.01


class ContaPoupanca(Conta):
    def __init__(self, numero, titular, tipo, saldo, limite):
        super().__init__(numero, titular, tipo, saldo, limite)

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa + 123
        return self._saldo


# class SeguroVida(Tributavel): não era herança multipla mas é o mesmo processo de cima
class SeguroVida:  # será registrada como subclasse virtual tbm
    def __init__(self, valor, titular, num_apolice):
        self._valor = valor
        self._titular = titular
        self._num_apolice = num_apolice

    def get_valor_imposto(self):
        return 50 + self._valor * 0.05


class ContaInvestimento(Conta):
    def __init__(self, numero, titular, tipo, saldo, limite):
        super().__init__(numero, titular, tipo, saldo, limite)

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa + 5
        return self._saldo

    def get_valor_imposto(self):
        return self._saldo * 0.03


if __name__ == '__main__':

    # c = Conta('123-4', 'Ricardo', 100)
    cc = ContaCorrente('111-1', 'Ricardo', 'corrente', 1000, 1000)
    cp = ContaPoupanca('222-2', 'Joana', 'poupanca', 5000, 10000)
    ci = ContaInvestimento('333-3', 'Vick', 'investimento', 1000, 50000)
    seguro = SeguroVida(100, 'Cleyton', '777-77')

    Tributavel.register(ContaCorrente)
    Tributavel.register(SeguroVida)
    Tributavel.register(ContaInvestimento)  # continua não tributavel por causa do hasatrb na classe maninpulador,

    print(cc.get_valor_imposto())
    print(seguro.get_valor_imposto())
    print(ci.get_valor_imposto())

    lista_tributaveis = [cc, seguro, ci]

    mt = ManipuladorDeTributaveis()
    total = mt.calcula_impostos(lista_tributaveis)
    print('imposto recolhido de todas as contas: {}'.format(total))
