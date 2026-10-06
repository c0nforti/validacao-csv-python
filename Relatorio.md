# Anotações e relatórios da primeira lista python
Este arquivo reúne testes, ideias, requisitos técnicos e cenários de borda específicos desta atividade. Seu objetivo é dar suporte contínuo ao programador durante as etapas de desenvolvimento, validação e manutenção do código, garantindo o alinhamento com as regras do exercício.

## Conteúdo central:
- Exigências e Requisitos: Especificações do comportamento esperado e critérios de aceite.
- Casos de Teste: Cenários de validação para garantir a qualidade do código e evitar regressões.
- Anotações e Ideias: Registro de decisões técnicas, pontos de atenção e propostas de melhorias futuras.

## Objetivos iniciais:
> - Capacidade de ler arquivo CSV
> - Receber 3 valores: nome, CPF e nº Cartão 
> - Verificar campos não-vazios
> - Verificar validade de CPF e nº Cartão
> - Imprimir relatório com erros achados
> - String descrevendo o erro
> - Erros válidos para o exercício:
>> - Valor vazio para o campo.
>> - Número incorreto de dígitos para o campo
>> - Falha na verificação do(s) dígito(s) verificador(es).
> - No documento, explicar por que sua utilização é preferível à implementação equivalente convencional usada, por exemplo, em uma linguagem C.
> - Criar 12 casos de teste com CPF e nº Cartão invalidos
> - Explique por que cada caso de teste foi escolhido e que possível erro de implementação ele procura detectar. 


## Observações iniciais:
> - Validade do CPF: Considerado válido se ele tiver 11 dígitos com separadores (“.”, “-”, “/”) opcionais e se os dígitos satisfizerem o algoritmo de verificação de números de CPF.
> - Validade do nº de cartão: Será válido se contiver 16 dígitos com possíveis espaços para separação e se os dígitos satisfizerem o algoritmo de Luhn.
> - Cada linha do relatório de erros deve ter a seguinte forma `Linha NNN: Razão do erro` 
> - **NNN** é o número da linha com o erro formatado com espaço para quatro dígitos
> - **Razão do erro** é uma string que começa com `CPF − `, se o erro foi no CPF, e `CARTÃO − `, se o erro foi no número do cartão de crédito.
> - ERRO 1: A string deve ser `Campo vazio`
> - ERRO 2: `Quantidade incorreta de dígitos (NN dígitos)` (NN é o número de dígitos do campo lido)
> - ERRO 3: `Erro nos dígitos verificadores`.
> - Se uma linha conter erro em ambos valores analisados, deve ser gerado **duas** linhas no relatório, uma pra cada erro.
> - Não usar bibliotecas externas (Imports).
> - Usar o maximo possivel de list comprehesions, sequencias, geradores, etc vistas em aula.
> - Para cada teste, registre entrada, resultado esperado e resultado obtido.


# Primeira interação com o código
As primeiras linhas de comando testadas pelo desenvolvedor foi se o arquivo CSV estava sendo lido corretamente:

``` py
with open('teste.csv') as file_object:
    leitura = file_object.read()
    print(leitura.rstrip())
```

### Algoritmo de CPF inicial:
Em um novo arquivo denominado "verificar_CPF.py" foi-se iniciado a implementação do algoritmo de validação de CPF:

``` py
# Algoritmo "Validação de CPF"
def validaCPF(cpf):

    #Extração dos digitos do CPF:
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

#TESTE DE VERIFICAÇÃO:
filename = 'teste.csv'

with open(filename) as file_object:
    linhas = file_object.readlines()
    CPF = linhas[1]

if validaCPF(CPF) == True:
    print(f"O cpf {CPF.rstrip()} é válido!")
else: print(f"O cpf {CPF.rstrip()} é inválido!")
```

### Algoritmo de Número de Cartão inicial:
Em um novo arquivo denominado "verificar_cartão.py" foi-se iniciado a implementação do algoritmo de validação de nº de cartão:

```py
# Algoritmo "Validação de nº de Cartão"

def validaCartao(n):

    soma = 0
    digits = 0
    secoundDigit = False

    while(n !=0):
        digit = n % 10

        if secoundDigit:
            digit *= 2
            soma += digit // 10 + digit % 10
        else:
            soma+=digit

        secoundDigit = not secoundDigit
        n //= 10
        digits += 1

    if digits != 16 or soma % 10 != 0:
        return False
    else: 
        return True
```

