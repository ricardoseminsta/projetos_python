class Conta:
    _total_contas = 0

    def __init__(self, saldo):

        self._saldo = saldo
        Conta._total_contas += 1

    @staticmethod
    def get_total_conta():
        return Conta._total_contas

# basicamente metodos staticos não recebem nenhum parêmtro
# e metodos de classe recebem parametro cls e instancia cls
# mas aparentemente tem funções semelhantes, ao menos nesse exemplo


c1 = Conta(100.0)
print(c1.get_total_conta())

c2 = Conta(200)
print(c2.get_total_conta())

print(Conta.get_total_conta())

'''os métodos estáticos utilizamos quando não precisamos
receber	a referência de um objeto especial (seja da classe
ou de uma	instância) e funciona como uma função comum,
sem relação.'''

