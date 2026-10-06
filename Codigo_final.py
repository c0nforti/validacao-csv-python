from verificar_CPF import validaCPF
from verificar_cartão import validaCartao

filename = 'teste.csv'

with open(filename) as file_object:
    linhas = file_object.readlines() #Readlines criou uma lista 

    print("REGISTRO DE ERROS:")

    for NNN, linha in enumerate(linhas, start = 1):
        #SEPARANDO POR COLUNAS
        lst = linha.strip().split(",")

        #REGISTRO DE ERROS:
        
        #ERROS CPF
        if not lst[1]:
            print(f"Linha {NNN:4}: CPF - Campo vazio",end="\n") #ERRO 1
        else:
            lst2 = [numeros for numeros in lst[1] if numeros != "." and numeros != "/" and numeros != "-"]
            cpf_limpo = ''.join(lst2).strip()
            if len(cpf_limpo) != 11:
                print(f"Linha {NNN:4}: CPF - Quantidade incorreta de dígitos ({len(cpf_limpo)} dígitos)",end="\n") #ERRO 2
            #TESTE DE VALIDADE CPF
            elif validaCPF(cpf_limpo) != True:   
                print(f"Linha {NNN:4}: CPF - Erro nos dígitos verificadores",end="\n") #ERRO 3

        #ERROS CARTAO
        if not lst[2]:
            print(f"Linha {NNN:4}: CARTÃO - Campo vazio",end="\n") #ERRO 1
        else:
            lst3 = [numeros2 for numeros2 in lst[2] if numeros2 != " "]
            cartao_limpo = ''.join(lst3).strip()
            if len(cartao_limpo) != 16:
                print(f"Linha {NNN:4}: CARTÃO - Quantidade incorreta de dígitos ({len(cartao_limpo)} dígitos)",end="\n") #ERRO 2
            #TESTE DE VALIDADE CARTAO
            elif validaCartao(cartao_limpo) != True:
                print(f"Linha {NNN:4}: CARTÃO - Erro nos dígitos verificadores",end="\n") #ERRO 3