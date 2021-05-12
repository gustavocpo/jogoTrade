Planetas = {"terra": {"nome": "terrai ", "tamanho": 3, "US": 2, "dist_x": 2, "dist_y": 2},
            "marte": {"nome": "martei ", "tamanho": 2, "US": 20, "dist_x": 1, "dist_y": 3},
            "vesculi": {"nome": "vescul ", "tamanho": 2, "US": 3, "dist_x": 4, "dist_y": 6}
            }
achou = False
for l in range(1, 16):
    for c in range(1, 16):
        for k in Planetas:
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