def advinhacao():

    print("***************************")
    print("*   Jogo da adivinhação   *")
    print("***************************")

    numero = 42
    nivel = int(input("escolha o nível entre 1 e 3: "))
    tentativas = 0
    pontos = 1000

    if nivel == 1:
        tentativas = 10
    elif nivel == 2:
        tentativas = 5
    elif nivel == 3:
        tentativas = 2
    else:
        print('numero de nivel errado')


    #tentativas =
    rodada = 0

    while rodada < tentativas:
    #for rodada in range(1, tentativas+1):

        print('\ntentativas {} de {}'.format(rodada+1,tentativas))
        chute = int(input('\nDigite um numero: '))
        print('vc digitou ', chute)

        acertou = chute == numero
        maior = chute > numero
        menor = chute < numero

        if acertou:
            print("Vc Acertou, sua pontuação é: {}".format(abs(pontos)))
            break
        elif maior:
            pontos = pontos - chute
            print("vc errou, chute maior, sua pontuação é: {}".format(abs(pontos)))
        elif menor:
            pontos = pontos - chute
            print("vc errou, chute menor, sua pontuação é: {}".format(abs(pontos)))

        #tentativas = tentativas -1
        rodada = rodada + 1