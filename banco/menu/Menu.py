from banco.conta.ContaPoupanca import ContaPoupanca
from banco.conta.ContaCorrente import ContaCorrente
from banco.extrato.Extrato import Extrato
from banco.usuario.PessoaFisica import PessoaFisica

class Menu:
    def __init__(self):
        pass

    @classmethod
    def get_menu(self):
        def menu():
            print("\n---------- BANCO PYTHON ----------\n")
            print("1 - CADASTRAR USUÁRIO")
            print("2 - CRIAR CONTA")
            print("3 - DEPOSITAR")
            print("4 - SACAR")
            print("5 - EXTRATO")
            print("6 - SAIR")
            print("\n-------------- FIM ---------------\n")
        menu()

        while True:
            opcoes = input("DIGITE A OPÇÃO: ")
            if opcoes == "1":
                nome = input("DIGITE SEU NOME: ")
                cpf = input("DIGITE SEU CPF: ")
                pessoa_fisica = PessoaFisica(nome, cpf)
                print("\nUsuário cadastrado com sucesso!")
                menu()
            elif opcoes == "2":
                try:
                    cpf = input("DIGITE SEU CPF: ")
                    if cpf == pessoa_fisica.get_cpf():    
                        print("----------------------------------")
                        print("1 - Conta Corrente")
                        print("2 - Conta Poupança")
                        print("----------------------------------")
                        escolha = input("ESCOLHA O TIPO DE CONTA: ")
                        if escolha == "1":
                            conta_corrente = ContaCorrente(pessoa_fisica)
                            print("\nConta Corrente criada com sucesso.")
                        elif escolha == "2":
                            conta_poupanca = ContaPoupanca(pessoa_fisica)
                            print("\nConta Poupança criada com sucesso!")  
                        else:
                            print("Escolha inválida!")      
                    else:
                        print("Cpf não encontrado. Cadastre-se na opção 1")    
                except:
                    print("Cpf não encontrado. Cadastre-se na opção 1.")
                menu()   
            elif opcoes == "3":
                try:
                    if escolha == "1":
                        print("----------------------------------")
                        valor_deposito = float(input("DIGITE O VALOR DO DEPÓSITO: "))
                        print("----------------------------------")
                        conta_corrente.depositar(valor_deposito)
                        print("Valor depositado na conta corrente com sucesso!")
                        menu()      
                    if escolha == "2":
                        print("----------------------------------")
                        valor_deposito = float(input("DIGITE O VALOR DO DEPÓSITO: "))
                        print("----------------------------------")
                        conta_poupanca.depositar(valor_deposito)
                        print("Valor depositado na conta poupança com sucesso!")
                        menu()    
                except:
                    print("A opção depósito não é válida sem uma conta criada.")         
            elif opcoes == "4":
                try:
                    if escolha == "1":
                        print("----------------------------------")
                        valor_saque = float(input("DIGITE O VALOR DO SAQUE: "))
                        print("----------------------------------")
                        conta_corrente.sacar(valor_saque)
                        print("Valor sacado da conta corrente com sucesso!")
                        menu()    
                    if escolha == "2":
                        print("----------------------------------")
                        valor_saque = float(input("DIGITE O VALOR DO SAQUE: "))
                        print("----------------------------------")
                        conta_poupanca.sacar(valor_saque)
                        print("Valor sacado da conta poupança com sucesso!")
                        menu()    
                except:
                    print("A opção saque não é válida sem uma conta criada.") 
            elif opcoes == "5":   
                try:      
                    if escolha == "1":
                        Extrato.get_extrato(conta_corrente)
                    elif escolha == "2":
                        Extrato.get_extrato(conta_poupanca)    
                    else:
                        print("Escolha inválida")    
                except:
                    print("A opção Extrato não é válida sem uma conta criada.")             
            elif opcoes == "6": 
                print("OBIGADO E VOLTE SEMPRE!")
                exit()   
            else:
                print("Opção inválida!")        
            