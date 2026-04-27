def selection_sort(arr):
    n = len(arr)
    # Percorre todo o array (exceto o último elemento)
    for i in range(n-1):
        # Assume que a posição atueal é o mínimo
        min_idx = i
         
        # Procura pelo menor elemento na porção não ordena
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                # Encontrou o elemento menor
                min_idx = j
        
        # Troca os elementos se um novo mínimo foi encontrado
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr



def insertion_sort(arr):
    # O tamanho da lista é obtido dinamicamente
    n = len(arr)

    # Começaos do segundo elemento (indice 1)
    # pois o primeiro elemento sozinho já é considerando "ordenado"
    for i in range(1, n):
        key = arr[i]   # O valor que queremos inserir na parte ordenada
        j = i - 1

        # Move os elementos maiores que a 'key' uma posição para a direita
        # até encontrarmos o lugar correto da 'key'.
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # Coloca a 'key' no espaço vazio criado pelo deslocamento
        arr[j + 1] = key

    return arr

### Atividade 2, entrega em 27/04/2026
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

### Atividade 2, entrega em 27/04/2026
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)




