print('******************************')
print('**BEM VINDO AO JOGO DA FORCA**')
print('******************************')

palavraSecreta='banana'
letrasAcertadas = ['_', '_', '_', '_', '_', '_']

acertou = False
enforcou = False
erros = 0

print(letrasAcertadas)

while not acertou and not enforcou:

    chute = input('Qual a Letra?: ')

    if chute in palavraSecreta:
        posicao = 0

        for letra in palavraSecreta:
            if chute.upper() == letra.upper():
                #print('Encontrei a letra {} na posição {}'.format(letra,posicao))
                letrasAcertadas[posicao] = letra
            posicao += 1
    else:
        erros += 1

    acertou = '_' not in letrasAcertadas
    enforcou = erros == 6

    if acertou:
        print('\nvc ganhou!!\n')
    elif enforcou:
        print("\nvc perdeu!!\n")

    print(letrasAcertadas)
    print('erros: {}'.format(str(erros)))



print('Fim do JOgo')