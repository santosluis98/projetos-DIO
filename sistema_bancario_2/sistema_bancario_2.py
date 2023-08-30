# Função de menu
def menu():
    menu_text = """
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Criar Usuário
    [5] Criar Conta
    [6] Listar Contas
    [0] Sair
    
    => """
    return input(menu_text)

# Função para depositar
def depositar(saldo, valor, extrato, /):
    saldo += valor
    extrato.append(f'DEPÓSITO: +R$ {valor:.2f}\n')
    return saldo, extrato

# Função para sacar
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor <= saldo and numero_saques < limite_saques:
        saldo -= valor
        extrato.append(f'SAQUE: -R$ {valor:.2f}\n')
        numero_saques += 1
    return saldo, extrato, numero_saques

# Função para exibir extrato
def exibir_extrato(saldo, *, extrato):
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("Extrato:")
    for operacao in extrato:
        print(operacao)

# Função para criar usuário
def criar_usuario(usuarios):
    nome = input("Digite o nome do usuário: ")
    data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")
    cpf = input("Digite o CPF: ")
    endereco = input("Digite o endereço (logradouro, endereco, número, bairro, cidade, estado): ")

    usuario = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    }

    usuarios.append(usuario)
    print(f"Usuário {nome} cadastrado com sucesso.")

# Função para filtrar usuário por CPF
def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            return usuario
    return None

# Função para criar conta
def criar_conta(agencia, numero_conta, usuario, contas):
    conta = {
        'agencia': agencia,
        'numero_conta': numero_conta,
        'usuario': usuario,
        'saldo': 0,
        'extrato': [],
        'numero_saques': 0,
        'limite_saques': 3,
    }

    contas.append(conta)
    print(f"Conta criada com sucesso. Agência: {agencia}, Conta: {numero_conta}")

# Função para listar contas
def listar_contas(contas):
    for conta in contas:
        print(f"Agência: {conta['agencia']}, Conta: {conta['numero_conta']}, Nome: {conta['usuario']['nome']}")

# Função principal
def main():
    usuarios = []
    contas = []
    numero_conta = 1

    while True:
        escolha = menu()

        if escolha == "1":
            # Realizar depósito
            if not contas:
                print("Não há contas bancárias cadastradas. Crie uma conta primeiro.")
            else:
                numero_conta = int(input("Digite o número da conta para depositar: "))
                conta = next((c for c in contas if c['numero_conta'] == numero_conta), None)
                if conta:
                    valor_deposito = float(input("Digite o valor do depósito: "))
                    if valor_deposito > 0:
                        conta['saldo'], conta['extrato'] = depositar(conta['saldo'], valor_deposito, conta['extrato'])
                    else:
                        print("Valor de depósito inválido. Insira um valor positivo.")
                else:
                    print("Conta não encontrada.")

        elif escolha == "2":
            # Realizar saque
            if not contas:
                print("Não há contas bancárias cadastradas. Crie uma conta primeiro.")
            else:
                numero_conta = int(input("Digite o número da conta para sacar: "))
                conta = next((c for c in contas if c['numero_conta'] == numero_conta), None)
                if conta:
                    valor_saque = float(input("Digite o valor do saque: "))
                    if valor_saque > 0:
                        conta['saldo'], conta['extrato'], conta['numero_saques'] = sacar(
                            conta['saldo'], valor_saque, conta['extrato'], conta['limite_saques'], conta['numero_saques']
                        )
                    else:
                        print("Valor de saque inválido. Insira um valor positivo.")
                else:
                    print("Conta não encontrada.")

        elif escolha == "3":
            # Exibir extrato
            if not contas:
                print("Não há contas bancárias cadastradas. Crie uma conta primeiro.")
            else:
                numero_conta = int(input("Digite o número da conta para exibir o extrato: "))
                conta = next((c for c in contas if c['numero_conta'] == numero_conta), None)
                if conta:
                    exibir_extrato(conta['saldo'], extrato=conta['extrato'])
                else:
                    print("Conta não encontrada.")

        elif escolha == "4":
            # Criar usuário
            criar_usuario(usuarios)

        elif escolha == "5":
            # Criar conta bancária
            if not usuarios:
                print("Não há usuários cadastrados. Crie um usuário primeiro.")
            else:
                cpf = input("Digite o CPF do usuário para criar a conta: ")
                usuario = filtrar_usuario(cpf, usuarios)
                if usuario:
                    criar_conta("0001", numero_conta, usuario, contas)
                    numero_conta += 1
                else:
                    print("Usuário com CPF especificado não encontrado.")

        elif escolha == "6":
            # Listar contas bancárias
            if not contas:
                print("Não há contas bancárias cadastradas. Crie uma conta primeiro.")
            else:
                listar_contas(contas)

        elif escolha == "0":
            print("Obrigado por usar o nosso banco.")
            break

        else:
            print("Opção inválida. Por favor, selecione novamente a operação desejada.")

# Executar a função principal
if __name__ == "__main__":
    main()
