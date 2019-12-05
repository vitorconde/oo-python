class Conta:

    #__init__ é o constructor
    #self é a referencia do objeto na memória
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo o Objeto... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Titular : {} <-> Saldo : {}".format(self.__titular, self.__saldo))

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
