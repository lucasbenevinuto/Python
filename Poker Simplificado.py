import random

def criar_baralho():
    naipes = ['♠', '♡', '♢', '♣']
    valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    baralho = []
    for naipe in naipes:
        for valor in valores:
            carta = (valor, naipe)
            baralho.append(carta)
    return baralho

def embaralhar_baralho(baralho):
    random.shuffle(baralho)

def dar_cartas(baralho, quantidade):
    return [baralho.pop() for _ in range(quantidade)]

def mostrar_mao(mao):
    for carta in mao:
        print(f"{carta[0]}{carta[1]}", end=' ')
    print()

def obter_valor(carta):
    valores = {'A': 14, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13}
    return valores[carta[0]]

def verificar_par(mao):
    valores = [obter_valor(carta) for carta in mao]
    for valor in set(valores):
        if valores.count(valor) == 2:
            return True
    return False

def verificar_dois_pares(mao):
    valores = [obter_valor(carta) for carta in mao]
    pares = set()
    for valor in set(valores):
        if valores.count(valor) == 2:
            pares.add(valor)
    return len(pares) == 2

def verificar_trinca(mao):
    valores = [obter_valor(carta) for carta in mao]
    for valor in set(valores):
        if valores.count(valor) == 3:
            return True
    return False

def verificar_sequencia(mao):
    valores = sorted([obter_valor(carta) for carta in mao])
    for i in range(1, len(valores)):
        if valores[i] != valores[i-1] + 1:
            return False
    return True

def verificar_flush(mao):
    naipes = [carta[1] for carta in mao]
    return len(set(naipes)) == 1

def verificar_full_house(mao):
    valores = [obter_valor(carta) for carta in mao]
    return len(set(valores)) == 2 and (valores.count(valores[0]) == 2 or valores.count(valores[0]) == 3)

def verificar_quadra(mao):
    valores = [obter_valor(carta) for carta in mao]
    for valor in set(valores):
        if valores.count(valor) == 4:
            return True
    return False

def verificar_straight_flush(mao):
    return verificar_sequencia(mao) and verificar_flush(mao)

def verificar_mao(mao):
    if verificar_straight_flush(mao):
        return "Straight Flush"
    if verificar_quadra(mao):
        return "Quadra"
    if verificar_full_house(mao):
        return "Full House"
    if verificar_flush(mao):
        return "Flush"
    if verificar_sequencia(mao):
        return "Sequencia"
    if verificar_trinca(mao):
        return "Trinca"
    if verificar_dois_pares(mao):
        return "Dois Pares"
    if verificar_par(mao):
        return "Um Par"
    return "Carta Alta"

def jogar_poker():
    baralho = criar_baralho()
    embaralhar_baralho(baralho)
    mao = dar_cartas(baralho, 5)
    mostrar_mao(mao)
    print("Resultado:", verificar_mao(mao))

print("Poker Simplificado\n")
jogar_poker()

