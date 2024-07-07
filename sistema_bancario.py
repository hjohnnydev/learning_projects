import os
from time import sleep

saldo = 300.00
numero_saques = 0
LIMITE_SAQUES = 3
LIMITE_SAQUE_VALOR = 500.00
deposito = 0
extrato = f"Saldo inicial: R$ {saldo:.2f}\nOperaçoes:\n"
opcao = ""
saque = 0
operacao = 0

def menu_print():
    sleep(1)
    os.system('cls')
    print(""" ********** Menu **********
         
    Opcoes:

    (S) - Saque
    (D) - Deposito
    (E) - Extrato
    (Q) - Sair
          
 **************************
          """)

def saldo_valor(saldo):
    print(f"Seu saldo e de: R$ {saldo:.2f}.\n")

def conf_opcao():
    while True:
        opc = input("(Y/N) ")
        opc = opc.capitalize()
        if opc == "Y":
            break
        elif opc == "N":
            break
        else:
            print("Opcao Invalida.\n")

    return opc

def sist_off():
    print("********** Fechando o sistema **********\n\n       Agradecemos a preferência\n")
    sleep(2)
    os.system('cls')

while True:
    menu_print()
    
    opcao = input("Selecione uma opcao: ")
    opcao = opcao.capitalize()

    if opcao == "S": # Saque
        menu_print()
        print(f"********** Operacao Saque **********\n")
        saldo_valor(saldo)
    
        while numero_saques < LIMITE_SAQUES: # limitacao de numero de saques por dia
            print(f"Você possui uma quantidade de {LIMITE_SAQUES - numero_saques} saques restantes hoje.\n")
            saque = input("Digite o valor desejado para o saque: ") # recebe qualquer tipo de input

            if saque.isnumeric(): #continua se saque for um numero
                saque = float(saque)
                if saque <= 0:
                    print("Digite um valor valido para o saque.\n")

                elif saque <= saldo: # verifica se tem saldo suficiente para saque
                    if saque <= LIMITE_SAQUE_VALOR: # limita valor de saque
                        print(f"Deseja continuar com a operacao do saque de R$ {saque:.2f}?")
                        opcao = conf_opcao()

                        # confirmacao para o saque
                        if opcao == "Y":
                            sleep(1)
                            print(f"O saque de R$ {saque:.2f} foi feito com exito!\
                                \nRetire o dinheiro na parte inferior do caixa eletronico.\n")
                            extrato += f"{operacao} - Saque: R$ {saque}\n"
                            operacao += 1
                            saldo -= saque
                            saldo_valor(saldo)
                            numero_saques += 1
                            
                            sleep(1)
                            print("Gostaria de continuar com outra operacao de saque? ")
                            opcao = conf_opcao()
                            if opcao == "Y":
                                continue
                            if opcao == "N":
                                break
                            
                        elif opcao == "N":
                            print(f"O saque de R$ {saque:.2f} foi cancelado.\n")
                            print("Gostaria de continuar com outra operacao? ")
                            opcao = conf_opcao()
                            if opcao == "Y":
                                continue
                            if opcao == "N":
                                break

                        else:
                            print("Operacao cancelada.\n")
                            print("Retornar ao menu inicial?")
                            opcao = conf_opcao()
                            if opcao == "Y":
                                continue
                            if opcao == "N":
                                break
                    else:
                        print(f"Valor de R$ {saque:.2f} excede o valor limite permitido para saques.\n")
                        print("Gostaria de realizar outro valor de saque?")
                        opcao = conf_opcao()
                        if opcao == "Y":
                            continue
                        if opcao == "N":
                            break

                elif saque > saldo:
                    print("Saldo insuficiente!\n")
                    print("Gostaria de realizar outro valor se saque?")
                    opcao = conf_opcao()
                    if opcao == "Y":
                        continue
                    if opcao == "N":
                        break

                print("Retornar ao menu inicial?")
                opcao = conf_opcao()
                if opcao == "Y":
                    continue
                if opcao == "N":
                    break
            
            else:
                print("Digite um valor valido para o saque.\n")
                saque = 0
        
        if numero_saques >= LIMITE_SAQUES:
            print("Número de saques máximo atingido hoje. Gostaria de realizar outra operação?")
            opcao = conf_opcao()
            if opcao == "Y":
                continue
            if opcao == "N":
                break

        print("Retornar ao menu inicial?")
        opcao = conf_opcao()
        if opcao == "Y":
            continue
        if opcao == "N":
            sist_off()
            break
        
    elif opcao == "D": # Deposito
        print(f"********** Operacao Deposito ***********\n")
        saldo_valor(saldo)
        
        while True:

            deposito = float(input("Digite o valor desejado para deposito em R$: "))
            
            if deposito > 0:
                
                print(f"Operacao bem sucedida!\n")
                extrato += f"{operacao} - Deposito: R$ {deposito:.2f}\n"
                operacao += 1
                saldo += deposito
                saldo_valor(saldo)

                print("Gostaria de realizar outro depósito?")
                opcao = conf_opcao()
                if opcao == "Y":
                    continue
                if opcao == "N":
                    print("Retornando ao menu incial...")
                    break
            else:
                print("Valor de deposito invalido.\n Gostaria de continuar na operação de Depósito?")
                opcao = conf_opcao()
                if opcao == "Y":
                    continue
                if opcao == "N":
                    break
        
            print("Retornar ao menu inicial?")
            opcao = conf_opcao()
            if opcao == "Y":
                continue
            if opcao == "N":
                sist_off()
                break

    elif opcao == "E": # Extrato
        print("========== Operacao Extrato ==========\n")
        
        print(extrato)
        print("______________________________________\n")
        sleep(1)
        print(f"Seu saldo final e de R$ {saldo:.2f}\n")
        print("======================================")
            
        print("\nRetornar ao menu inicial?")

        opcao = conf_opcao()
        if opcao == "Y":
            continue
        if opcao == "N":
            sist_off()
            break

    elif opcao == "Q": # Sair
        sist_off()
        break

    else:
        print("Selecione uma opcao valida.\n")
        sleep(1)
