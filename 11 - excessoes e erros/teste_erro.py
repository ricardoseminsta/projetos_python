from conta import Conta


def metodo1():
    print('inicio metodo 1')
    metodo2()
    print('fim metodo 1')


def metodo2():
    print('inicio metodo 2')
    c = Conta('ricardo', '111-1', 0, 0)
    for i in range(1, 15):
        c.deposita(i + 1000)
        print(c.saldo)
        if i == 5:
            c = None

    print('fim metodo 2')


if __name__ == "__main__":

    print('inicio do main')
    try:
        metodo1()
    except AttributeError:
        print('erro')
    print('fim do main')

"""repare que onde colocar o o try/exception a execuçaõ volta ao
normal a partir daquele ponto, não finalizando os outros metodos"""
