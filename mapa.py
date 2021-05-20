Planetas = {"tudush": {"nome": "tudush ", "tamanho": 1, "US": 1, "dist_x": 13, "dist_y": 9},
            "momouc": {"nome": "momouc ", "tamanho": 2, "US": 2, "dist_x": 2,  "dist_y": 8},
            "zapis":  {"nome": "zapis  ", "tamanho": 3, "US": 1, "dist_x": 12, "dist_y": 7},
            "chukna": {"nome": "chukna ", "tamanho": 5, "US": 2, "dist_x": 9,  "dist_y": 14},
            "kkanik": {"nome": "kkanik ", "tamanho": 3, "US": 2, "dist_x": 8,  "dist_y": 6},
            "apicat": {"nome": "apicat ", "tamanho": 2, "US": 1, "dist_x": 5,  "dist_y": 1},
            "hstula": {"nome": "hstula ", "tamanho": 1, "US": 2, "dist_x": 11, "dist_y": 4},
            "piktle": {"nome": "piktle ", "tamanho": 3, "US": 1, "dist_x": 3,  "dist_y": 5},
            "rupita": {"nome": "rupita ", "tamanho": 3, "US": 2, "dist_x": 15, "dist_y": 11},
            "bosshi": {"nome": "bosshi ", "tamanho": 4, "US": 1, "dist_x": 10, "dist_y": 3},
            "karaii": {"nome": "karaii ", "tamanho": 3, "US": 2, "dist_x": 7,  "dist_y": 13},
            "teknot": {"nome": "teknot ", "tamanho": 3, "US": 1, "dist_x": 14, "dist_y": 2},
            "terra":  {"nome": "terra  ", "tamanho": 3, "US": 2, "dist_x": 6,  "dist_y": 12},
            "marte":  {"nome": "marte  ", "tamanho": 2, "US": 5, "dist_x": 1,  "dist_y": 15},
            "vescul": {"nome": "vescul ", "tamanho": 2, "US": 3, "dist_x": 4,  "dist_y": 10}
            }

def printa_mapa():
    achou = False
    interacoes = 0
    for l in range(1, 16):
        for c in range(1, 16):
            for k in Planetas:
                interacoes = interacoes + 1
                if l == Planetas[k]["dist_x"] and c == Planetas[k]["dist_y"]:
                    achou = True
                    npla = Planetas[k]["nome"]
            if achou is False:
                print("# "*4, end='')
            else:
                print(npla + " ", end='')
                #print(". "*4, end='')
                achou = False
        print("")
    print(interacoes)
# "tudush": {"nome": "tudush ", "tamanho": 1, "US": 1, "dist_x": 13, "dist_y": 9},
#  tudush,1,1,13,9
def lerplanetas():
    arquivo = open('arquivo.txt', 'r')
    campo = ""
    l1 = ""
    while True:
        letra = arquivo.read(1)
        campo = campo + letra
        if letra == ",":
            l1 = campo
            campo = ""
        if not letra:
            break
    print(campo)
    arquivo.close()


if __name__ == "__main__":
    printa_mapa()
    # lerplanetas()