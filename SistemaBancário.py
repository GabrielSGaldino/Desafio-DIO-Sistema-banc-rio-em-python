class ContaBancaria:
    def __init__(self):
        self.saldo = 0
        self.transacoes = []
        self.numero_saques = 0
        self.LIMITE_SAQUES = 2
        self.limite = 500

    def deposito(self):
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            self.saldo += valor
            self.transacoes.append(('Depósito', valor))
        else:
            print("Operação falhou! O valor informado é inválido. Tente novamente!")

    def saque(self):
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > self.saldo
        excedeu_limite = valor > self.limite
        excedeu_saques = self.numero_saques >= self.LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não possui saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excedeu o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número de saques foi excedido.")
        elif valor > 0:
            self.saldo -= valor
            self.transacoes.append(('Saque', -valor))
            self.numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")

    def extrato(self):
        print("\n=============EXTRATO==============")
        for transacao, valor in self.transacoes:
            print(f'{transacao}: R$ {valor:.2f}')
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("===============================")

conta = ContaBancaria()
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

while True:
    opcao = input(menu)
    if opcao == "d":
        conta.deposito()
    elif opcao == 's':
        conta.saque()
    elif opcao == "e":
        conta.extrato()
    elif opcao =="q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
