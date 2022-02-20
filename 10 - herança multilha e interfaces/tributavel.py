import abc


class Tributavel(abc.ABC):
    """Classe que contém operações de um objeto autenticavel
    As subclasses concretas devem sobrescrever o método get_valor_imposto."""
    @abc.abstractmethod
    def get_valor_imposto(self):
        #aplica taxa de imposto sobre valor do objeto
        pass
    # todos que quiserem ser tributáveis precisam saber retornar o valor do imposto



