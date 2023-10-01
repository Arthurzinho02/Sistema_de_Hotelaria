from classes import *
import os

def main():
    y = 1
    while y == 1:
        try:
            print("Bem vindo! Você está no Hotel ARNI.")
            print("O que deseja?\n[1] Cadastrar-se\n[2] Alugar quartos\n[3] Cancelamento de reserva\n[4] Visualizar Reservas\n[5] Sair")
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
                    print("Bem vindo!\nQuartos Disponíveis:\n")
                    recepcionista.Visualizar()

                    x = input("\nQual quarto deseja alugar?\n- ")

                    if x == "1":
                        recepcionista.LuxoCadastro(emaillogin)
                        os.system("pause")
                        os.system("cls")

                    elif x == "2":
                        recepcionista.MasterCadastro(emaillogin)
                        os.system("pause")
                        os.system("cls")

                    elif x == "3":
                        recepcionista.SimplesCadastro(emaillogin)
                        os.system("pause")
                        os.system("cls")

                    elif x == "4":
                        recepcionista.SimplesCasalCadastro(emaillogin)
                        os.system("pause")
                        os.system("cls")

                    elif x == "5":
                        recepcionista.DuoCadastro(emaillogin)
                        os.system("pause")
                        os.system("cls")

                    elif x == "6":
                        recepcionista.DuoCasalCadastro(emaillogin)
                        os.system("pause")
                        os.system("cls")

                    else:
                        print("O quarto não existe.")
                    
                elif recepcionista.login(emaillogin, senhalogin) == 2:
                    print("Cliente não existe ou não foi encontrado.")
                    os.system("pause")
                    os.system("cls")

            elif escolha == "3":
                print ("=== Cancelamento de Reserva ===") 
                print ("Insira os seus dados para realizar o cancelamento:")
                emaillogin = input("E-mail: ")
                senhalogin = input("Senha: ")
                recepcionista.Cancelar(emaillogin, senhalogin)

            elif escolha == "4":
                print ("=== Visualizar Reservas ===")
                recepcionista.ClienteVisualizar()

            elif escolha == "5":
                y = 0
                
        except Exception as erro:
            print(f"O erro é: {erro.__class__.__name__}")