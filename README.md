# Ordenação por Comparação 1 - UFPB
**Disciplina:** Estrutura de Dados e Complexidade de Algoritmos  
**Entrega 01:** 26/03/2026
**Entrega 02:** 27/04/2026

## Descrição
Este projeto contém a implementação manual dos algoritmos **Selection Sort** e **Insertion Sort** em Python, conforme as especificações da atividade. 
O objetivo é analisar o desempenho de ambos em vetores de diferentes tamanhos (1.000 a 100.000 elementos) contendo números inteiros positivos e negativos.

Foi feita a inclusão dos algoritmos **Merge Sort** e **Quick Sort** em Python, conforme as especificações da atividade para a entrega de 27/04.
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
Os testes foram realizados processando 12 arquivos de entrada. Os tempos abaixo representam a execução em segundos.

```bash
moraes@vm-marcelo:~/EDCA/ordena-compara-ufpb$ python3 testartudo.py
Arquivo                   | N        | Selection (s)   | Insertion (s)   | Merge (s)       | Quick (s)
-------------------------------------------------------------------------------------------------------
num.1000.1.in             | 1001     | 0.01838         | 0.01523         | 0.00097         | 0.00076
num.1000.2.in             | 1001     | 0.01749         | 0.01138         | 0.00261         | 0.00073
num.1000.3.in             | 1001     | 0.01564         | 0.01182         | 0.00096         | 0.00081
num.1000.4.in             | 1001     | 0.01362         | 0.00884         | 0.00101         | 0.00077
num.10000.1.in            | 10001    | 1.47103         | 1.25691         | 0.01258         | 0.00809
num.10000.2.in            | 10001    | 1.43616         | 1.16837         | 0.01166         | 0.00735
num.10000.3.in            | 10001    | 1.38996         | 1.22437         | 0.01176         | 0.00662
num.10000.4.in            | 10001    | 1.38631         | 1.07943         | 0.01203         | 0.01015
num.100000.1.in           | 100001   | 125.99249       | 110.86685       | 0.13047         | 0.08131
num.100000.2.in           | 100001   | 126.82044       | 112.07645       | 0.13146         | 0.08500
num.100000.3.in           | 100001   | 126.42213       | 110.58097       | 0.12845         | 0.08329
num.100000.4.in           | 100001   | 120.39213       | 97.34792        | 0.13022         | 0.08270
(venv) moraes@vm-marcelo:~/EDCA/ordena-compara-ufpb$


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
