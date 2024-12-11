# Sistema Bancário Simples
class Banco:
    def __init__(self):
        self.contas = {}  # Dicionário para armazenar contas bancárias
        self.historico = {}  # Dicionário para armazenar histórico de transações

    def criar_conta(self, nome, numero_conta, saldo_inicial):
        if numero_conta in self.contas:
            print("Erro: Número da conta já existe!")
            return
        self.contas[numero_conta] = {"nome": nome, "saldo": saldo_inicial}
        self.historico[numero_conta] = []
        print(f"Conta {numero_conta} criada com sucesso para {nome}.")

    def consultar_saldo(self, numero_conta):
        conta = self.contas.get(numero_conta)
        if not conta:
            print("Erro: Conta não encontrada!")
            return
        print(f"Saldo da conta {numero_conta}: R${conta['saldo']:.2f}")

    def depositar(self, numero_conta, valor):
        conta = self.contas.get(numero_conta)
        if not conta:
            print("Erro: Conta não encontrada!")
            return
        if valor <= 0:
            print("Erro: Valor de depósito deve ser positivo!")
            return
        conta["saldo"] += valor
        self.historico[numero_conta].append(f"Depósito de R${valor:.2f}")
        print(f"Depósito de R${valor:.2f} realizado com sucesso. Saldo atual: R${conta['saldo']:.2f}")

    def sacar(self, numero_conta, valor):
        conta = self.contas.get(numero_conta)
        if not conta:
            print("Erro: Conta não encontrada!")
            return
        if valor <= 0:
            print("Erro: Valor de saque deve ser positivo!")
            return
        if conta["saldo"] < valor:
            print("Erro: Saldo insuficiente!")
            return
        conta["saldo"] -= valor
        self.historico[numero_conta].append(f"Saque de R${valor:.2f}")
        print(f"Saque de R${valor:.2f} realizado com sucesso. Saldo atual: R${conta['saldo']:.2f}")

    def encerrar_conta(self, numero_conta):
        conta = self.contas.get(numero_conta)
        if not conta:
            print("Erro: Conta não encontrada!")
            return
        if conta["saldo"] != 0:
            print("Erro: A conta deve ter saldo zerado para ser encerrada!")
            return
        del self.contas[numero_conta]
        del self.historico[numero_conta]
        print(f"Conta {numero_conta} encerrada com sucesso.")

    def exibir_historico(self, numero_conta):
        if numero_conta not in self.historico:
            print("Erro: Conta não encontrada!")
            return
        print(f"Histórico de transações da conta {numero_conta}:")
        for transacao in self.historico[numero_conta]:
            print(f"- {transacao}")


# Demonstração do Sistema Bancário
banco = Banco()

# Menu interativo
while True:
    print("\n--- Sistema Bancário ---")
    print("1. Criar Conta")
    print("2. Consultar Saldo")
    print("3. Depositar")
    print("4. Sacar")
    print("5. Encerrar Conta")
    print("6. Exibir Histórico")
    print("7. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do cliente: ")
        numero_conta = input("Número da conta: ")
        saldo_inicial = float(input("Saldo inicial: "))
        banco.criar_conta(nome, numero_conta, saldo_inicial)
    elif opcao == "2":
        numero_conta = input("Número da conta: ")
        banco.consultar_saldo(numero_conta)
    elif opcao == "3":
        numero_conta = input("Número da conta: ")
        valor = float(input("Valor do depósito: "))
        banco.depositar(numero_conta, valor)
    elif opcao == "4":
        numero_conta = input("Número da conta: ")
        valor = float(input("Valor do saque: "))
        banco.sacar(numero_conta, valor)
    elif opcao == "5":
        numero_conta = input("Número da conta: ")
        banco.encerrar_conta(numero_conta)
    elif opcao == "6":
        numero_conta = input("Número da conta: ")
        banco.exibir_historico(numero_conta)
    elif opcao == "7":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida! Tente novamente.")
