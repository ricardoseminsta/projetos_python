def teste(vo, *args):
    print('primeiro argumento normal: {}'.format(vo))
    for vo in args:
        print('outro argumento: {}'.format(vo))


lista = ['come', 'comida', 'saudavel']

# teste('ricardo', 'come', 'comida', 'saudavel', 'para', 'um', 'caralho')
# teste('ricardo', *lista)


def func(**kwargs):
    for key, value in kwargs.items():
        print('{} = {}'.format(key, value))


dict = {'nome': 'ricardo', 'sobrenome': 'emanuel', 'idade': 33}
# func(nome='ricardo', sobrenome='emanuel', idade=33)

func(**dict)
