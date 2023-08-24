from classes import *
import os

def main():
    print("Bem vindo! Você está no Hotel ARNI.")
    print("O que deseja?\n[1] Cadastrar-se\n[2] Alugar quartos\n[3] Visualizar quartos")
    escolha = input("- ")

    if escolha == "1":
        print("=== Área de Cadastro ===")
        nomecadastro = input("Nome de usuário: ")
        emailcadastro = input("E-mail: ")
        senhacadastro = input("Senha: ")
        #Salvar nome, email e senha para login depois
        recepcionista.Cadastrar(nomecadastro, emailcadastro, senhacadastro)

    elif escolha == "2":
        print("=== Alugar Quartos ===")
        #Em "classes.py" há uma função que confere se o hotel está disponível para alugar quartos, fazer um if e else disso depois
        print("Insira os dados para login:")
        emaillogin = input("E-mail: ")
        senhalogin = input("Senha: ")
        #Comparar os dados de login se há algum usuário já cadastrado
        if recepcionista.login(emaillogin, senhalogin) == 1:
            print("Bem vindo! \nQuartos Disponíveis:")
            recepcionista.Visualizar()
            x = input("Qual quarto deseja alugar?\n- ") 
            if x == "1":
                recepcionista.LuxoCadastro(emaillogin)
            elif x == "2":
                recepcionista.MasterCadastro(emaillogin)
            elif x == "3":
                recepcionista.DuoCadastro(emaillogin)
            elif x == "4":
                recepcionista.DuoCasalCadastro(emaillogin)
            elif x == "5":
                recepcionista.SimplesCadastro(emaillogin)
            elif x == "6":
                recepcionista.SimplesCasalCadastro(emaillogin)
            else:
                print("O quarto não existe!")
            
        elif recepcionista.login(emaillogin, senhalogin) == 2:
            print("Cliente não existe ou não  encontrado.")


def alugar():
    print("=== Quartos Disponíveis ===")
    #Printar os quartos que estão disponíveis
    #visualizar()