## Desafios e ideias iniciais:
- implementar `try` e `except` para identificar os erros.
- implementar `len()` para contagem de dígitos.
- implementar ERROS como string **CPF-** em uma variável para ser chamada depois no relatório.
- implementar `del()` (testar).
- implementar `key=lambda x:` (testar).
- implementar `.split(".")` para remoção do ponto (testar).
- Implementar `for` (list comprehension).
- Implementar `enumerate()` para numeração de linhas.
- Implementar `.join()`.
- Implementar iteradores no cpf e no numero do cartao.

# Evolução do código
Após a implementação inicial dos algoritmos de validação, o desenvolvedor iniciou a integração das funções com o programa principal responsável pela leitura e análise do arquivo CSV.

### Leitura e separação dos dados:
Inicialmente, foi utilizado o `readlines()` para armazenar todas as linhas do arquivo CSV em uma lista. Em seguida, foi utilizado o `enumerate()` para obter o número correspondente a cada linha durante a leitura.
Para separar os três valores presentes em cada linha, foi utilizado o `.split(",")`, criando uma lista contendo o nome, CPF e número do cartão (uma separação por coluna):

```py
linhas = file_object.readlines()

for NNN, linha in enumerate(linhas, start = 1):
    #SEPARANDO POR COLUNAS
    lst = linha.strip().split(",")
```

O uso do `enumerate()` permitiu que o número da linha fosse obtido diretamente durante o `for`, evitando a necessidade de criar e incrementar manualmente uma variável para controle da numeração.

### Verificação de campos vazios:
Após a separação das colunas, foram adicionadas verificações para identificar quando o CPF ou o número do cartão estavam vazios.

```py
#ERRO 1 CPF
if not lst[1]:
    print(f"Linha {NNN}: CPF - Campo vazio", end="\n")

#ERRO 1 CARTÃO
if not lst[2]:
    print(f"Linha {NNN}: CARTÃO - Campo vazio", end="\n")
```

Foi necessário utilizar uma estrutura condicional para que, quando o campo estivesse vazio, o programa não continuasse tentando validar a quantidade de dígitos ou os dígitos verificadores daquele campo.

### Limpeza dos separadores do CPF:
Como o exercício permite que o CPF contenha os separadores `.`, `-` e `/`, foi utilizada uma list comprehension para remover esses caracteres antes da validação.

```py
else:
    lst2 = [numeros for numeros in lst[1] if numeros != "." and numeros != "/" and numeros != "-"]
    cpf_limpo = ''.join(lst2).strip()
```

Houve uma tentativa de utilizar `or` na condição da list comprehension. Durante os testes, foi identificado que essa condição não removia os caracteres corretamente, sendo necessário utilizar `and`, pois o caractere deveria ser diferente dos três separadores ao mesmo tempo.
Após a filtragem, o `.join()` foi utilizado para transformar novamente a sequência de caracteres em uma única string.

### Verificação da quantidade de dígitos do CPF:
Depois da limpeza dos separadores, foi utilizada a função `len()` para verificar se o CPF possuía exatamente 11 dígitos.

```py
#ERRO 2 CPF
if len(cpf_limpo) != 11:
    print(f"Linha {NNN}: CPF - Quantidade incorreta de dígitos ({len(cpf_limpo)} dígitos)", end="\n")
```

Após a verificação, o CPF é enviado para a função `validaCPF()`:

```py
#ERRO 3 CPF
elif validaCPF(cpf_limpo) != True:
    print(f"Linha {NNN}: CPF - Erro nos dígitos verificadores", end="\n")
```

Dessa forma, evitamos que a função de validação receba um CPF (o mesmo com o nº de cartão, descrito mais a frente) com quantidade incorreta de caracteres.

### Limpeza dos espaços do número do cartão:
Para o nº de cartão, foi utilizado procedimento semelhante ao CPF. Como o exercício permite espaços para separação dos números, foi criada uma list comprehension para removê-los:

```py
lst3 = [numeros2 for numeros2 in lst[2] if numeros2 != " "]
cartao_limpo = ''.join(lst3).strip()
```

Verificando os dígitos:

```py
#ERRO 2 CARTÃO
if len(cartao_limpo) != 16:
    print(f"Linha {NNN}: CARTÃO - Quantidade incorreta de dígitos ({len(cartao_limpo)} dígitos)", end="\n")
```

