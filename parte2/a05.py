import random

print("*********************************")
print("Bem vindo ao jogo de foca!")
print("*********************************")

palavra_secreta = "banana".upper()

letras_acertadas = ["_" for letra in palavra_secreta]


enforcou = False
acertou = False
erros = 0

print(letras_acertadas)

while(not enforcou and not acertou):
    chute = input("Qual letra? ")
    chute = chute.strip().upper()

    if (chute in palavra_secreta):
        index = 0
        for letra in palavra_secreta:
            if (letra == chute):
                letras_acertadas[index] = letra
            index = index + 1
    else:
        erros += 1
        print("Ops! Faltam {} tentativas".format(len(palavra_secreta) - erros))
    
    enforcou = erros == len(palavra_secreta)
    acertou = "_" not in letras_acertadas
    print(letras_acertadas)
    
if (acertou): 
    print("GG")
else:
    print("Loser")

def jogar():
    print("Jogando forca")