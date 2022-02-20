def jogar():
    import random
    print('******************************')
    print('**BEM VINDO AO JOGO DA FORCA**')
    print('******************************')

    arquivo = open('palavras.txt', 'r')
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))

    palavra_secreta= palavras[numero].upper()
    letras_acertadas = ['_' for letra in palavra_secreta]

    acertou = False
    enforcou = False
    erros = 0

    print(letras_acertadas)

    while not acertou and not enforcou:

        chute = input('Qual a Letra?: ')
        chute = chute.strip().upper()

        if chute in palavra_secreta:
            posicao = 0

            for letra in palavra_secreta:
                if chute.upper() == letra.upper():
                    #print('Encontrei a letra {} na posição {}'.format(letra,posicao))
                    letras_acertadas[posicao] = letra
                posicao += 1
        else:
            erros += 1

        acertou = '_' not in letras_acertadas
        enforcou = erros == 6

        if acertou:
            print('\nvc ganhou!!\n')
        elif enforcou:
            print("\nvc perdeu!!\n")

        print(letras_acertadas)
        print('erros: {}'.format(str(erros)))

    print('Fim do JOgo')
