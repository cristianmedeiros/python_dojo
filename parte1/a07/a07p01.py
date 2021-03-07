import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1,101)
pontos = 1000

nivel = int(input("Escolha um nivel (1) facil (2) normal (3) dificil: "))
if nivel == 1:
    total_de_tentativas = 20
elif nivel == 2:
    total_de_tentativas = 10
elif nivel == 3:
    total_de_tentativas = 5

rodada = 1
#while(rodada <= total_de_tentativas):
for rodada in range(1, total_de_tentativas + 1):

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
        print("Você acertou e fez {} pontos!".format(pontos))
        break
    else:
        if(maior):
            print("chutou pra cima")
        elif (menor):
            print("chutou pra baixo")
            
        pontos_perdidos = abs(chute - numero_secreto)
        pontos = pontos - pontos_perdidos
            
    rodada = rodada + 1
            
print("Fim de jogo")
        

