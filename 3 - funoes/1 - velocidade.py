def velocidade(espaco, tempo):
    v = espaco/tempo
    print('velocidade: {}m/s'.format(v))
    return v


def dados(nome, idade=None):
    if idade is not None:
        return 'nome: {}\nidade: {}\n'.format(nome, idade)
    else:
        return 'nome: {}\nidade não informada\n'.format(nome)


print(dados('joão', 20))
print(dados('joão'))
# velocidade(100, 20)
# aceleracao = velocidade(100, 20)/20

