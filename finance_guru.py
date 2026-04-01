gastos = []
ganhos = []
while True: 
    print("\n1 - Adicionar gasto")
    print("2 - Adicionar ganho")
    print("3 - Ver gastos")
    print("4 - Ver total")
    print("5 -Sair")
    opcao = input ("Escolha uma opção")
    
    if opcao =="1":
        nome = input ("Nome do gasto:")
        valor = float (input("Valor:"))
        gastos.append((nome, valor))
    elif opcao == "2":
        nome = input ("Nome do ganho:")
        valor = float (input('Valor:'))
        ganhos.append((nome, valor))
    
    elif opcao =="3":
        for gasto in gastos:
             print(gasto)
    
    elif opcao =="4":
        total_gastos = sum (valor for nome, valor in gastos)
        total_ganhos = sum (valor for nome, valor in ganhos)
        
        saldo = total_ganhos - total_gastos
        print (f"seu saldo atual: R$ {saldo}")
    elif opcao =="5":
        break