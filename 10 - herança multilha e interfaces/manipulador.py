from tributavel import Tributavel  # precisa importar tributavel senão não registra register()


class ManipuladorDeTributaveis:
    def calcula_impostos(self, lista_tributaveis):
        total = 0
        for t in lista_tributaveis:
            if isinstance(t, Tributavel) and hasattr(t, 'get_valor_imposto'):
                total += t.get_valor_imposto()
            else:
                print(t.__repr__(), " não é tributavel")
        return total


if __name__ == "__main__":

        cc1 = ContaCorrente('111-1', 'Ricardo', 'corrente', '1000')
        cc2 = ContaCorrente('212-2', 'Joana', 'corrente', '1000')
        seg1 = SeguroVida(100, 'romildo', '24-4')
        seg2 = SeguroVida(200, 'maria', '66-4')

        lista_tributaveis = []
        lista_tributaveis.append(cc1)
        lista_tributaveis.append(cc2)
        lista_tributaveis.append(seg1)
        lista_tributaveis.append(seg2)
        manipulador = ManipuladorDeTributaveis()
        total = manipulador.calcula_impostos(lista_tributaveis)