Após a verificação, o nº de cartão é enviado para a função `validaCartao()`:

```py
#ERRO 3 CARTÃO
elif validaCartao(cartao_limpo) != True:
    print(f"Linha {NNN:4}: CARTÃO - Erro nos dígitos verificadores",end="\n")
```

### Erros e adaptação do algoritmo do cartão:
Inicialmente, a integração do algoritmo de validação do cartão através da função `validaCartao()` esperava receber um número inteiro.
Entretanto, o programa principal trabalhava com o cartão como uma string, principalmente por causa da necessidade de remover os espaços presentes no arquivo CSV.
Por esse motivo, o algoritmo foi adaptado com um `for`: 

```py
for i in range(15, -1, -1):
    digito = int(n[i])
```

Dessa forma, cada caractere da string é convertido para inteiro somente dentro da função e ainda percorre seus dígitos de trás para frente, como esperado no algoritmo de Luhn.

### Contagem de linhas:
Dentro de cada `print(f"string")` que expunha as linhas de erros, foi formatada a variável `NNN` com largura de 4 caracteres (como indicado no texto-base do exercício)

```py
print(f"Linha {NNN:4}: ...")
```

### Nome vazio:
Durante a verificação dos campos, os testes realizados foram concentrados principalmente no CPF e no número do cartão, pois são os campos que possuem regras específicas de validação e os tipos de erro definidos no relatório pelo exercício. O campo nome faz parte da estrutura de três valores do arquivo CSV, porém não foi realizado um caso de teste específico para nome vazio durante esta etapa. Essa verificação poderia ser acrescentada posteriormente para complementar os testes de entrada do programa.


# Fase de testes
## Testes realizados durante o desenvolvimento:
### Teste de múltiplos erros na mesma linha:
Durante os testes dentro do desenvolvimento, foi verificado que uma mesma linha poderia apresentar erros tanto no CPF quanto no cartão.
O programa foi estruturado para realizar as duas verificações independentemente. Dessa forma, quando ambos apresentam erro, são geradas duas linhas no relatório.

Exemplo:
```text
Linha 4: CPF - Erro nos dígitos verificadores
Linha 4: CARTÃO - Quantidade incorreta de dígitos (13 dígitos)
```

Esse comportamento atende à regra de que cada erro deve possuir sua própria linha no relatório.

---

### Teste de validade e invalidade:
Foi utilizado inicialmente um arquivo CSV contendo registros válidos e inválidos para verificar o comportamento do programa.
Como resultado, os testes com CPF e nº de cartão válidos foi bem sucedido, assim como os com dados inválidos:

```text
Gabriel Conforti,###.###.###-##,#### #### #### ####
Juliana Lourenza,###########,1234567891234560
Jurema Messias,###/###/###/##,#### ######## ####
Guilherme Elias,11111111111,24506422 43232
,,2345 6054 0450 4560
```
>**OBS:** Alguns dados que foram utilizados são reais. Por isso, foram substituidos neste documento por `#`.

Resultado:

```text
REGISTRO DE ERROS:
Linha 2: CARTÃO - Erro nos dígitos verificadores
Linha 4: CPF - Erro nos dígitos verificadores
Linha 4: CARTÃO - Quantidade incorreta de dígitos (13 dígitos)
Linha 5: CPF - Campo vazio
Linha 5: CARTÃO - Erro nos dígitos verificadores
```

O teste permitiu verificar simultaneamente a validação do CPF, a validação do cartão, a contagem de dígitos, os campos vazios e a possibilidade de existirem dois erros na mesma linha.

---

### Teste de linha com quantidade incorreta de campos:
Também foi realizado um teste com uma linha que não possuía o terceiro campo:

```text
Hermione Granger, 123.321.456-18
```

Como resultado, o programa apresentou um `IndexError` ao tentar acessar `lst[2]`, pois o `.split(",")` produziu somente duas posições.

Posteriormente, foi realizado o teste adicionando a terceira coluna vazia (adição de uma vírgula), e como resultado:

```text
Linha 1: CARTÃO - Campo vazio
```

Este resultado não levou à adição de um novo tipo de erro no relatório, pois os erros considerados já foram pré-fixados.

---

### Teste com espaços no início ou no final dos campos:
Durante os testes, foi identificado que espaços adicionais no início ou no final do CPF poderiam interferir na conversão dos caracteres para inteiro dentro da função `validaCPF()`.
Para corrigir, o desenvolvedor utilizou o `strip()` após a montagem das strings limpas:

