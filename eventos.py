from random import choices
from main import jogador
from main import nave

def eventos():
    escolhas = [1, 2, 3, 4, 5]
    pesos = [10, 25, 25, 5, 35]

    sorte = choices(escolhas, pesos, k=1)  # k e quantida de numeros eventados
    event = sorte[0]

    if event == 5:  # 35% de nada acontecer
        print("Nada no seu caminho")
    elif event == 4:  # 5% de chance de ganhar 200 creditos
        print("Vc encontrou uma carteira com 200 creditos no seu caminho!")
        jogador.grana = jogador.grana + 200
    elif event == 3:  # 25% chance de encontrar com uma nave que queira fazer negocios
        print("Vc encontro uma nave que quer negociar")
        nave.deposito.append("terra")
        print("Vc recebeu uma carga")
        input("Digite <ENTER> para continuar")
    elif event == 2:
        print("nave inimiga")
    elif event == 1:
        print("chocar em um asteroid, escudo zera")
    else:
        print("erro")

if __name__ == "__main__":
    eventos()
