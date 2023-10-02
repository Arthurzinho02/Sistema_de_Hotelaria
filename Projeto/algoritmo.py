from classes import *
import os

def main():
    while True:
        try:
            print("Bem vindo! Você está no Hotel ARNI.")
            print("O que deseja?\n[1] Login \n[2] Cadastrar \n[3] Sair")
            escolha = int(input(">> "))
            os.system("cls")
            match escolha:
                case 1:
                    print("=== Login ===")
                    print("Insira os dados para login:")
                    emaillogin = input("E-mail: ")
                    senhalogin = input("Senha: ")
                    os.system("cls")

                    match recepcionista.login(emaillogin, senhalogin):
                        case 1:
                                while True:
                                    print(f"=== Bem vindo {recepcionista.getNomeC(emaillogin)}===")
                                    print("Deseja: \n[1] Vizualizar quartos \n[2] Alugar \n[3] Cancelar Reserva \n[4] Ver reservas \n[5] Sair")
                                    opção = int(input(">> "))
                                    os.system("cls")

                                    match opção:
                                        case 1:
                                            print("=== Quartos ===")
                                            recepcionista.Visualizar()
                                            os.system("pause")
                                            os.system("cls")

                                        case 2:
                                            print("=== Bem vindo ===\nQuartos Disponíveis:\n")
                                            recepcionista.Visualizar()

                                            x = int(input("\nQual quarto deseja alugar?\n>> "))
                                            match x:

                                                case 1:
                                                    recepcionista.LuxoCadastro(emaillogin)
                                                    os.system("pause")
                                                    os.system("cls")

                                                case 2:
                                                    recepcionista.MasterCadastro(emaillogin)
                                                    os.system("pause")
                                                    os.system("cls")

                                                case 3:
                                                    recepcionista.SimplesCadastro(emaillogin)
                                                    os.system("pause")
                                                    os.system("cls")

                                                case 4:
                                                    recepcionista.SimplesCasalCadastro(emaillogin)
                                                    os.system("pause")
                                                    os.system("cls")

                                                case 5:
                                                    recepcionista.DuoCadastro(emaillogin)
                                                    os.system("pause")
                                                    os.system("cls")

                                                case 6:
                                                    recepcionista.DuoCasalCadastro(emaillogin)
                                                    os.system("pause")
                                                    os.system("cls")

                                                case _:
                                                    print("O quarto não existe.")
                                                    os.system("pause")
                                                    os.system("cls")
                                    
                                        case 3:
                                            print ("=== Cancelamento de Reserva ===") 
                                            recepcionista.ClienteVisualizar(emaillogin)
                                            vetor = int(input("Digite o índice do quarto a ser excluido: "))
                                            recepcionista.Cancelar(emaillogin, vetor)
                                            print("Quarto excluido")
                                            os.system("pause")
                                            os.system("cls")

                                        case 4:
                                            print ("=== Visualizar Reservas ===")
                                            recepcionista.ClienteVisualizar(emaillogin)
                                            os.system("pause")
                                            os.system("cls")

                                        case 5:
                                            break

                                        case _:
                                            print("Inválido")
                                            os.system("pause")
                                            os.system("cls")
                        case _:
                            print("Senha ou email incorretos")
                case 2:
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

                case 3:
                    break

                case _:
                    print("Inválido")
                    os.system("pause")
                    os.system("cls")
                
        except Exception as erro:
            print(f"O erro é: {erro.__class__.__name__}")