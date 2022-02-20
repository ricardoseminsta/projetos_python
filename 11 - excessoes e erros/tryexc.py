def divisao(x, y):
    try:
        resultado = x / y
    except ZeroDivisionError:
        print('divisão por zero!')
    else:
        print('o resultado é {}'.format(resultado))
    finally:
        print('executando finally')


if __name__ == "__main__":
    divisao(2, 1)
    divisao(2, 0)
    divisao('2', '1')
