# Ordenação por Comparação 1 - UFPB
**Disciplina:** Estrutura de Dados e Complexidade de Algoritmos  
**Entrega:** 26/03/2026

## Descrição
Este projeto contém a implementação manual dos algoritmos **Selection Sort** e **Insertion Sort** em Python, conforme as especificações da atividade. 
O objetivo é analisar o desempenho de ambos em vetores de diferentes tamanhos (1.000 a 100.000 elementos) contendo números inteiros positivos e negativos.

## Como Executar
1. **Para rodar todos os testes (12 arquivos):**
```bash
   python3 testartudo.py
```

2. **Para rodar um arquivo específico:**
```bash
   python3 main.py data/nome_do_arquivo.in
```
## Resultados de Desempenho
Os testes foram realizados processando 12 arquivos de entrada. Os tempos abaixo representam a execução em segundos (O(n²)).

```bash
moraes@vm-marcelo:~/EDCA/ordena-compara-ufpb$ python3 testartudo.py
Arquivo                   | N        | Selection (s)   | Insertion (s)
----------------------------------------------------------------------
num.1000.1.in             | 1001     | 0.01219         | 0.00999
num.1000.2.in             | 1001     | 0.01184         | 0.01037
num.1000.3.in             | 1001     | 0.01255         | 0.01001
num.1000.4.in             | 1001     | 0.01250         | 0.00926
num.10000.1.in            | 10001    | 1.27666         | 1.05045
num.10000.2.in            | 10001    | 1.24086         | 1.14013
num.10000.3.in            | 10001    | 1.25465         | 1.03896
num.10000.4.in            | 10001    | 1.20711         | 0.93826
num.100000.1.in           | 100001   | 125.69829       | 109.80772
num.100000.2.in           | 100001   | 130.24198       | 115.40670
num.100000.3.in           | 100001   | 127.15620       | 108.32106
num.100000.4.in           | 100001   | 123.00459       | 100.07650

```


## Estrutura do Repositório
```bash

ordena-compara-ufpb/
|--- data/                      # Arquivos de entrada fornecidos pelo professor.
|--- src/                       # Pasta com implementação dos algoritmos.
|     |--- algoritmos.py        # Implementações dos algoritmos (selection_sort e insertion_sort).
|--- saidas/                    # Pasta com arquivos de saídas de execuções de prova.
|--- main.py                    # Script de entrada para execução individual.
|--- testartudo.py              # Automação para processar os 12 casos de teste.
|--- Makefile                   # Automação de comandos de linha de comando
|--- README.md                  

```
