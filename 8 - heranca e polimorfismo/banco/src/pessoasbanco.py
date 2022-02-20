class Funcionario:
    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario

    def get_bonificacao(self):
        return self._salario * 0.10


class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, senha, qtd_gerenciados):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._qtd_gerenciados = qtd_gerenciados

    def autencica(self, senha):
        if self._senha == senha:
            print('acesso permitido')
            return True
        else:
            print('acesso negado')
            return False

    def get_bonificacao(self):
        return super().get_bonificacao() + 1000


class ContrleBonificacoes:
    def __init__(self, total_bonificacoes=0):
        self._total_bonificacoes = total_bonificacoes

    def registra(self, obj):
        """a função isinstance verifica se o obj é instancia de uma classe e tbm funcionaria nesse caso
           porem é preferível escrecer o código esperando a interface de um objeto e não seu tipo. O método
           registra espera que o obj possua o metodo get_bonificação e não um objeto do tipo Funcionario"""

        if hasattr(obj, 'get_bonificacao'):
            self._total_bonificacoes += obj.get_bonificacao()
        else:
            print('Instancia de {} não implementa o metodo get_bonificação'.format(obj.__class__.__name__))

    @property
    def total_bonificacoes(self):
        return self._total_bonificacoes


class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf


funcionario = Funcionario('geralda', '777777777-77', 1500)
gerente = Gerente('vick', '888888888-88', 3000, '123456', 12)
cliente = Cliente('Ricardo', 'Silva', '555555555-55')

print(vars(funcionario))
#print(dir(funcionario))
print(vars(gerente))
print('Bonificação do funcionario: {}'.format(funcionario.get_bonificacao()))
print('bonificação do gerente: {}'.format(gerente.get_bonificacao()))

controle = ContrleBonificacoes()
controle.registra(funcionario)
controle.registra(gerente)
controle.registra(cliente)

print('total: {}'.format(controle.total_bonificacoes))