from classes import *

def main():
    print("Esse é um Sistema de Hotelaria.")
    print("Você deseja:\n[1] Cadastrar-se\n[2] Alugar quartos")
    escolha = input("- ")

    if escolha == "1":
        print("===Área de Cadastro===")
        nomecadastro = input("Nome de usuário: ")
        emailcadastro = input("E-mail: ")
        senhacadastro = input("Senha: ")
        #Salvar nome, email e senha para login depois
        hotel.cadastrar(nomecadastro, emailcadastro, senhacadastro)

    elif escolha == "2":
        print("===Alugar quartos===")
        #Em "classes.py" há uma função que confere se o hotel está disponível para alugar quartos, fazer um if e else disso depois
        print("Insira os dados para login:")
        emaillogin = input("")
        senhalogin = input("")
        #Comparar os dados de login se há algum usuário já cadastrado
        if emailcadastro == emaillogin and senhacadastro == senhalogin:
            print("Você fez o Login.")
            #alugar() função que vai servir para fazer a escolha dos quartos
        elif emailcadastro != emaillogin or senhacadastro != senhalogin:
            print("Alguma das informações está incorreta ou o usuário não está cadastrado.")
            escolha = "2" #Vai voltar pra área de alugar quartos
        
def alugar():
    print("===Quartos Disponíveis===")
    #Printar os quartos que estão disponíveis
    #visualizar()