class Contas:
    def __init__(self,numero,senha,saldo = 0):
        self.numero = numero
        self.saldo = saldo
        self.senha = senha

    def depositar(self,valor):
        if valor <= 0:
            return False
        else:
            self.saldo += valor

    def saque(self,valor):
        if valor < 0:
            valor *= -1
        if self.saldo >= valor:
            self.saldo -= valor
            return True
        else:
            return False

    def transferir(self,alvo,valor):
        if valor < 0:
            valor *= -1
        if self.numero != alvo.numero:
            if self.saque(valor) == True:
                alvo.depositar(valor)
                return True
            else:
                return False
    def mostrarConta(self):
        return f"""
NUMERO DA CONTA -> {self.numero}
SALDO DA CONTA -> R${self.saldo}

"""

