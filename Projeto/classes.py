class Cliente:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
    
class Hotel:
    def __init__(self):
        self.clientes = {} # Dicionario de clientes
        self.nomes = [] # Lista de nomes
        self.limluxo = 2
        self.limmaster = 2
        self.limsimples = 3
        self.limsimplescasal = 3
        self.limduo = 3
        self.limduocasal = 3
    
    def Visualizar(self):
        print(f"[1]Luxo: {self.limluxo} \n[2]Master: {self.limmaster} \n[3]Simples: {self.limsimples} \n[4]Simples Casal: {self.limsimplescasal} \n[5]Duplo Simples: {self.limduo} \n[6]Duplo Casal: {self.limduocasal}")
        
    def Cadastrar(self, nome, email, senha):
        cliente = Cliente(nome, email, senha)
        self.nomes.append(cliente)

    def login(self, email, senha):
        for cliente in self.nomes:
            if cliente.email == email  and cliente.senha == senha:
                return 1
            else:
                return 2

class Quartos(Hotel):
    def clientevizualizar(self, email):
        for chave, valor in self.clientes.items():
            if chave == email:
                print(f"{chave} | {valor}")
            else:
                print("E-mail não encontrado")
        
    def desmarcar(self, email, quarto):
        for chave, valor in self.clientes.items():
            if chave == email:
                if valor == quarto:
                    self.clientes.pop(chave)
                    print(f"Quarto {quarto} excluido")
                else:
                    print("Quarto não encontrado")
            else:
                print("Cliente não encontrado")
                
        
    def LuxoCadastro(self, email):
        if self.limluxo <= 2 and self.limluxo > 0:
            for cliente in self.nomes:
                if cliente.email == email:
                    self.clientes[cliente.email] = "LUXO"
                    self.limluxo = self.limluxo - 1
                    print(f"Quarto de Luxo alugado por {cliente.nome}")
                else:
                    print("Cliente não encontrado")
        else:
            print("Indisponível")

    def MasterCadastro(self, email):
        if self.limmaster <= 2 and self.limmaster > 0:
            for cliente in self.nomes:
                if cliente.email == email:
                    self.clientes[cliente.email] = "MASTER"
                    self.limmaster = self.limmaster - 1
                    print(f"Quarto Master alugado por {cliente.nome}")
                else:
                    print("Cliente não encontrado")
        else:
            print("Indisponível")

    def SimplesCadastro(self, email):
        if self.limsimples <= 3 and self.limsimples > 0:
            for cliente in self.nomes:
                if cliente.email == email:
                    self.clientes[cliente.email] = "SIMPLES"
                    self.limsimples = self.limsimples - 1
                    print(f"Quarto simples alugado por {cliente.nome}")
                else:
                    print("Cliente não encontrado")
        else:
            print("Indisponível")

    def SimplesCasalCadastro(self, email):
        if self.limsimplescasal <= 3 and self.limsimplescasal > 0:
            for cliente in self.nomes:
                if cliente.email == email:
                    self.clientes[cliente.email] = "SIMPLES CASAL"
                    self.limsimplescasal = self.limsimplescasal - 1
                    print(f"Quarto Simples de Casal alugado por {cliente.nome}")
                else:
                    print("Cliente não encontrado")
        else:
            print("Indisponível")

    def DuoCadastro(self, email):
        if self.limduo <= 3 and self.limduo > 0:
            for cliente in self.nomes:
                if cliente.email == email:
                    self.clientes[cliente.email] = "DUO"
                    self.limduo = self.limduo - 1
                    print(f"Quarto duplo alugado por {cliente.nome}")
                else:
                    print("Cliente não encontrado")
        else:
            print("Indisponível")

    def DuoCasalCadastro(self, email):
        if self.limduocasal <= 3 and self.limduocasal > 0:
            for cliente in self.nomes:
                if cliente.email == email:
                    self.clientes[cliente.email] = "DUO CASAL"
                    self.limduocasal = self.limduo - 1
                    print(f"Quarto Duo de Casal alugado por {cliente.nome}")
                else:
                    print("Cliente não encontrado")
        else:
            print("Indisponível")


recepcionista = Quartos()
