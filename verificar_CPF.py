# Algoritmo "Validação de CPF"
def validaCPF(cpf):

    n1 = int(cpf[0])
    n2 = int(cpf[1])
    n3 = int(cpf[2])
    n4 = int(cpf[3])
    n5 = int(cpf[4])
    n6 = int(cpf[5])
    n7 = int(cpf[6])
    n8 = int(cpf[7])
    n9 = int(cpf[8])
    n10 = int(cpf[9])
    n11 = int(cpf[10])

    #Validação dos CPFs inválidos conhecidos
    if (n1 == n2) and (n2 == n3) and (n3 == n4) and (n4 == n5) and (n5 == n6) and (n6 == n7) and (n7 == n8) and (n8 == n9) and (n9 == n10) and (n10 == n11):
        return False
    
    else:
        soma1 = n1 *10 + n2 * 9 + n3 * 8 + n4 * 7 + n5 * 6 + n6 * 5 + n7 * 4 + n8 * 3 + n9 * 2
        resto1 = (soma1*10) % 11
        
        if resto1 == 10:
            resto1 = 0

        soma2 = int(n1 * 11 + n2 * 10 + n3 * 9 + n4 * 8 + n5 * 7 + n6 * 6 + n7 * 5 + n8 * 4 + n9 * 3 + n10 * 2)
        resto2 = (soma2 *10) % 11
        
        if resto2 == 10:
            resto2 = 0

        if (resto1 == n10) and (resto2 == n11):
            return True 
        
        else: return False