import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************\n")

    numero_secreto = random.randrange(1, 101)
    tentativas = 0
    total_tentativas = 0
    pontos = 1000

    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Qual o nível de dificuldade?"))

    if(nivel == 1):
        total_tentativas = 15
    elif(nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    print(numero_secreto)

    for rodada in range (0,total_tentativas + 1) :
        print("\nTentativa", rodada, "de", total_tentativas, sep=" ")
        chute = int(input("Digite um número entre 1 e 100: "))
        if(chute <= 0 or chute > 100 ):
            print("Numero inválido")
            continue
        else:
            print("Você digitou ", chute, )

            acertou = numero_secreto == chute
            maior = chute > numero_secreto
            menor = chute < numero_secreto

            if(acertou):
                print("\nVocê acertou!\nSua pontução é de %d pontos" % (pontos))
                break

            else:
                if(maior):
                    print("Não tão alto! Você errou")
                    pontos_perdidos = abs(numero_secreto -  chute)
                    pontos -= pontos_perdidos
                elif(menor):
                    print("Não tão baixo! Você errou")
                    pontos_perdidos = abs(numero_secreto -  chute)
                    pontos -= pontos_perdidos

    print("Fim do jogo")

if(__name__=="__main__"):
    jogar()