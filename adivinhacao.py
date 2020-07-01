print("***********************************")
print("Bem vindo ao jogo de adivinhação!!!")
print("***********************************")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while (total_de_tentativas >= rodada):
    print("Tentativa {0} rodada {1}".format(rodada,total_de_tentativas))
    numero = int(input("Digite o seu número: "))

    print("Você digitou ", numero)

    acertou = numero == numero_secreto
    maior   = numero > numero_secreto
    menor   = numero < numero_secreto


    if (acertou):
        print("Você acertou")
    else:
        if(maior):
            print("Você errou, seu chute foi maior que o número secreto!")
        elif(menor):
            print("Você errou, seu chute foi menor que o número secreto!")

    rodada = rodada + 1
print("Fim do jogo")