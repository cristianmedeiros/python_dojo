import random

print("*********************************")
print("Bem vindo ao jogo de foca!")
print("*********************************")

palavra_secreta = "banana"

letras_acertadas = ["_","_","_","_","_","_"]


enforcou = False
acertou = False

print(letras_acertadas)

while(not enforcou and not acertou):
    chute = input("Qual letra? ")
    chute = chute.strip()

    index = 0
    for letra in palavra_secreta:
        if (letra.upper() == chute.upper()):
            letras_acertadas[index] = letra
        index = index + 1
        
    print(letras_acertadas)

def jogar():
    print("Jogando forca")