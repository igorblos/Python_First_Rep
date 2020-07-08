import random

print("***********************************")
print("Bem vindo ao jogo de adivinhação!!!")
print("***********************************")

numero_secreto = 42
total_de_tentativas = 3

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
        print("Você acertou")
        break
    else:
        if(maior):
            print("Você errou, seu chute foi maior que o número secreto!")
        elif(menor):
            print("Você errou, seu chute foi menor que o número secreto!")

print("Fim do jogo")