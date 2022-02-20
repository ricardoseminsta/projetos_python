def cria_conta(numero, titular, saldo, limite):
    conta = {'numero': numero, 'titular': titular, 'saldo': saldo, 'limite': limite}
    return conta


def deposita(conta, valor):
    conta['saldo'] += valor

def saca(conta, valor):
    conta['saldo'] -= valor


def extrato(conta):
    print('numero: {}\nsaldo: {}\n'.format(conta['numero'], conta['saldo']))

def help():
    arquivo = open('documantacao.txt', 'r')
    print(arquivo.read())
    arquivo.close()



conta = cria_conta('123-4', 'ricardo', 100.0, 500.0)
extrato(conta)
deposita(conta, 100)
extrato(conta)

saca(conta, 500)
extrato(conta)

help()