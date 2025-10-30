class Conta:
    def __init__(self, titular, numero, saldo):
        self.saldo = 0.0
        self.titular = titular
        self.numero = numero

        @property
        def valor(self):
            return self.saldo

        @saldo.setter
        def saldo(self, saldo):
            if(self.saldo>= valor):
                self.saldo-= saldo
                print("Saque realizado com sucesso")
            else:
                print("Saldo insuficiente")

        def deposita(self,valor):
            self.saldo += valor

        def extrato(self):
            print("Cliente: ",self._titular, " Saldo Atual: ",self._saldo)
