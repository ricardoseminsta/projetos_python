import random


def jogar():
    imprime_abertura()
    nivel = carregar_nivel()
    tentativa = carregar_tentativas(nivel)

    numero = carregar_numero()
    pontos = 1000
    rodadas = 0

    while rodadas < tentativa:

        print('\ntentativas {} de {}'.format(rodadas + 1, tentativa))
        chute = chutar()

        acertou = chute == numero
        maior = chute > numero
        menor = chute < numero

        if acertou:
            imprimir_msg_acerto(pontos)
            break
        elif maior:
            pontos = pontos - chute
            imprimir_msg_erro_maior(pontos)
        elif menor:
            pontos = pontos - chute
            imprimir_msg_erro_menor(pontos)

        rodadas += 1


def imprime_abertura():
    print("***************************")
    print("*   Jogo da adivinhação   *")
    print("***************************")


def carregar_nivel():
    nivel = int(input("escolha o nível entre 1 e 3: "))
    return nivel


def carregar_tentativas(nivel):
    tentativa = 0
    if nivel == 1:
        tentativa = 10
    elif nivel == 2:
        tentativa = 5
    elif nivel == 3:
        tentativa = 3
    else:
        print('escolha errada de nivel, tente novamente')
        jogar()
    return tentativa


def carregar_numero():
    arquivo = open('numero.txt', 'r')
    numeros = []

    for linha in arquivo:
        linha = linha.strip()
        numeros.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(numeros))

    numero_secreto = numeros[numero]

    return int(numero_secreto)



def chutar():

    chute = int(input('\nDigite um numero: '))
    print('vc digitou ', chute)
    return chute


def imprimir_msg_acerto(pontos):
    print("Vc Acertou, sua pontuação é: {}".format(abs(pontos)))


def imprimir_msg_erro_maior(pontos):
    print("vc errou, chute maior, sua pontuação é: {}".format(abs(pontos)))


def imprimir_msg_erro_menor(pontos):
    print("vc errou, chute menor, sua pontuação é: {}".format(abs(pontos)))

jogar()
