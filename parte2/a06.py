import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de foca!")
    print("*********************************")

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
        
    arquivo.close()

    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()

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

if (__name__ == "__main__"):
    jogar()