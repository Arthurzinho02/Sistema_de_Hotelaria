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
    
    def Visualizar(self):
        print(f"Luxo: {self.limluxo} \nMaster: {self.limmaster} \nSimples: {self.limsimples} \nSimples Casal: {self.limsimplescasal} \nDuplo Simples: {self.limduo} \nDuplo Casal: {self.limduocasal}")
    
    def Cadastrar(self, nome, email, senha):
        if len(self.clientes) < self.limitehotel:
            cliente = Cliente(nome, email, senha)
            self.nomes.append(cliente)
        else:
            print("Não tem quartos disponíveis")
    

class Luxo(Hotel):
    def LuxoCadastro(self, email):
        if self.limluxo <= 2 and self.limluxo > 0:
            for cliente in self.nomes:
                if cliente.email == email:
                    self.clientes[cliente] = "luxo"
                    self.limluxo = self.limluxo - 1
                    print(f"Quarto de Luxo alugado por {cliente.nome}")
                else:
                    print("Cliente não encontrado")
        else:
            print("Indisponível")

class Master(Hotel):
    def MasterCadastro(self, email):
        if self.limmaster <= 2 and self.limmaster > 0:
            for cliente in self.nomes:
                if cliente.email == email:
                    self.clientes[cliente] = "luxo"
                    self.limmaster = self.limmaster - 1
                    print(f"Quarto Master alugado por {cliente.nome}")
                else:
                    print("Cliente não encontrado")
        else:
            print("Indisponível")

class Simples(Hotel):
    def SimplesCadastro(self, email):
        if self.limsimples <= 3 and self.limsimples > 0:
            for cliente in self.nomes:
                if cliente.email == email:
                    self.clientes[cliente] = "luxo"
                    self.limsimples = self.limsimples - 1
                    print(f"Quarto simples alugado por {cliente.nome}")
                else:
                    print("Cliente não encontrado")
        else:
            print("Indisponível")

class SimplesCasal(Hotel):
    def SimplesCasalCadastro(self, email):
        if self.limsimplescasal <= 3 and self.limsimplescasal > 0:
            for cliente in self.nomes:
                if cliente.email == email:
                    self.clientes[cliente] = "luxo"
                    self.limsimplescasal = self.limsimplescasal - 1
                    print(f"Quarto Simples de Casal alugado por {cliente.nome}")
                else:
                    print("Cliente não encontrado")
        else:
            print("Indisponível")

class Duo(Hotel):
    def DuoCadastro(self, email):
        if self.limduo <= 3 and self.limduo > 0:
            for cliente in self.nomes:
                if cliente.email == email:
                    self.clientes[cliente] = "luxo"
                    self.limduo = self.limduo - 1
                    print(f"Quarto duplo alugado por {cliente.nome}")
                else:
                    print("Cliente não encontrado")
        else:
            print("Indisponível")

class DuoCasal(Hotel):
    def DuoCasalCadastro(self, email):
        if self.limduocasal <= 3 and self.limduocasal > 0:
            for cliente in self.nomes:
                if cliente.email == email:
                    self.clientes[cliente] = "luxo"
                    self.limduocasal = self.limduo - 1
                    print(f"Quarto Duo de Casal alugado por {cliente.nome}")
                else:
                    print("Cliente não encontrado")
        else:
            print("Indisponível")


hotel = Hotel()