```py
cpf_limpo = ''.join(lst2).strip()
cartao_limpo = ''.join(lst3).strip()
```

Assim, os espaços extras nas extremidades dos campos são descartados antes da contagem dos dígitos e da chamada das funções de validação.

---

## Casos de Teste:
Os casos de teste foram elaborados buscando não apenas verificar entradas obviamente inválidas, mas também situações que poderiam ocorrer no uso cotidiano do programa. Foram considerados erros de digitação, falta de familiaridade com computadores, utilização incorreta dos campos, diferentes formas de apresentação dos números e entradas que poderiam explorar limitações da implementação.

O enunciado determina a criação de pelo menos 12 casos de teste com CPF e número de cartão inválidos. Além disso, solicita que os testes sejam criativos e que sejam consideradas situações em que uma pessoa leiga poderia inserir dados incorretos ou em que uma pessoa mal-intencionada poderia tentar provocar um comportamento inesperado do programa.

> **Observação:** Os dados utilizados abaixo são fictícios e foram escolhidos exclusivamente para teste. Não foram utilizados dados pessoais reais.

---

### Teste 01 — CPF com apenas um dígito a menos

**Objetivo:** verificar se o programa identifica corretamente um CPF com quantidade insuficiente de dígitos.

**Entrada:**

```csv
Usuário Teste1,1234567890,4532015112830366
```

**Resultado esperado:**

```text
Linha    1: CPF - Quantidade incorreta de dígitos (10 dígitos)
```

**Resultado obtido:**

```text
Linha    1: CPF - Quantidade incorreta de dígitos (10 dígitos)
```

**Justificativa:**
Uma situação comum é o usuário esquecer um dígito ao digitar o CPF. O teste verifica se o programa realiza a contagem dos dígitos antes de executar o algoritmo de validação do CPF.

**Possível erro de implementação detectado:**
O programa poderia enviar diretamente um CPF com quantidade incorreta de dígitos para a função `validaCPF()`, causando erro durante o acesso aos caracteres ou produzindo um resultado incorreto. O código foi estruturado para verificar `len(cpf_limpo)` antes da validação.

---

### Teste 02 — CPF com um dígito a mais

**Objetivo:** verificar o comportamento quando o usuário digita um CPF com um caractere numérico excedente.

**Entrada:**

```csv
Usuário Teste2,123456789012,4532015112830366
```

**Resultado esperado:**

```text
Linha    1: CPF - Quantidade incorreta de dígitos (12 dígitos)
```

**Resultado obtido:**

```text
Linha    1: CPF - Quantidade incorreta de dígitos (12 dígitos)
```

**Justificativa:**
O erro de digitação pode ocorrer tanto pela perda quanto pela repetição de um número. Este teste complementa o teste anterior verificando o limite superior da quantidade permitida.

**Possível erro de implementação detectado:**
Detecta uma implementação que verifica somente se existem pelo menos 11 dígitos, em vez de exigir exatamente 11.

---

### Teste 03 — Nome contendo vírgula

**Objetivo:** teste de quebra do .split()

**Entrada:**

```csv
Gabriel, Conforti,52998224725,4532015112830366
```

**Resultado esperado:**

```text
ValueError
```

**Resultado obtido:**

```text
Linha    3: CPF - Quantidade incorreta de dígitos (8 dígitos)
```

**Justificativa:**
Simula um nome contendo uma vírgula, fazendo com que a separação das colunas do CSV seja deslocada. É uma entrada incomum, mas possível em um arquivo de dados.

**Possível erro de implementação detectado:**
Verifica se o programa considera corretamente a estrutura das colunas após o uso de `split(",")`. Uma vírgula presente no nome pode deslocar o CPF e o cartão para posições diferentes das esperadas e provocar erro na validação.

---

### Teste 04 — CPF composto por números repetidos

**Objetivo:** verificar se o algoritmo rejeita um CPF formado pelo mesmo dígito repetido.

**Entrada:**

```csv
Usuário Teste4,111.111.111-11,4532015112830366
```

**Resultado esperado:**

```text
Linha    1: CPF - Erro nos dígitos verificadores
```

**Resultado obtido:**

```text
Linha    1: CPF - Erro nos dígitos verificadores
```

