Planetas = {"terra": {"nome": "terra", "tamanho": 3, "US": 2, "dist_x": 2, "dist_y": 2},
            "marte": {"nome": "marte", "tamanho": 2, "US": 20, "dist_x": 1, "dist_y": 3},
            "vesculi": {"nome": "vesculi", "tamanho": 2, "US": 3, "dist_x": 2, "dist_y": 6}
            }
achou = False
for l in range(1, 7):
    for c in range(1, 7):
        for k in Planetas:
            if l == Planetas[k]["dist_x"] and c == Planetas[k]["dist_y"]:
                achou = True
        if achou is False:
            print("# ", end='')
        else:
            print(". ", end='')
            achou = False
    print("")