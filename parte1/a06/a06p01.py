import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = random.random(1,101)

total_de_tentativas = 3
rodada = 1
#while(rodada <= total_de_tentativas):
for rodad in range(1, total_de_tentativas + 1):

    chute_str = input("Digite o seu número entre 1 e 100: ")
    print("tentativa {} de {}".format(rodada, total_de_tentativas))
    print("Voce digitou: ", chute_str)
    chute = int(chute_str)
    
    if(chute < 1 or chute > 100):
        print("Voce deve digitar um valor entre 1 e 100")
        continue
        

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
        

