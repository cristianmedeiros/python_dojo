print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

total_de_tentativas = 3
rodada = 1
#while(rodada <= total_de_tentativas):
for rodad in range(1, total_de_tentativas + 1):

    chute_str = input("Digite o seu número: ")
    print("tentativa {} de {}".format(rodada, total_de_tentativas))
    print("Voce digitou: ", chute_str)
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if (acertou):
        print("GG")
        break
    else:
        if(maior):
            print("chutou pra cima")
        elif (menor):
            print("chutou pra baixo")
            
    rodada = rodada + 1
            
print("Fim de jogo")
        

