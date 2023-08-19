import os

usuarios = { "07061754338": {"nome":"Lucas Benevinuto Pereira", "cpf":"07061754338", "saldo": 0, "credito": 0, "extrato":[]},
}
resp=-1

def menu_1():
    print('\nBEM-VINDO AO BANCO ZEUS\n')
    print('\n--------------------')
    print('        MENU')
    print('--------------------\n')
    print('[1] NOVO USUARIO')
    print('[2] PESQUISAR USUARIO ')
    print('[3] GERENCIAR USUARIO')
    resp = int(input('ESCOLHA:'))
    return resp

def novo_usuario():
        nome = input('NOME:')
        while nome == '':
            print('DIGITE UM NOME VALIDO:')
            nome = input('NOME:')
        cpf = input('DIGITE SEU CPF:')
        while len(cpf) != 11:
            print('DIGITE UM CPF VALIDO:')
            cpf = input('DIGITE SEU CPF:')
        novo = {
            "nome": nome,
            "cpf": cpf,
            "saldo": 0,
            "credito": 0,
            "extrato": []
        }
        usuarios[cpf] = novo
    
def pesquisar_usuario():
        print('---Pesquisar Usuario---')
        cpf = input('Digite o CPF do usuario:')
        while len(cpf) != 11:
            print('DIGITE UM CPF VALIDO:')
            cpf = input('DIGITE SEU CPF:')
        print('----------------------')
        print(f'NOME:{usuarios[cpf]["nome"]}')
        print(f'CPF:{usuarios[cpf]["cpf"]}')
        print(f'SALDO:{usuarios[cpf]["saldo"]}')
        print(f'CREDITO:{usuarios[cpf]["credito"]}')
        print('----------------------')
    
def gerenciar_usuario():
        cpf = input('Digite o cpf do usuario:')
        while len(cpf) != 11:
                print('DIGITE UM CPF VALIDO:')
                cpf = input('DIGITE SEU CPF:')
        while True:
            print('----------------------------------')
            print('     GERENCIAMENTO DE USUARIO')
            print('----------------------------------')
            print('[1] VERIFICAR SALDO')
            print('[2] DEPOSITO')
            print('[3] SAQUE')
            print('[4] EXTRATO')
            print('[5] OPÇÕES DE CREDITO')
            print('[0] Sair')
            resp = int(input('ESCOLHA:'))
            if resp == 0:
                break
            if resp == 1:
                print(f'SALDO DA CONTA: {usuarios[cpf]["saldo"]}')
            if resp == 2:
                print('--DEPOSITO--')
                dep = float(input('DIGITE O VALOR QUE DESEJA DEPOSITAR:'))
                usuarios[cpf]["saldo"] += dep
                usuarios[cpf]["extrato"].append(f'DEPOSITO DE R${dep} FEITO.')
            if resp == 3:
                print('--SAQUE--')
                saq = float(input('DIGITE O VALOR QUE DESEJA SACAR:'))
                usuarios[cpf]["saldo"] -= saq
            if resp == 4:
                print(f'EXTRATO: {usuarios[cpf]["extrato"]}')
            if resp == 5:
                if usuarios[cpf]["saldo"] < 100:
                    print(f'SALDO INSUFICIENTE PARA O SERVIÇO DE CREDITO, ADICIONE MAIS {100-usuarios[cpf]["saldo"]} PARA LIBERAR')
                elif usuarios[cpf]["saldo"] >= 100 and usuarios[cpf]["saldo"]< 1000:
                    print('VOCÊ PODE LIBERAR R$500 DE CREDITO\n[1]DESEJO LIBERAR O CREDITO\n[OUTRO NUMERO] NÃO TENHO INTERESSE')
                    esc = int(input('ESCOLHA:'))
                    if esc == 1:
                        usuarios[cpf]["credito"] = 500
                elif usuarios[cpf]["saldo"] >= 1000:
                    print('VOCÊ PODE LIBERAR R$5000 DE CREDITO\n[1]DESEJO LIBERAR O CREDITO\n[OUTRO NUMERO] NÃO TENHO INTERESSE')
                    esc = int(input('ESCOLHA:'))
                    if esc == 1:
                        usuarios[cpf]["credito"] = 5000


while True:
    resp = menu_1()
    while resp != 1 and resp != 2 and resp != 3 and resp != 4 and resp != 0:
        os.system('cls')
        print('--------------------')
        print('ESCOLHA UMA OPÇÃO VALIDA')
        resp = menu_1()
    if resp == 0:
        break                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    if resp == 1:
        os.system('cls')
        novo_usuario()
    if resp == 2:
       os.system('cls')
       pesquisar_usuario()
    if resp == 3:
         os.system('cls')
         gerenciar_usuario()
