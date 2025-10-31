class Main:
    pass

from Cliente import  Cliente

from Conta import Conta

c1 = Cliente("Arthur", "6198266-4172")
conta= Conta(c1.get_nome(), 6565, 0)

conta.deposita(100)
conta.saque(50)
conta.extrato()