import random

def jogar():

    from setuptools.command.build_py import build_py

    print("***********************************")
    print("Bem vindo ao jogo de adivinhação!!!")
    print("***********************************")

    numero_secreto = round(random.randrange(1,101))
    pontos = 100

    print("Qual o nível de dificuldade?")
    print("(1)Fácil (2)Médio (3) Difícil")

    nivel = int((input("Defina o nível:")))

    if (nivel ==1):
        total_de_tentativas = 20
    elif (nivel==2):
        total_de_tentativas = 10
    elif (nivel==3):
        total_de_tentativas = 5


    for rodada in range(1,total_de_tentativas+1):
        print("Tentativa {0} rodada {1}".format(rodada,total_de_tentativas))
        numero = int(input("Digite o seu número: "))

        print("Você digitou ", numero)

        if(numero<1 or numero>100):
            print("Você deve digitar um número entre 1 e 100!")
            continue


        acertou = numero == numero_secreto
        maior   = numero > numero_secreto
        menor   = numero < numero_secreto


        if (acertou):
            print("Você acertou e fez {0} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou, seu chute foi maior que o número secreto!")
            elif(menor):
                print("Você errou, seu chute foi menor que o número secreto!")
            pontos_perdidos = abs(numero_secreto - numero)
            pontos = pontos - pontos_perdidos

    print("Fim do jogo, sua pontuação foi de {0}".format(pontos))