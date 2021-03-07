print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

chute_str = input("Digite o seu número: ")
print("Voce digitou: ", chute_str)
chute = int(chute_str)

acertou = chute == numero_secreto
maior   = chute > numero_secreto
menor   = chute < numero_secreto

if (acertou):
    print("GG")
else:
    if(maior):
        print("chutou pra cima")
    elif (menor):
        print("chutou pra baixo")
        