**Justificativa:**
CPFs formados por onze números iguais são uma entrada clássica de teste. Apesar de possuírem a quantidade correta de dígitos e poderem passar por determinados cálculos matemáticos de forma aparentemente válida, não devem ser aceitos pelo programa.

**Possível erro de implementação detectado:**
Verifica se a implementação possui o tratamento específico para sequências com todos os dígitos iguais. Esse tratamento foi implementado na função `validaCPF()`.

---

### Teste 05 — Usuário coloca o próprio nome no campo CPF (Campo com 11 caracteres totais)

**Objetivo:** simular uma pessoa leiga preenchendo o campo incorreto.

**Entrada:**

```csv
Mario Moura,Mario Moura,4532015112830366
```

**Resultado esperado:**

```text
Erro de valor
```

**Resultado obtido:**

```text
ValueError: invalid literal for int() with base 10: 'M'
```
>***O programa quebrou***

**Justificativa:**
Este é um exemplo de situação em que uma pessoa com pouca experiência pode colocar o nome no lugar do CPF.

**Possível erro de implementação detectado:**
O teste verifica a robustez da função `validaCPF()` diante de caracteres não numéricos. A implementação atual espera receber uma sequência numérica após a remoção dos separadores e pode gerar um `ValueError` ao tentar executar `int()` sobre letras.

**Observação:**
Este teste não representa um dos três tipos de erro definidos pelo exercício. Ele foi incluído como teste adicional de robustez, justamente para verificar como o programa se comporta diante de uma entrada inesperada.

---

### Teste 06 — Usuário coloca o próprio nome no campo CPF (Campo com mais de 11 caracteres totais)

**Objetivo:** como o teste anterior, simular uma pessoa leiga preenchendo o campo incorreto.

**Entrada:**

```csv
Gabriel Conforti,Gabriel Conforti,453201511283036
```

**Resultado esperado:**

```text
Linha    6: CPF - Quantidade incorreta de dígitos (16 dígitos)
```

**Resultado obtido:**

```text
Linha    6: CPF - Quantidade incorreta de dígitos (16 dígitos)
```

**Justificativa:**
Este teste complementa o anterior simulando uma pessoa leiga que coloca o próprio nome no campo do CPF, mas, neste caso, o valor possui 16 caracteres. O objetivo é verificar se o programa identifica corretamente a quantidade incorreta do campo antes de tentar validar o CPF.

**Possível erro de implementação detectado:**
O teste verifica se o programa utiliza corretamente a quantidade de caracteres do campo para determinar a quantidade de dígitos antes de chamar validaCPF(). Um erro nessa etapa poderia fazer o programa considerar apenas os caracteres numéricos ou tentar executar a função de validação mesmo com uma quantidade incorreta de caracteres.

---

### Teste 07 — Cartão contendo uma letra no meio

**Objetivo:** verificar o caso de um cartão com 16 caracteres, mas com um letra no meio.

**Entrada:**

```csv
Usuário Teste7,52998224725,4532 0151 128A 0367
```

**Resultado esperado:**

```text
ValueError
```

**Resultado obtido:**

```text
ValueError: invalid literal for int() with base 10: 'A'
```
>***O programa quebrou***

**Justificativa:**
Simula um erro de digitação em que uma letra é inserida acidentalmente no número do cartão, mantendo a quantidade esperada de caracteres.

**Possível erro de implementação detectado:**
Verifica se a função `validaCartao()` consegue lidar com caracteres não numéricos. A conversão direta de cada caractere para `int` pode interromper o programa caso uma letra seja encontrada.

---

### Teste 08 — CPF com espaço no meio

**Objetivo:** verificar se os espaços no CPF quebraria o código, já que nao foi definido no `for`.

**Entrada:**

```csv
Usuário Teste8,529 982 247 25,4532015112830366
```

**Resultado esperado:**

```text
ValueError
```

**Resultado obtido:**

```text
Linha    8: CPF - Quantidade incorreta de dígitos (14 dígitos)
```

**Justificativa:**
Simula uma pessoa que tenta separar visualmente os números do CPF utilizando espaços, como é comum ao digitar números longos.

**Possível erro de implementação detectado:**
Verifica se a função de limpeza do CPF trata adequadamente caracteres inesperados. Como o programa remove apenas `.`, `/` e `-`, um espaço interno permanece na string e pode provocar erro na conversão para inteiro.

---

### Teste 09 — Cartão com espaços entre todos os dígitos

**Objetivo:** testar uma forma menos convencional de utilização dos espaços.

