import time



def mensagem():
    
    print("------------------------------------")
    print("         LOjA DE MEIAS LUPO")
    print("------------------------------------")


    print("[1] ver opcoes de meias  disponiveis")
    print("[2] comprar meias")  
    print("[3] Colocar ou atualizar preco das meias ")
    print("[4] Relacao  das vendas")
    print("[5] Sair")
    print("\n")
    print("\n")



def mostrar(preco):

    print("------------------------------------")
    print(f"[1] Meia Lupo(P)===================R${preco[0]}")
    print("        ")
    print(f"[2] Meia Lupo(M)===================R${preco[1]}")
    print("        ")
    print(f"[3] Meia Lupo(G)===================R${preco[2]}")
    print("------------------------------------")
    print("\n")


def  mudarp(preco):
    print("\n")

    mostrar(preco)
    r="S"
    while r != "N" :   
        esco=int(input("selecione qual opcao quer alterar->"))
        n=input("insira o novo valor utilizando ponto no lugar de virgula->")
        preco[esco-1]=n
        arquivo=open("prco.txt","wt")
        for l in range(0,2,1):
            arquivo.write("")
        
        for j, i in enumerate(preco):
            if j==esco-1:
                arquivo.write(f"{i}\n")
            else:
                arquivo.write(f"{i}")
            
        arquivo.close()
        r  = input("Deseja atualizar ou incrementar outro preco? [S/N]->" ).upper()


def passar(preco, numero):
    j=cont=0
    for cont, i in enumerate(preco):
        if cont == len(preco):
            j=float(i)
            numero.append(j)
        else:
            j=float(i[:-2])
            numero.append(j)
    
    
#----------------------------------
def comprar(numero):
    mostrar(preco)

    valor=quantidade=opt=0
  
    opt=int(input("selecione a opcao de compra->"))
    quantidade = int(input("quantas unidades deseja adquirir->"))
    valor=numero[opt-1]*quantidade
    
    arquivo=open("relacao.txt","at") 
    arquivo.write(f"foram {quantidade} compradas do tipo {opt}, custando R${valor:.2f}\n")
    arquivo.close()


def relacao():
    arquivo=open("relacao.txt","rt")
    for linha in arquivo.readlines():
        print(linha)
    arquivo.close()


def escolher(opt):
    global preco    
    preco=[]
    global numero
    numero=[]
    
    arquivo = open("prco.txt","rt")
    for l in arquivo.readlines():
       preco.append(l)
    arquivo.close()
    

    passar(preco,numero)
    #---------------------------------------------------------------------------------------------
    if opt == 1 :
        mostrar(preco)
        time.sleep(2)
    elif opt == 2 :
        comprar(numero)
        print("\n\n\n\n")
        time.sleep(2)

    elif opt == 3 :
        print("\n")
        mudarp(preco)
        
    elif opt == 4 :
        print("\n")
        relacao()

        print("\n")
    elif opt == 5:
        time.sleep(1)
        print('...')
        time.sleep(2)
        print('Excutando saida....')
        time.sleep(3)
        print('................')
        print("Finalizado com sucesso ")

