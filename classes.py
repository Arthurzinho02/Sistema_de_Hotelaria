class Cliente:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

    def getNome(self):
        return self.nome
    
    def getEmail(self):
        return self.email
    
    def getSenha(self):
        return self.senha
    
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
        self.quartos = ["Luxo", "Master", "Simples", "Simples Casal", "Duo", "Duo Casal"]

    def Quartos(self):
        cont = 0
        for i in self.quartos:
            cont += 1
            print(f"{cont} - {i}")
    
    def Visualizar(self):
        print(f"[1]Luxo: {self.limluxo} \n[2]Master: {self.limmaster} \n[3]Simples: {self.limsimples} \n[4]Simples Casal: {self.limsimplescasal} \n[5]Duplo Simples: {self.limduo} \n[6]Duplo Casal: {self.limduocasal}")
        
    def Cadastrar(self, nome, email, senha):
        cliente = Cliente(nome, email, senha)
        self.nomes.append(cliente)

    def login(self, email, senha):
        for cliente in self.nomes:
            if cliente.getEmail() == email  and cliente.getSenha() == senha:
                return 1
            
    def getNomeC(self, email):
        for cliente in self.nomes:
            if cliente.getEmail() == email:
                return cliente.getNome()
    

class Quartos(Hotel):
    def ClienteVisualizar(self, email):
        cont = 0
        for chave, valor in self.clientes.items():
            if chave.getEmail() == email:
                cont += 1
                print(f"{cont} - {valor}")
            
        
    def Cancelar(self, email, vetorQ):
        for chave, valor in self.clientes.items():
            if chave.getEmail() == email and valor == self.quartos[vetorQ - 1]:
                self.clientes.pop(chave)
                break
                    
                
        
    def LuxoCadastro(self, email):
        if self.limluxo <= 2 and self.limluxo > 0:
            for cliente in self.nomes:
                if cliente.getEmail() == email:
                    self.clientes[cliente] = self.quartos[0]
                    self.limluxo = self.limluxo - 1
                    print(f"Quarto de Luxo alugado por {cliente.getNome()}")
                else:
                    print("Cliente não encontrado")
        else:
            print("Indisponível")

    def MasterCadastro(self, email):
        if self.limmaster <= 2 and self.limmaster > 0:
            for cliente in self.nomes:
                if cliente.getEmail() == email:
                    self.clientes[cliente] = self.quartos[1]
                    self.limmaster = self.limmaster - 1
                    print(f"Quarto Master alugado por {cliente.getNome()}")
                else:
                    print("Cliente não encontrado")
        else:
            print("Indisponível")

    def SimplesCadastro(self, email):
        if self.limsimples <= 3 and self.limsimples > 0:
            for cliente in self.nomes:
                if cliente.getEmail() == email:
                    self.clientes[cliente] = self.quartos[2]
                    self.limsimples = self.limsimples - 1
                    print(f"Quarto simples alugado por {cliente.getNome()}")
                else:
                    print("Cliente não encontrado")
        else:
            print("Indisponível")

    def SimplesCasalCadastro(self, email):
        if self.limsimplescasal <= 3 and self.limsimplescasal > 0:
            for cliente in self.nomes:
                if cliente.getEmail() == email:
                    self.clientes[cliente] = self.quartos[3]
                    self.limsimplescasal = self.limsimplescasal - 1
                    print(f"Quarto Simples de Casal alugado por {cliente.getNome()}")
                else:
                    print("Cliente não encontrado")
        else:
            print("Indisponível")

    def DuoCadastro(self, email):
        if self.limduo <= 3 and self.limduo > 0:
            for cliente in self.nomes:
                if cliente.getEmail() == email:
                    self.clientes[cliente] = self.quartos[4]
                    self.limduo = self.limduo - 1
                    print(f"Quarto duplo alugado por {cliente.getNome()}")
                else:
                    print("Cliente não encontrado")
        else:
            print("Indisponível")

    def DuoCasalCadastro(self, email):
        if self.limduocasal <= 3 and self.limduocasal > 0:
            for cliente in self.nomes:
                if cliente.getEmail() == email:
                    self.clientes[cliente] = self.quartos[5]
                    self.limduocasal = self.limduo - 1
                    print(f"Quarto Duo de Casal alugado por {cliente.getNome()}")
                else:
                    print("Cliente não encontrado")
        else:
            print("Indisponível")


recepcionista = Quartos()