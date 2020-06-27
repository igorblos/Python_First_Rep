print("***********************************")
print("Bem vindo ao jogo de adivinhação!!!")
print("***********************************")

numero_secreto = 42

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

print("Fim do jogo")