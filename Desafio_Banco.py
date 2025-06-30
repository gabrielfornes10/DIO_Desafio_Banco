menu = """
----------------------------
     
     [1] Depositar
     [2] sacar
     [3] Extrato
     [0] sair

----------------------------    

"""
saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)
    
    if opcao == "1" :
       print("Depositar")
       valor = float(input("Quanto deseja depositar:"))
       
       if valor > 0:
          
           saldo += valor
           extrato += f"Deposito: R${valor:.2f}\n"
       else:
          print("Operação invalida")
          


    elif opcao == "2" :
       print("sacar")
       valor = float(input("Quanto deseja sacar: "))
       
       excedeu_saldo = valor > saldo

       excedeu_limite = valor > limite

       excedeu_saques = numero_saque >= LIMITE_SAQUES
       
       
       if excedeu_saldo:
          print("Operação falhou! Você não tem saldo suficiente.")
       
       elif excedeu_limite:
          print("Operação falhou! O valor do saque excede o limite ")

       elif excedeu_saques:
          print("Operação falhou! Número maximo de saques  excedido. ")

       elif valor > 0:
          saldo += valor 
          extrato += f"Saque R$ {valor:.2f}\n"
          numero_saque += 1
       else:
         print("Operação falhou! Valor inválido. ")            

      


    elif opcao == "3" :
       print("\n===============Extrato===============\n")
       print("Nenhuma movimentação" if not extrato else extrato) 
       print(f"\n Saldo: R${saldo:.2f}")
       print("=========================================") 
    
    elif opcao == "0" :
       break
    
    else:
       print("Opção invalida")

    



