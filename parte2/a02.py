import random

print("*********************************")
print("Bem vindo ao jogo de foca!")
print("*********************************")

palavra_secreta = "banana"

letra_tentativa = []


enforcou = False
acertou = False

while(not enforcou and not acertou):
    chute = input("Qual letra? ")
    chute = chute.strip()

    index = 0
    for letra in palavra_secreta:
        if (letra.upper() == chute.upper()):
            letra_tentativa.append(letra)
        index = index + 1

def jogar():
    print("Jogando forca")