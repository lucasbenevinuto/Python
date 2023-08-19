import random

class Time:
    def __init__(self, nome):
        self.nome = nome
        self.vitorias = 0
    
    def vencer(self):
        self.vitorias += 1

def criar_times():
    times = []
    nomes = ["Time A", "Time B", "Time C", "Time D", "Time E", "Time F", "Time G", "Time H"]
    for nome in nomes:
        times.append(Time(nome))
    return times

def jogar_partida(time1, time2):
    resultado = random.choice([1, 2])  # 1 para time1 vencer, 2 para time2 vencer
    if resultado == 1:
        time1.vencer()
        return time1
    else:
        time2.vencer()
        return time2

def disputar_mata_mata(times):
    while len(times) > 1:
        vencedores = []
        for i in range(0, len(times), 2):
            time1 = times[i]
            time2 = times[i+1]
            vencedor = jogar_partida(time1, time2)
            vencedores.append(vencedor)
        times = vencedores
    return times[0]

def simular_campeonato():
    times = criar_times()
    campeao = disputar_mata_mata(times)
    print(f"O campeão é: {campeao.nome}")

print("Simulação de Campeonato de Futebol\n")
simular_campeonato()
