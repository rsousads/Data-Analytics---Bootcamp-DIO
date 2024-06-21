## SISTEMA PARA CONTROLE DE DESPESAS
from datetime import datetime 



def valida_dados(tipo, dado):  # METODO DE VALIDAÇÃO DOS DADOS
    try:
        if tipo =="int":
            int(dado)
        elif tipo =="float":
            float(dado)
        elif tipo == "str":
            if not dado:
                raise ValueError("Digite novamente! \n")
        elif tipo == "data":
            datetime.strptime(dado, "%d/%m/%Y")
    except ValueError:
        print("Dados digitados invalidos, digite novamente! \n")


def menu() :
    print("""Seja bem vindo ao sistema de controle de finanças! \n### Planilha de controle Mensal ### \n" )
                                            ("1 - Cadastrar despesa")
                                            ("2 - Cadastrar receita")
                                            ("3 - Relatorio de Despesa")
                                            ("4 - Relatorio de Receita")
                                            ("5 - Relatorio de despesa e receita por categoria")
                                            ("6 - APERTE 0 PARA SAIR""")




def cadastro_despesa (cad_despesas): ##referencia um objeto 
     despesa = valida_dados ("str", input("Insira o nome da despesa:\n"))
     valordespesa = valida_dados("float", input("Insira o valor da despesa R$:\n"))
     categoriadespesa = valida_dados("str", input("informe a categoria:\n"))
     datadespesa = valida_dados("data", input("infome a data ( dd/mm/aaaa)\n"))

        # Converte a string para um objeto datetime
     dataconvertdespesa = datetime.strptime(datadespesa, "%d/%m/%Y")

     lista_despesa = [despesa,valordespesa,categoriadespesa,datadespesa] ##armazena em uma lista os valores
     cad_despesas.append(lista_despesa) ##usa referencia para adicionar cada vez qque cadastrar 1 despesa ( adiciona na lista)   return cad_despesa  ##retorna os valores


def cadastro_receita():

    
        receita = valida_dados("str", input("Insira o nome da receita: \n"))
        valoreceita = valida_dados("float", input("Insira o valor da receita R$: \n"))
        categoriareceira = valida_dados("str", input("Insira a categoria da Receita"))
        datareceita = valida_dados("data", input("informe a data em  DD/MM/AAAA\n"))

        dataconverreceita = datetime.strptime(datareceita, "%d/%m/%Y")

        return receita,valoreceita,categoriareceira,datareceita


def relatorio_despesa(lista_despesa):
     
    
    while True:
        try:
                print("BEM VINDO AO RELATORIO DE DESPESAS \n\n")
                opcao = valida_dados("int", input(""" 1 - PARA VER TODAS DESPESAS CADASTRADAS
                                                      2 - PARA VER SOMA TOTAL DAS DESPESAS
                                                      3 - PARA VER A MÉDIA DAS DESPESA \n\n"""))
                break
        except ValueError:
            print("Opcao invalide digite uma das informadas:  ")
                    
    if opcao == 1 :    
        for rel_despesas in lista_despesa:
            print("Nome :", rel_despesas[0], "| Valor :", rel_despesas[1], "| Categoria: ", rel_despesas[2],"| Data: ", rel_despesas[3],"\n\n\n")   

    elif opcao ==2:

        soma_total = sum(lista_despesa[1] for reldespesas in lista_despesa) #armazena a soma de todos os valores do indicie um da lista_despesa
        # for reldespesas in lista_despesa:
        #     soma_total += lista_despesa[1]
        if soma_total ==0:
            print("NÃO HA DESPESAS CADASTRADAS \n\n")
        else:
            print(f"O VALOR TOTAL DAS DESPESAS FOI DE: R$ {soma_total:.2f} \n")

    else :
        if soma_total <= 0:
            print ("NÃO EXISTE VALORES NA LISTA CADASTRADOS! \n\n")
        else:
            media_total = soma_total / (len(lista_despesa[1]) for reldespensa in lista_despesa ) # o LEN contabiliza a quantidade de valores cadastrados para o calculo
            print (f"A média das depesas cadastradas é: R${media_total:.2f}")


def relatorio_receitas(lista_receita):
    while True :
        try:
            print("""SEJA BEM VINDO AO RELATORIO DE RECEITAS""")
            opcao = valida_dados("int", input("""  1 - PARA VER TODAS DESPESAS CADASTRADAS
                                            2 - PARA VER SOMA TOTAL DAS DESPESAS
                                            3 - PARA VER A MÉDIA DAS DESPESA \n\n"""))
        except ValueError:
            print("Opção invalida digita, digite novamente!! \n")

            if opcao == 1 :
                
                for relreceita in lista_receita :
                    print ("Nome: ", relreceita[0], "| Valor: ", relreceita[1], "| Categoria: ", relreceita[2], "| Data: ", relreceita[3], "\n")

            elif opcao ==2:
                soma_total = sum(lista_receita[1] for relreceita in lista_receita) #armazena a soma de todos os valores do indicie um da lista_receita
                if soma_total ==0:
                    print(" Não existe valores cadastrados \n")
                else:
                    print(f"O valor total das receitas foi de: R${soma_total:.2f} \n")
                

            elif opcao ==3:
                media_receita = soma_total / (len(lista_receita[1]) for relreceita in lista_receita)
                if media_receita ==0:
                    print("Não existe valores suficientes para calculo. \n")
                else:
                    print(f" A media total das receitas é de R$ {media_receita:.2f} \n")

                    
            elif opcao ==4:  #("5 - Relatorio de despesa e receita por categoria")

                dicionario = {}   
                print(".".join("BEM VINDO AO RELATORIO POR CATEGORIA"))

                for reldespesa in lista_receita:
                    nome_categoria_despesa = reldespesa[lista_receita[2]]
                    valor_categoria_despesa = relreceita[lista_receita[1]

                ] 
                    
                

                
        
            
        
        


def main():

        despesas = []
        opcao = -1
        receitas = []
        while opcao != 0:
            try:
                    menu()
                    opcao = int(input("Escolha uma opção: "))
                    if opcao == 1:
                        cadastro_despesa(despesas)
                    elif opcao == 3:
                        relatorio_despesa(despesas)
                    elif opcao == 2:
                        cadastro_receita(receitas)
                    # elif opcao == 4:
                    #     relatorio_receita(receitas)
            except ValueError:
                print("Opção invalida")
                
                if __name__ == "__main__":
                    main()
        
           
            

    

    



