print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

chute_str = input("Digite o seu número: ")
chute = int(chute_str)

if (chute == numero_secreto):
    print("GG")
else:
    print("nope")

