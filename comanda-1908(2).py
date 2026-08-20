'''
Gabriel Magno de Oliveira Santos;
Luíza Gomes Barbosa;
Janyelle Maryanne De Souza Ferreira
'''
cardapio=["Arroz","Bife Assado","Frango Assado","Suco De Goiaba","Porco Assado"]
valor=[1.99,12.99,23.99,0.99,45.99]
mesasabertas=[]

titulo="SABOR DA ORLA"

while True:
    print(f"{'='*20}\n{titulo.center(20)}\n{'='*20}")
    print("1 - Cadastrar item no cardápio\n2 - Consultar cardápio\n3 - Abrir mesa\n4 - Consultar mesas\n5 - Consultar produto por código\n6 - Pesquisar produto por nome \n0 - Sair")
    opcao=int(input("Escolha uma opção: "))
    
    
#o cadastro do cardapio inicia aqui

    if opcao==1:
        print(f"{'='*9} CADASTRO DE PRODUTO {"="*9}")
        comida=input("Nome do produto: ")
        
        comida = comida.strip()
        comida = comida.title()
        
        if comida in cardapio:
            print("Produto já cadastrado.")
        else:
            cardapio.append(comida)
            preco=float(input("Preço: "))
            valor.append(preco)
            print("Produto cadastrado com sucesso!")

#o cadastro do cardapio acaba aqui

#a consulta do cardapio inicia aqui

    elif opcao==2:
       
       if len(cardapio)>0:
        print(f"{'='*15} CARDÁPIO {'='*15}")
        print(f"{'Código':<5} {'Produto':<17} {'Preço':>10}")
        print("-"*35)
        for i in range(len(cardapio)):
            preco_fmt = f"R$ {valor[i]:.2f}"
            print(f"{i+1:<5} {cardapio[i]:<17}{preco_fmt:>10}")
       
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
    elif opcao==5:
        print(f"{'='*15} CONSULTAR PRODUTO {'='*15}")
        i=int(input("Digite o código do produto: "))
        
        if len(cardapio)>=i:
            print(f"{'Código':<5} {'Produto':<17} {'Preço':>10}")
            print("-"*35)
            preco_fmt = f"R$ {valor[i-1]:.2f}"
            print(f"{i:<5} {cardapio[i-1]:<17}{preco_fmt:>10}")
        else:
            print("Produto não encontrado.")
            
    elif opcao==6:
        print(f"{'='*9} PESQUISAR PRODUTO {'='*9}")
        i=input("Digite o nome ou parte do nome: ")
        contador=0
        tem=[]
        for j in range(len(cardapio)):
            if i in cardapio[j]:
                contador+=1
                tem.append(cardapio[j])
        if contador==0:
            print("Nenhum produto encontrado.")
        else:
            print(f"{'Código':<5} {'Produto':<17} {'Preço':>10}")
            print("-"*35)

            for k in range(len(tem)):
                    preco_fmt = f"R$ {valor[cardapio.index(tem[k])]:.2f}"
                    print(f"{cardapio.index(tem[k])+1:<5} {tem[k]:<17}{preco_fmt:>10}")
    elif opcao==0:
       break

print(f"{cardapio.index(tem[k])+1}  {tem[k]}",end=" ")
print(f"R${valor[cardapio.index(tem[k])]:.2f}")