Planetas = {}


def carga():
    with open("arquivo.txt", 'r') as f:
        for line in f:
            listDetails = line.strip().split('|')
            Planetas[listDetails[0]] = {"nome": listDetails[0]}
            Planetas[listDetails[0]].update({"tamanho": listDetails[1]})
            Planetas[listDetails[0]].update({"US": listDetails[2]})
            Planetas[listDetails[0]].update({"dist_x": int(listDetails[3])})
            Planetas[listDetails[0]].update({"dist_y": int(listDetails[4])})
        return Planetas

if __name__ == "__main__":
    carga()

