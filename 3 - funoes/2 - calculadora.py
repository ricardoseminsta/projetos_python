def calculadora(x, y):
    return {'soma': x+y, 'subtração': x-y}


resultados = calculadora(1, 2)

for key in resultados:
    print('{}: {}'.format(key, resultados[key]))


# print(type(calculadora(1, 2)))
# print(calculadora(1, 2))
