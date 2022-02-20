from collections.abc import Container, MutableSequence


class Funcionarios(Container):
    _dados = []

    def __contains__(self, posicao):
        return self._dados.__contains__(self, posicao)

    def __len__(self):
        return len(self._dados)

    def __iter__(self):
        return self._dados.__iter__(self)

    """basta nossa classe Funcionarios herdar de MutableSequence
e implementar seus metodos abstratos"""


class FuncionariosDois(MutableSequence):

    _dados = []

    def __len__(self):
        return len(self._dados)

    def __getitem__(self, posicao):
        return self._dados[posicao]

    def __setitem__(self, posicao, valor):
        if isinstance(valor, FuncionariosDois):
            self._dados[posicao] = valor
        else:
            raise ValueError('Valor Atribuido não é um funcionario')

    def __delitem__(self, posicao):
        del self._dados[posicao]

    def insert(self, posicao, valor):
        return self._dados.insert(posicao, valor)


if __name__ == '__main__':
    funcionarios = Funcionarios()
