import sys
import time
import os
from src.algoritmos import selection_sort, insertion_sort, merge_sort, quick_sort

def ler_arquivo(caminho):
    """Lê o arquivo e retorna uma lista de inteiros."""
    try:
        with open(caminho, 'r') as f:
            # strip() remove espaços/quebras de linha; int() converte o valor
            return [int(linha.strip()) for linha in f if linha.strip()]
    except Exception as e:
        print(f"Erro ao ler {caminho}: {e}")
        return None

def executar_testes(caminho_arquivo):
    numeros = ler_arquivo(caminho_arquivo)
    if numeros is None: return

    n = len(numeros)
    nome_base = os.path.basename(caminho_arquivo)

    print(f"\n--- Processando: {nome_base} ({n} elementos) ---")

    # Teste Selection Sort
    dados_sel = numeros.copy()
    start = time.perf_counter()
    selection_sort(dados_sel)
    end = time.perf_counter()
    tempo_sel = end - start
    print(f"Selection Sort: {tempo_sel:.5f} segundos")

    # Teste Insertion Sort
    dados_ins = numeros.copy()
    start = time.perf_counter()
    insertion_sort(dados_ins)
    end = time.perf_counter()
    tempo_ins = end - start
    print(f"Insertion Sort: {tempo_ins:.5f} segundos")

    # Teste Merge Sort
    dados_merge = numeros.copy()
    start = time.perf_counter()
    merge_sort(dados_merge)
    end = time.perf_counter()
    tempo_merge = end - start
    print(f"Merge Sort: {tempo_merge:.5f} segundos")

    # Teste Quick Sort
    dados_quick = numeros.copy()
    start = time.perf_counter()
    quick_sort(dados_quick)
    end = time.perf_counter()
    tempo_quick = end - start
    print(f"Quick Sort: {tempo_quick:.5f} segundos")




if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 main.py <caminho_do_arquivo>")
    else:
        executar_testes(sys.argv[1])