**Entrada:**

```csv
Usuário Teste9,52998224725,4 5 3 2 0 1 5 1 1 2 8 3 0 3 6 7
```

**Resultado esperado:**

```text
Linha    1: CARTÃO - Erro nos dígitos verificadores
```

**Resultado obtido:**

```text
Linha    1: CARTÃO - Erro nos dígitos verificadores
```

**Justificativa:**
Embora seja uma forma incomum de escrever um cartão, o requisito afirma que podem existir espaços para separação. O teste verifica se o programa trata os espaços de forma geral, em vez de aceitar somente o formato tradicional de quatro grupos.

**Possível erro de implementação detectado:**
Detecta uma implementação que remova somente espaços em posições específicas, em vez de remover todos os espaços existentes no campo.

---

### Teste 10 — Cartão com uma letra no meio (mais de 16 caracteres)

**Objetivo:** verificar o caso de um cartão com mais de 16 caracteres e com um letra no meio.

**Entrada:**

```csv
Usuário Teste10,52998224725,45320151128303A70
```

**Resultado esperado:**

```text
Linha   10: CARTÃO - Quantidade incorreta de dígitos (17 dígitos)
```

**Resultado obtido:**

```text
Linha   10: CARTÃO - Quantidade incorreta de dígitos (17 dígitos)
```

**Justificativa:**
O teste complementa outro anterior simulando uma entrada malformada que possui mais de 16 caracteres e contém uma letra.

**Possível erro de implementação detectado:**
Verifica se a validação diferencia corretamente quantidade de caracteres e/ou conteúdo numérico.

---

### Teste 11 — Campo CPF contendo apenas espaços

**Objetivo:** Verificar se o programa quebraria se o campo CPF fosse composto apenas com espaços

**Entrada:**

```csv
Usuário Teste11,           ,4532015112830366
```

**Resultado esperado:**

```text
ValueError
```

**Resultado obtido:**

```text
CPF - Quantidade incorreta de dígitos (0 dígitos)
```

**Justificativa:**
Simula um usuário que preenche o campo utilizando apenas espaços, sem fornecer efetivamente um CPF.

**Possível erro de implementação detectado:**
Verifica se a identificação de campos vazios ocorre antes ou depois da remoção dos espaços. Uma implementação que analise somente a string original pode considerar um campo contendo apenas espaços como preenchido.

---

### Teste 12 — CPF vazio e cartão inválido

**Objetivo:** verificar se o programa identifica um campo CPF vazio sem impedir a análise independente do cartão.

**Entrada:**

```csv
Usuário Teste12,,123456789012345
```

**Resultado esperado:**

```text
Linha    15: CPF - Campo vazio
Linha    15: CARTÃO - Quantidade incorreta de dígitos (15 dígitos)
```

**Resultado obtido:**

```text
Linha    15: CPF - Campo vazio
Linha    15: CARTÃO - Quantidade incorreta de dígitos (15 dígitos)
```

**Justificativa:**
O teste simula um usuário que esqueceu completamente de preencher o CPF, mas informou algum valor no cartão.

**Possível erro de implementação detectado:**
Verifica duas coisas: se o campo vazio é identificado corretamente e se o programa continua a análise dos demais campos da linha.

---

## Testes adicionais de situações de entrada:
Além dos 12 casos principais, foram realizados testes adicionais para verificar situações extras.

### Teste 13 — Os dois campos vazios

**Entrada:**

```csv
Usuário Teste13,,
```

**Resultado esperado:**

```text
Linha    1: CPF - Campo vazio
Linha    1: CARTÃO - Campo vazio
```

**Resultado obtido:**

```text
Linha    1: CPF - Campo vazio
Linha    1: CARTÃO - Campo vazio
```

**Justificativa:**
Simula um registro em que o usuário informou apenas o nome e deixou os dois campos numéricos sem preenchimento.

**Possível erro de implementação detectado:**
Verifica se o programa consegue registrar dois erros de campo vazio na mesma linha e se não tenta executar os algoritmos de validação sobre strings vazias.

---

### Teste 14 — CPF com separador repetido

**Entrada:**

```csv
Usuário Teste14,222..222.222-22,123456789012345
```

**Resultado esperado:**

```text
Linha   14: CPF - Erro nos dígitos verificadores
```

**Resultado obtido:**

```text
Linha   14: CPF - Erro nos dígitos verificadores
```

