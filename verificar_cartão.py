# Algoritmo "Validação de nº de Cartão"

def validaCartao(n):

    soma = 0
    digits = 0
    secoundDigit = False
    
    for i in range(15, -1, -1):
        digito = int(n[i])
        
        if secoundDigit:
            digito *= 2
            soma += digito // 10 + digito % 10
        else:
            soma+=digito

        secoundDigit = not secoundDigit
        
        digits += 1
    
    if digits != 16 or soma % 10 != 0:
        return False
    else: 
        return True