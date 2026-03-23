import os
import time
from src.algoritmos import selection_sort, insertion_sort

def ler_arquivo(caminho):
    with open(caminho, 'r') as f:
        return [int(line.strip()) for line in f if line.strip()]

def rodar_experimento():
    pasta_dados = 'data'
    # Lista e ordena os arquivos para processar do menor para o maior
    arquivos = sorted([f for f in os.listdir(pasta_dados) if f.endswith('.in')])
    
    print(f"{'Arquivo':<25} | {'N':<8} | {'Selection (s)':<15} | {'Insertion (s)':<15}")
    print("-" * 70)

    for nome_arq in arquivos:
        caminho = os.path.join(pasta_dados, nome_arq)
        dados_originais = ler_arquivo(caminho)
        n = len(dados_originais)

        # Medição Selection Sort
        copia_sel = dados_originais.copy()
        inicio = time.perf_counter()
        selection_sort(copia_sel)
        fim = time.perf_counter()
        t_sel = fim - inicio

        # Medição Insertion Sort
        copia_ins = dados_originais.copy()
        inicio = time.perf_counter()
        insertion_sort(copia_ins)
        fim = time.perf_counter()
        t_ins = fim - inicio

        print(f"{nome_arq:<25} | {n:<8} | {t_sel:<15.5f} | {t_ins:<15.5f}")

if __name__ == "__main__":
    if not os.path.exists('data'):
        print("Erro: Pasta 'data' não encontrada.")
    else:
        rodar_experimento()
