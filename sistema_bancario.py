menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numeros_de_saques = 0
LIMITES_DE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor_deposito = float(input("Digite o valor do depósito: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f'DEPÓSITO: +R$ {valor_deposito:.2f}\n'
            print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido. Insira um valor positivo.")

    elif opcao == "2":
        if numeros_de_saques < LIMITES_DE_SAQUES:
            valor_saque = float(input("Digite o valor do saque: "))
            if valor_saque > 0 and valor_saque <= limite and valor_saque <= saldo:
                saldo -= valor_saque
                extrato += f'SAQUE: -R$ {valor_saque:.2f}\n'
                numeros_de_saques += 1
                print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso.")
            else:
                print("Não é possível realizar o saque. Verifique as restrições.")
        else:
            print("Limite diário de saques atingido")

    elif opcao == "3":
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("Extrato:\n" + extrato)

    elif opcao == "0":
        print("Obrigado por usar o nosso banco.")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")