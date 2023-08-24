class Cliente:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

    
class Hotel:
    def __init__(self):
        self.limitehotel = 16
        self.clientes = {}
        self.nomes = []
        self.limluxo = 2
        self.limmaster = 2
        self.limsimples = 3
        self.limsimplescasal = 3
        self.limduo = 3
        self.limduocasal = 3
    
    def visualizar(self):
        print(f"Luxo: {self.limluxo} \nMaster: {self.limmaster} \nSimples: {self.limsimples} \nSimples Casal: {self.limsimplescasal} \nDuplo Simples: {self.limduo} \nDuplo Casal: {self.limduocasal}")
    
    def cadastrar(self, nome, email, senha):
        if len(self.clientes) < self.limitehotel:
            cliente = Cliente(nome, email, senha)
            self.nomes.append(cliente)
        else:
            print("Não tem quartos disponíveis")
    

class Luxo(Hotel):
    def luxocadastro(self, email):
        if self.limluxo <= 2 and self.limluxo > 0:
            for cliente in self.nomes:
                if cliente.email == email:
                    self.clientes[cliente] = "luxo"
                    self.limluxo = self.limluxo - 1
                else:
                    print("Cliente não encontrado")
        else:
            print("Indisponível")

class master()

        
hotel = Hotel()

oi = Luxo()
oi.luxocadastro("arthur", "arthur@gmail.com", 12345)

