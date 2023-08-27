from classes import *
import os

def main():
    print("Bem vindo! Você está no Hotel ARNI.")

    y = 1
    while y == 1:
        try:
            print("O que deseja?\n[1] Cadastrar-se\n[2] Alugar quartos\n[3] Cancelamento de reserva\n[4] Sair")
            escolha = input("- ")
            os.system("cls")

            if escolha == "1":
                print("=== Área de Cadastro ===")
                nomecadastro = input("Nome de usuário: ")
                emailcadastro = input("E-mail: ")
                senhacadastro = input("Senha: ")
                recepcionista.Cadastrar(nomecadastro, emailcadastro, senhacadastro)
                os.system("cls")
                print("Parabéns! Você foi cadastrado com sucesso. ")
                print("As seguintes informações de sua conta foram salvas:")
                print(f"Usuário: {nomecadastro}\nE-mail: {emailcadastro}\nSenha: {senhacadastro}")
                os.system("pause")
                os.system("cls")

            elif escolha == "2":
                print("=== Alugar Quartos ===")
                print("Insira os dados para login:")
                emaillogin = input("E-mail: ")
                senhalogin = input("Senha: ")
                os.system("cls")

                if recepcionista.login(emaillogin, senhalogin) == 1:
                    print("Bem vindo!\nQuartos Disponíveis:")
                    recepcionista.Visualizar()

                    x = input("Qual quarto deseja alugar?\n- ")

                    if x == "1":
                        recepcionista.LuxoCadastro(emaillogin)

                    elif x == "2":
                        recepcionista.MasterCadastro(emaillogin)

                    elif x == "3":
                        recepcionista.SimplesCadastro(emaillogin)

                    elif x == "4":
                        recepcionista.SimplesCasalCadastro(emaillogin)

                    elif x == "5":
                        recepcionista.DuoCadastro(emaillogin)

                    elif x == "6":
                        recepcionista.DuoCasalCadastro(emaillogin)

                    else:
                        print("O quarto não existe.")
                    
                    os.system("pause")
                    os.system("cls")
                    
                elif recepcionista.login(emaillogin, senhalogin) == 2:
                    print("Cliente não existe ou não foi encontrado.")
                    os.system("pause")

            elif escolha == "3":
                print ("=== Cancelamento de Reserva ===") 
                print ("Insira os seus dados para realizar o cancelamento:")
                emaillogin = input("E-mail: ")
                senhalogin = input("Senha: ")
                recepcionista.Cancelar(emaillogin, senhalogin)
                print("Seu cancelamento foi realizado com sucesso!")

            elif escolha == "4":
                y = 0
                
        except Exception as erro:
            print(f"O erro é: {erro.__class__.__name__}")