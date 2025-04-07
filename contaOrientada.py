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

    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, limite):
        self._limite = limite

    