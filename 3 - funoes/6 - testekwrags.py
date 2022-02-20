def teste_kwargs(arg1, arg2, arg3, *args):
    print('arg1: ', arg1)
    print('arg2: ', arg2)
    print('arg3: ', arg3)
    for ar in args:
        print('outro argumento: {}\n'.format(ar))


def teste_kwargs2(**kwargs):
    for ar, value in kwargs.items():
        print('{} = {}\n'.format(ar, value))


args = ('um', 2, 3, 4, 'dezoito', 22, 14)
kwargs = {'arg4': 'dezoito', 'arg3': 3, 'arg2': 'dois', 'arg1': 'um'}

teste_kwargs(*args)
teste_kwargs2(**kwargs)
