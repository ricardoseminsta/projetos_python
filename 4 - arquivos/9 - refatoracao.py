import random


def jogar():
    imprime_abertura()
    palavra_secreta = carregar_palavra_secreta()
    letras_acertadas = inicia_letras_acertadas(palavra_secreta)
    print(letras_acertadas)


    acertou = False
    enforcou = False
    erros = 0
    print('Erros = {}'.format(erros))
    desenha_forca(erros)

    while not acertou and not enforcou:
        chute = pede_chute()

        if chute in palavra_secreta:
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
            print('Erros = {}'.format(erros))
        else:
            erros += 1
            desenha_forca(erros)
           # print('Erros = {}'.format(erros))

        enforcou = erros == 7
        acertou = '_' not in letras_acertadas

        print(letras_acertadas)

    if acertou:
        imprime_msg_vencedor()
    elif enforcou:
        imprime_msg_perdedor(palavra_secreta)


def imprime_abertura():
    print('******************************')
    print('**BEM VINDO AO JOGO DA FORCA**')
    print('******************************')


def carregar_palavra_secreta():
    arquivo = open('palavras.txt', 'r')
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()

    return palavra_secreta


def inicia_letras_acertadas(palavra):
    return ['_' for letra in palavra]


def pede_chute():
    chute = input('qual a letra?: ')
    chute = chute.strip().upper()
    return chute


def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    posicao = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[posicao] = letra
        posicao += 1


def imprime_msg_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_msg_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if erros == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if erros == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if erros == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if erros == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if erros == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

#def imprime_erros():



jogar()