**Justificativa:**
Simula uma entrada digitada incorretamente em que um separador é inserido duas vezes consecutivamente.


**Possível erro de implementação detectado:**
Verifica se a implementação apenas remove os separadores ou se também verifica se eles aparecem em posições/formatação coerentes. O código atual prioriza a remoção dos caracteres permitidos antes da validação.

---

### Teste 15 — Linha sem a terceira coluna

**Entrada:**

```csv
Usuário Teste15,123.456.789-09
```

**Resultado esperado:**

```text
IndexError
```

**Resultado obtido:**

```text
IndexError: list index out of range
```
>***O programa quebrou***

**Justificativa:**
Este teste representa uma entrada malformada do próprio arquivo CSV. O usuário pode apagar acidentalmente uma coluna ou uma pessoa pode tentar produzir uma entrada que não siga o formato especificado.

**Possível erro de implementação detectado:**
Verifica se o programa possui proteção contra linhas com quantidade insuficiente de campos.

**Observação:**
O `IndexError` não corresponde a um dos três tipos de erro definidos pelo enunciado. Portanto, não foi criada uma nova categoria de erro no relatório. O teste serve para documentar uma limitação de robustez da implementação.

---

### Teste 16 — Separadores inesperados no CPF

**Entrada:**

```csv
Usuário Teste16,123*456*78909,4532015112830366
```

**Resultado esperado:**

```text
ValueError
```

**Resultado obtido:**

```text
Linha   16: CPF - Quantidade incorreta de dígitos (13 dígitos)
```

**Justificativa:**
O enunciado permite apenas `.`, `-` e `/` como separadores do CPF. Este teste verifica o que acontece quando uma pessoa utiliza outro caractere, como poderia ocorrer por erro de digitação.

**Possível erro de implementação detectado:**
Verifica se a função de validação possui tratamento para caracteres que não são números nem separadores permitidos.

---

### Teste 17 — Separadores inesperados no CPF (com 11 caracteres totais)

**Entrada:**

```csv
Usuário Teste17,123*456*789,4532015112830366
```

**Resultado esperado:**

```text
ValueError
```

**Resultado obtido:**

```text
ValueError: invalid literal for int() with base 10: '*'
```
>***O codigo quebrou.***
>**OBS**: Este erro é valido para todos os caracteres que não forem inteiros ou os definidos no `for`.

**Justificativa:**
O enunciado permite apenas `.`, `-` e `/` como separadores do CPF. Este teste verifica o que acontece quando uma pessoa utiliza outro caractere, como poderia ocorrer por erro de digitação.

**Possível erro de implementação detectado:**
Verifica se a função de validação possui tratamento para caracteres que não são números nem separadores permitidos.

---

# Justificativa da implementação em Python

A implementação foi realizada em Python utilizando principalmente operações sobre strings, listas, estruturas de repetição, list comprehensions, `enumerate()`, `len()`, `join()` e `strip()`.

A utilização dessas ferramentas permite trabalhar diretamente com os dados lidos do arquivo CSV sem a necessidade de realizar manualmente diversas operações de controle de memória e manipulação de caracteres que seriam necessárias em uma implementação convencional em C.

Um exemplo é a remoção dos separadores do CPF. Em Python, foi utilizada uma list comprehension para percorrer os caracteres e manter somente aqueles que não correspondem aos separadores permitidos:

```py
lst2 = [numeros for numeros in lst[1] if numeros != "." and numeros != "/" and numeros != "-"]
cpf_limpo = ''.join(lst2).strip()
```

Da mesma forma, os espaços do número do cartão são removidos por meio de uma list comprehension e posteriormente os caracteres são reunidos novamente com `join()`.

O `enumerate()` também simplifica o controle da numeração das linhas do arquivo, permitindo que o número da linha seja obtido diretamente durante a iteração, sem a necessidade de criar manualmente uma variável de controle.

Além disso, o Python permite trabalhar diretamente com strings e sequências de caracteres, o que facilita a adaptação do algoritmo de Luhn para percorrer o número do cartão de trás para frente.

Em uma implementação convencional em C, seria necessário trabalhar de forma mais explícita com vetores de caracteres, índices e controle de memória, aumentando a quantidade de código necessária para realizar operações equivalentes.

Dessa forma, para este exercício, a implementação em Python apresenta como principal vantagem a maior concisão e facilidade de manipulação das sequências e strings, mantendo o código mais próximo da lógica do problema.
