cardapio=[]
valor=[]
mesasabertas=[]

titulo="SABOR DA ORLA"

while True:
    print(f"{'='*20}\n{titulo.center(20)}\n{'='*20}")
    print("1 - Cadastrar item no cardápio\n2 - Consultar cardápio\n3 - Abrir mesa\n4 - Consultar mesas\n0 - Sair")
    opcao=int(input("Escolha uma opção: "))
    
    
#o cadastro do cardapio inicia aqui

    if opcao==1:
        print(f"{'='*9} CADASTRO DE PRODUTO {"="*9}")
        comida=input("Nome do produto: ")
        
        comida = comida.strip()
        comida = comida.capitalize()
        
        cardapio.append(comida)
        
        preco=float(input("Preço: "))
        valor.append(preco)
        print("Produto cadastrado com sucesso!")

#o cadastro do cardapio acaba aqui

#a consulta do cardapio inicia aqui

    elif opcao==2:
       
       if len(cardapio)>0:
        print(f"{'='*9} CARDÁPIO {'='*9}")
        
        for i in range(len(cardapio)):
            print(f" {i+1} - {cardapio[i]}",end=" ")
            print(f"R${valor[i]:.2f}")
       
       else:
           print("Nenhum produto cadastrado.")

#a consulta do cardapio acaba aqui

#a abertura de mesas começa aqui

    elif opcao==3:
        mesa=int(input("Número da mesa:"))
        
        if mesa not in mesasabertas:
           mesasabertas.append(mesa)
           print(f"Mesa {mesasabertas[mesasabertas.index(mesa)]} aberta com sucesso!")
        
        else:
           print(f"A mesa {mesasabertas[mesasabertas.index(mesa)]} já está aberta.")
           
#a abertura de mesas acaba aqui

#Checagem de mesas começa aqui:

    elif opcao==4:
        
        if len(mesasabertas)==0:
           print("Nenhuma mesa está aberta.")
        
        else:
            print(f"{'='*9} MESAS ABERTAS {'='*9}")
            for i in range (len(mesasabertas)):
                print(f"Mesa {mesasabertas[i]}")

#Checagem de mesas acaba aqui

    elif opcao==0:
       break
