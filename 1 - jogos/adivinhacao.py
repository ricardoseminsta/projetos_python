print("***************************")
print("*   Jogo da adivinhação   *")
print("***************************")

numero = 42
tentativas = 3
rodada = 1

while tentativas > 0:

    print('tentativas {} rodada {}'.format(tentativas,rodada))
    chute = int(input('\nDigite um numero: '))
    print('\nvc digitou ', chute)

    acertou = chute == numero
    maior = chute > numero
    menor = chute < numero

    if acertou:
        print("Vc Acertou")
        break
    elif maior:
        print("vc errou, chute maior")
    elif menor:
        print("vc errou, chute menor")

    tentativas = tentativas -1
    rodada = rodada + 1
