menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informa o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado não é válido.")

    elif opcao == "2":
        valor = float(input("Informe um valor para o saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_de_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não possui saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excdedeu seu limite!")
            
        elif excedeu_saques:
            print("Operação inválida! O usuário excedeu o limite de saques diários.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_de_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3":
        print("================ EXTRATO ================")
        print("Não foram realizados movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=================================")

    elif opcao == "0":
        break

    else:
        print("Opção inválida. Por favor, selcione novamente a operação desejada!")