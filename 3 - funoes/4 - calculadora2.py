def soma(x, y):
    return x+y


def subtracao(x, y):
    return x-y


def mult(x, y):
    return x*y


def divisao(x, y):
    if y == 0:
        print("divizão por zero")
    elif x < y:
        print("divisor não pode ser negativo")
    else:
        return x/y


def calculadora(x, y):
    return print('soma {}\nsubtração {}\nmultiplicação {}'.format(soma(x, y), subtracao(x, y), mult(x, y)))


def vmed(distancia, tempo):
    velocidade = divisao(distancia, tempo)
    # return print(velocidade)
    return print(velocidade)


#print(vmed(100, 20))
vmed(100, 20)
vmed(150, 0)
vmed(-20, 10)

calculadora(2, 2)
