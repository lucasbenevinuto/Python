def encontrar_maior_elemento(matriz):
    maior_elemento = matriz[0][0]
    linha_maior_elemento = 0
    coluna_maior_elemento = 0

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] > maior_elemento:
                maior_elemento = matriz[i][j]
                linha_maior_elemento = i
                coluna_maior_elemento = j

    return maior_elemento, linha_maior_elemento, coluna_maior_elemento

def encontrar_menor_elemento(matriz):
    menor_elemento = matriz[0][0]
    linha_menor_elemento = 0
    coluna_menor_elemento = 0

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] < menor_elemento:
                menor_elemento = matriz[i][j]
                linha_menor_elemento = i
                coluna_menor_elemento = j

    return menor_elemento, linha_menor_elemento, coluna_menor_elemento

matriz = []
for i in range(6):
    linha = []
    for j in range(3):
        valor = float(input(f"Digite o valor da posição ({i+1}, {j+1}): "))
        linha.append(valor)
    matriz.append(linha)

maior_elemento, linha_maior, coluna_maior = encontrar_maior_elemento(matriz)
print(f"O maior elemento é {maior_elemento} e está na posição ({linha_maior+1}, {coluna_maior+1}).")

menor_elemento, linha_menor, coluna_menor = encontrar_menor_elemento(matriz)
print(f"O menor elemento é {menor_elemento} e está na posição ({linha_menor+1}, {coluna_menor+1}).")
