# Validação de dados em CSV com Python

Projeto desenvolvido para a disciplina **ES453 — Introdução a Python**, da Universidade Federal de Pernambuco (UFPE), no segundo semestre de 2026.

## Sobre o projeto

O projeto consiste na implementação de um programa em Python capaz de ler um arquivo CSV contendo **nome, CPF e número de cartão de crédito**, verificar a validade dos dados e gerar um relatório com os erros encontrados.

A atividade teve como foco a aplicação prática de recursos da linguagem Python para manipulação de arquivos, strings e sequências, além da implementação de algoritmos de validação.

## Funcionalidades

O programa realiza:

* leitura do arquivo CSV;
* separação dos campos de cada registro;
* identificação de campos vazios;
* validação de CPF;
* validação de número de cartão de crédito;
* verificação da quantidade de dígitos;
* verificação dos dígitos verificadores;
* identificação da linha em que cada erro ocorreu;
* registro independente de múltiplos erros em uma mesma linha.

### Validação do CPF

O programa considera os separadores `.`, `-` e `/` permitidos no CPF. Esses caracteres são removidos antes da validação.

Após a limpeza dos dados, o programa verifica se o CPF possui 11 dígitos e realiza o cálculo dos dois dígitos verificadores.

### Validação do cartão

Os espaços utilizados para separar os grupos de dígitos do cartão são removidos antes da validação.

O número é então verificado utilizando o **algoritmo de Luhn**, além da verificação da quantidade de dígitos.

## Conceitos utilizados

Durante o desenvolvimento foram utilizados recursos da linguagem Python, entre eles:

* manipulação de arquivos com `open()` e `readlines()`;
* `split()` para separação dos campos;
* `strip()` para remoção de espaços;
* `join()` para reconstrução de strings;
* `len()` para contagem de dígitos;
* `enumerate()` para numeração das linhas;
* list comprehensions;
* estruturas de repetição;
* funções;
* manipulação de strings e sequências.

A implementação não utiliza bibliotecas externas nem imports da biblioteca padrão do Python, conforme especificado na atividade.

## Testes

Foram realizados testes com diferentes situações de entrada, incluindo:

* dados válidos;
* CPF inválido;
* cartão inválido;
* campos vazios;
* quantidade incorreta de dígitos;
* erros simultâneos de CPF e cartão na mesma linha;
* diferentes formatos de separação do CPF;
* espaços adicionais nos campos;
* entradas fora do formato esperado.

Os testes também foram utilizados durante o desenvolvimento para identificar comportamentos inesperados e corrigir problemas na implementação.

### Arquivos

**`Codigo_final.py`**
Programa principal. Realiza a leitura do arquivo CSV, processa os registros e gera o relatório de erros.

**`verificar_CPF.py`**
Contém a função responsável pela validação dos CPFs.

**`verificar_cartão.py`**
Contém a função responsável pela validação dos números de cartão utilizando o algoritmo de Luhn.

**`teste.csv`**
Arquivo utilizado como entrada para os testes do programa.

**`Relatorio.md`**
Documento com o desenvolvimento da atividade, decisões de implementação, testes realizados e análise dos resultados.

**`1a_lista.pdf`**
Enunciado original da atividade.

## Aprendizados

A atividade permitiu praticar a manipulação de arquivos e dados textuais em Python, principalmente por meio de strings, listas, list comprehensions e funções que trabalham com sequências.

Também foi possível aplicar os algoritmos de validação de CPF e Luhn em um programa que processa dados a partir de um arquivo, além de explorar diferentes casos de teste e situações de entrada.

---

**Disciplina:** ES453 — Introdução a Python
**Instituição:** Universidade Federal de Pernambuco (UFPE)
**Semestre:** 2026.2
