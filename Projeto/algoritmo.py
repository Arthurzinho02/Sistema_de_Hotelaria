from classes import *

def main():
    s = 1
    while s != 1:

        try:
            print("Bem vindos ao Hotel ARNI. Aqui você encontra o que desejar, mas primeiro, o que deseja fazer?\n1 - Cadastro \n2 - Reserva")
            menu_op = int(input(""))

        except Exception as erro:
            print("Valor invalido")
            print(erro.__class__.__name__)