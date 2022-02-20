import abc


class Funcionario(abc.ABC):
    def __init__(self, nome, cpf, salario):
        self.nome = nome
        self.cpf = cpf
        self._salario = salario

    @abc.abstractmethod
    def get_bonificacao(self):
        return self._salario * 1.2


class Autenticavel(abc.ABC):

    @abc.abstractmethod
    def autentica(self, senha):
        if self.senha == senha:
            return True
        else:
            print('senha incorreta')
            return False


class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, senha, gerenciados):
        super().__init__(nome, cpf, salario)
        self.senha = senha
        self.gerenciados = gerenciados

    def get_bonificacao(self):
        return self._salario * 1.15

    def autentica(self, senha):
        if self.senha == senha:
            return True
        else:
            print('senha incorreta')
            return False


class Diretor(Funcionario):
    def __init__(self, nome, cpf, salario, senha):
        super().__init__(nome, cpf, salario)
        self.senha = senha
    """Não conseguimos instanciar uma subclasse de Funcionario 
    sem implementar o método abstrato get_bonificacao()	"""
    def get_bonificacao(self):
        return self._salario * 1.5


class Cliente():
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf


class SistemaInterno:
    def login(self, obj, senha):
        if isinstance(obj, Autenticavel):
            obj.autentica(senha)
        else:
            print('{} não é autenticável'.format(obj.__class__.__name__))


class ControleBonificacoes:
    def __init__(self, total_bonificacoes=0):
        self.__total_bonificacoes = total_bonificacoes

    @property
    def total_bonificacoes(self):
        return self.__total_bonificacoes

    @total_bonificacoes.setter
    def total_bonificacoes(self, total_bonificacoes):
        self.__total_bonificacoes = total_bonificacoes

    def registra(self, obj):
        if hasattr(obj, 'get_bonificacao'):
            self.total_bonificacoes += obj.get_bonificacao()
        else:
            print('instancia de {} não implementa o metodo get_bonificacao()'.format(obj.__class__.__name__))


if __name__ == '__main__':

    g = Gerente('Ricardo', '111111111-11', 5000, '1234', 11)
    d = Diretor('Joana', '222222222-22', 10000, '1234')
    gera = Cliente('geras', 'dá silva', '555555555-55')

    c = ControleBonificacoes()
    c.registra(g)
    c.registra(d)
    # c.registra(gera)

    Autenticavel.register(Gerente)
    sistema = SistemaInterno()
    sistema.login(g, '1234')
    sistema.login(d, '1234')
    sistema.login(gera, '1234')
