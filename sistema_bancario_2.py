class Endereco:
    def __init__(self, logradouro, numero, bairro, cidade_sigla, estado):
        self.logradouro = logradouro
        self.numero = numero
        self.bairro = bairro
        self.cidade_sigla = cidade_sigla
        self.estado = estado


class Usuario:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco
        self.contas = []

    def cadastrar_conta(self, agencia, numero_conta):
        conta = ContaBancaria(agencia, numero_conta, self)
        self.contas.append(conta)
        return conta


class ContaBancaria:
    def __init__(self, agencia, numero_conta, usuario):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.usuario = usuario
        self.saldo = 0
        self.transacoes = []
        self.limite = 1000
        self.numero_saques = 0
        self.limite_saques = 5

    def deposito(self, valor):
        self.saldo += valor
        self.transacoes.append(f"Depósito: +{valor}")
        return self.saldo, self.transacoes

    def saque(self, valor):
        if self.saldo - valor >= -self.limite and self.numero_saques < self.limite_saques:
            self.saldo -= valor
            self.transacoes.append(f"Saque: -{valor}")
            self.numero_saques += 1
            return self.saldo, self.transacoes
        else:
            return "Saldo insuficiente ou limite de saques atingido."

    def obter_extrato(self):
        return self.saldo, self.transacoes


# Funções de Cadastro e Operações

usuarios = []

def cadastrar_usuario(nome, data_nascimento, cpf, endereco):
    if not any(user.cpf == cpf for user in usuarios):
        endereco_obj = Endereco(*endereco)
        usuario = Usuario(nome, data_nascimento, cpf, endereco_obj)
        usuarios.append(usuario)
        return usuario
    else:
        return "CPF já cadastrado."

def buscar_usuario_por_cpf(cpf):
    for usuario in usuarios:
        if usuario.cpf == cpf:
            return usuario
    return None

# Exemplo de Uso

print("\nBem vindo ao Banco Santos!\n")

while True:
    print("1 - Criar conta")
    print("2 - Cadastro do usuário")
    print("0 - Sair\n")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("\nNome: ")
        data_nascimento = input("Data de Nascimento: ")
        cpf = input("CPF: ")
        endereco = [
            input("Logradouro: "),
            input("Número: "),
            input("Bairro: "),
            input("Cidade/Sigla: "),
            input("Estado: ")
        ]
        novo_usuario = cadastrar_usuario(nome, data_nascimento, cpf, endereco)
        if novo_usuario:
            print(f"\nUsuário {novo_usuario.nome} cadastrado com sucesso!\n")
        else:
            print("\nCPF já cadastrado.")

    elif opcao == "2":
        cpf = input("\nCPF do usuário: ")
        usuario = buscar_usuario_por_cpf(cpf)
        if usuario:
            print(f"\nBem vindo, {usuario.nome}!")
            while True:
                print("\nBem vindo,", usuario.nome)
                print("\n1 - Depósito")
                print("2 - Saque")
                print("3 - Extrato")
                print("0 - Sair")
                opcao_usuario = input("\nEscolha uma opção: ")

                if opcao_usuario == "1":
                    valor = float(input("\nValor do depósito: "))
                    if not usuario.contas:
                        agencia = "0001"  # Agência fixa
                        numero_conta = 1  # Número da primeira conta
                        usuario.cadastrar_conta(agencia, numero_conta)
                    saldo, transacoes = usuario.contas[0].deposito(valor)
                    print(f"Depósito realizado. Novo saldo: {saldo}")
                    print("Transações:", transacoes)

                elif opcao_usuario == "2":
                    valor = float(input("\nValor do saque: "))
                    if not usuario.contas:
                        print("Nenhuma conta cadastrada.")
                        continue
                    saldo, transacoes = usuario.contas[0].saque(valor)
                    if isinstance(saldo, float):
                        print(f"Saque realizado. Novo saldo: {saldo}")
                        print("Transações:", transacoes)
                    else:
                        print(saldo)

                elif opcao_usuario == "3":
                    if not usuario.contas:
                        print("Nenhuma conta cadastrada.")
                        continue
                    saldo, transacoes = usuario.contas[0].obter_extrato()
                    print(f"\nSaldo: {saldo}")
                    print("Transações:", transacoes)

                elif opcao_usuario == "0":
                    break
        else:
            print("Usuário não encontrado.")

    elif opcao == "0":
        break

print("Obrigado por utilizar o Banco Santos!")
