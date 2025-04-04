class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print(f"Saldo de ${self.saldo} do titular ${self.titular}")

    def deposita(self, valor):
        self.saldo += valor

    def saque(self, valor):
        self.saldo -= valor

    def transfere(self, valor, destino):
        self.saque(valor)
        destino.deposita(valor)

    