import menu as menu
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True :
    opcao = input(menu)
    if opcao =="d":

        valor = float(input("Informe o valor do deposito:"))
        if valor > 0 :
            saldo += valor
            extrato += f"Deposito : R$ {valor:.2f}\n"
        else:
            print("Operação falhou! o valor informado é invalido")
        print("Deposito")
    elif opcao == "s":
        valor = float(input("Informe o valor do saque:"))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! o valor do saque excede o limite")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido")
        print("Saque")
    elif opcao == "e":
        print("Extrato")
    elif opcao == "q":
        break
    else:
        print("Operação invalida, por favor selecione novamente a operação desejada")
