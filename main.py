# Gustavo Oliveira 05/05/2021 #

# from tabulate import tabulate

#   INICIO CLASSES   #
import random


class Jogador: # Classe Jogador
    dist_x = 0
    dist_y = 0
    nome = ""
    grana = 1000

    def viajar(self, nome_pla):
        origem = planeta.nome_pla
        print("Vc já viu no radar e agora quer ir para....")
        planeta.nome_pla = input("Destino> ")
        distpercor = round(
            ((planeta.dist_x - Planetas[nome_pla]["dist_x"]) ** 2 + (planeta.dist_y - Planetas[nome_pla]["dist_y"]) ** 2) ** (1 / 2))
        print(distpercor)
        nave.gas = nave.gas - distpercor
        return planeta.nome_pla




class Nave(Jogador):  # Subclasse -----Nave herdou as variaveis e metodos de Jogador
    gas = 10
    gas_max = 20
    escudo = 100
    escudo_max = 100
    deposito = []
    arma = 1

    def explodir(self):
        print("A nave explodiu")
        self.gas = 0

    def buraconegro(self, jogador):
        print("Bugou as cordenadas")
        jogador.dist_x = 111
        jogador.dist_y = 111

class Menus(Jogador):
    comando = ""

    def case(self, item):
        itens = {
            #"01": self.ajuda,
            "11": self.status,
            "21": self.loja,  # Nao pode ter o () porque senao executa na lida, abaixo ele concatena
            "31": "Radar",
            "41": jogador.viajar,
            #"02": self.ajuda,
            "12": self.status,
            "22": self.comprar,
            "32": self.vender,
            "42": self.armar,
            "52": self.abastecer
        }
        if item != "41":
            return itens.get(item, "Nao existe essa opcao.")()  # "()" final doidera, tipo ele poe, nao entendi mas funciona
        else:
            return itens.get(item, "Nao existe essa opcao.")(planeta.nome_pla)

    def loja(self):
        menus.comando = ""
        menun1 = ("0", "1", "2", "3", "4", "5")
        print("Aqui vc compra e vende produtos.")
        print("Escolha uma opcao: <0-volta> <1-status> <2-comprar> <3-vender> <4-armar> <5-abastecer>")
        while menus.comando != "0":
            menus.comando = input("Loja > ")
            if menus.comando == "+":
                print("Escolha uma opcao: <0-volta> <1-status> <2-comprar> <3-vender> <4-armar> <5-abastecer>")
            elif menus.comando not in menun1:
                print("Opção invalida")
            elif menus.comando != "0":
                menus.case(menus.comando + "2")
            elif menus.comando == "0":
                break


    def status(self):
        print("Vc esta no planeta: " + planeta.nome_pla)
        print("Seu tanque de combustivel esta em: %d/%d " % (nave.gas, nave.gas_max))
        print("Cap %s, seu escudo esta em: %d/%d, grana: %d" % (jogador.nome, nave.escudo, nave.escudo_max, jogador.grana))
        print("Carga: ")
        print(nave.deposito)

    def comprar(self):
        print("Segue a lista do que vc pode comprar no planeta " + planeta.nome_pla)
        for k, v in Goods.items():
            print((k, v * Planetas[planeta.nome_pla]["US"])) # TODO: Modificar para sorteiaUS
        print("Vai querer comprar o q? <nada> para sair.")
        good = ""
        while True:
            good = input("Compra > ")
            if good in Goods.keys():
                jogador.grana = jogador.grana - (Goods[good] * Planetas[planeta.nome_pla]["US"])
                nave.deposito.append(good)
            elif good == "nada":
                break
            else:
                print("nao existe esse produto, escolha outro")
                print(nave.deposito)

    def vender(self):
        print(planeta.nome_pla)
        print("Vc tem para vender: ")
        print(nave.deposito)
        print("Oq deseja vender?")
        good = input("> ")
        nave.deposito.remove(good)
        jogador.grana = jogador.grana + (Goods[good] * Planetas[planeta.nome_pla]["US"])

    def armar(self):
        print("Cap %s, sua arma é do tipo: %d, grana: %d" % (jogador.nome, nave.arma, jogador.grana))
        print("Fazer uma melhoria vai lhe custar X$ 100,00. S/N?")
        simounao = input("Armar > ")
        if simounao == "s" and jogador.grana >= 100:
            nave.arma = nave.arma + 1
            jogador.grana = jogador.grana - 100
        elif jogador.grana < 100:
            print("vc nao tem grana")
        else:
            print("vc quem sabe...")

    def abastecer(self):
        print("Cap %s, seu gas esta em: %d/%d, grana: %d" % (jogador.nome, nave.gas, nave.gas_max, jogador.grana))
        print("Valor do gas e X$ 3,00 ")
        print("Quanto vai por de gas?")
        aux = input("> ")
        jogador.grana = jogador.grana - int(aux) * 3
        nave.gas = nave.gas + int(aux)

class Planeta():
    nome_pla = "terra"
    dist_x = 0
    dist_y = 0
    def sorteia_us(self):
        us = 1
        us = us * random.randint(1, 3)
        print(us)

jogador = Jogador()
nave = Nave()
menus = Menus()
planeta = Planeta()

def main():
    menun2 = ("0", "1", "2", "3", "4")
    print("Jogo Didatico")
    print("Digite seu nome comandante")
    jogador.nome = input("> ")
    print("Bem vindo Comandate %s." % jogador.nome)
    print("Vc acaba de receber uma nave com poucos recursos, vc deve melhorar isso rapido")
    print("Digite o nome da nave")
    nave.nome = input("> ")
    print("%s e uma b..... De seu jeito" % nave.nome)
    print("Escolha uma opcao: <1-status> <2-loja> <3-radar> <4-viajar>")
    while True:
        menus.comando = ""
        menus.comando = input("Angar > ")
        if menus.comando == "+":
            print("Escolha uma opcao: <1-status> <2-loja> <3-radar> <4-viajar>")
        elif menus.comando not in menun2:
            print("Opção invalida")
        elif menus.comando != "0":
            menus.case(menus.comando + "1")
        elif menus.comando == "0":
            break

#  FIM CLASSES  #

#  INICIO DICIONARIO  #
Goods = {
    "fumo": 1,
    "terra": 3,
    "alcool": 5,
    "tiberium": 7
}
Planetas = {"terra": {"nome": "terra", "tamanho": 3, "US": 2, "dist_x": 4, "dist_y": 2},
            "marte": {"nome": "marte", "tamanho": 2, "US": 20, "dist_x": 4, "dist_y": -2},
            "vesculi": {"nome": "vesculi", "tamanho": 2, "US": 3, "dist_x": -2, "dist_y": -5}
            }
#  FIM DICIONARIO  #

if __name__ == "__main__":
    main()