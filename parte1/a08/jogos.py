import forca
import adivinhacao

def escolhe_jogo():
    print("1 Forca 2 Adinhacao")
    jogo = int(input("Escolha o jogo: "))

    if jogo == 1:
        forca.jogar()
    elif jogo == 2:
        adivinhacao.jogar()
        
if (__name__ == "__main__"):
    escolhe_jogo()