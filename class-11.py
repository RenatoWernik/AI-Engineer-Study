class Conta:
    def __init__(self,titular,saldo):
        
        self.titular = titular
        self.saldo = saldo

    def mostrar_saldo(self):
        print(f"Titular: {self.titular.title()}\nSaldo: {self.saldo}\n")
    

    def depositar(self,deposito):
        self.deposito = deposito
        print(f"Saldo atual: {self.saldo}")
        self.saldo = self.saldo + self.deposito
        print(f"Saldo pós deposito: {self.saldo}")



    

class ContaPremium(Conta):
    def __init__(self,titular,saldo,taxa_juro):
        super().__init__(titular,saldo)
        self.taxa_juro = taxa_juro
    
    def depositar(self,deposito):
        
        super().depositar(deposito)
        self.saldo = self.saldo + (deposito * self.taxa_juro)
        print(f"Juros de {self.taxa_juro * 100}%")
        



cliente_normal = Conta("renato",1900)
cliente_normal.mostrar_saldo()
cliente_normal.depositar(100)




cliente_vip = ContaPremium("elon",20_000,0.02)
cliente_vip.depositar(2_000)
cliente_vip.mostrar_saldo()
