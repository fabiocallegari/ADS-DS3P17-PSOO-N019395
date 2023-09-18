class ContaBancaria:
    def __init__(self, numero_da_conta, saldo_inicial):
        self.numero_da_conta = numero_da_conta
        self.saldo = saldo_inicial

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")

    def consultar_saldo(self):
        return self.saldo

class Cliente:
    def __init__(self, nome, numero_da_conta):
        self.nome = nome
        self.numero_da_conta = numero_da_conta
        self.conta_bancaria = None

    def abrir_conta(self, numero_da_conta, saldo_inicial):
        self.conta_bancaria = ContaBancaria(numero_da_conta, saldo_inicial)

    def fechar_conta(self):
        self.conta_bancaria = None

    def get_nome(self):
        return self.nome

    def get_numero_da_conta(self):
        return self.numero_da_conta

    def get_conta_bancaria(self):
        return self.conta_bancaria

# Exemplo:

cliente1 = Cliente("João", 12345)
cliente1.abrir_conta(987654, 1000.0)

cliente2 = Cliente("Maria", 54321)
cliente2.abrir_conta(456789, 500.0)

print(f"Nome do Cliente 1: {cliente1.get_nome()}")
print(f"Número do Cliente 1: {cliente1.get_numero_da_conta()}")
print(f"Saldo da Conta do Cliente 1: {cliente1.get_conta_bancaria().consultar_saldo()}")

print(f"Nome do Cliente 2: {cliente2.get_nome()}")
print(f"Número do Cliente 2: {cliente2.get_numero_da_conta()}")
print(f"Saldo da Conta do Cliente 2: {cliente2.get_conta_bancaria().consultar_saldo()}")
