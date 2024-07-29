import heapq

def shortestReach(n, edges, s):
    # Representação do grafo
    graph = {i: [] for i in range(1, n + 1)}
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    # Inicialização das distâncias
    distances = {i: float('inf') for i in range(1, n + 1)}
    distances[s] = 0
    
    # Fila de prioridade (min-heap)
    heap = [(0, s)]
    
    while heap:
        current_distance, u = heapq.heappop(heap)
        
        if current_distance > distances[u]:
            continue
        
        for v, weight in graph[u]:
            distance = current_distance + weight
            if distance < distances[v]:
                distances[v] = distance
                heapq.heappush(heap, (distance, v))
    
    # Construção do resultado
    result = []
    for i in range(1, n + 1):
        if i == s:
            continue
        if distances[i] == float('inf'):
            result.append("-1")
        else:
            result.append(str(distances[i]))
    
    return " ".join(result)

# Função para obter entradas do usuário com validação
def get_user_input():
    n = int(input("Digite o número de nós (n): "))
    e = int(input("Digite o número de arestas: "))
    
    edges = []
    for _ in range(e):
        while True:
            try:
                u, v, w = map(int, input("Digite a aresta (formato: u v w): ").split())
                edges.append((u, v, w))
                break
            except ValueError:
                print("Entrada inválida. Por favor, digite novamente no formato: u v w")
    
    s = int(input("Digite o nó inicial (s): "))
    
    return n, edges, s

# Testes fornecidos no enunciado
def run_tests():
    test_cases = [
        (4, [(1, 2, 24), (1, 4, 20), (3, 1, 3), (4, 3, 12)], 1, "24 3 15"),
        (5, [(1, 2, 10), (1, 3, 6), (2, 4, 8)], 2, "10 16 8 -1"),
        (6, [(1, 2, 7), (1, 3, 9), (1, 6, 14), (2, 3, 10), (2, 4, 15), (3, 4, 11), (3, 6, 2), (4, 5, 6), (5, 6, 9)], 1, "7 9 20 20 11"),
        (3, [(1, 2, 1), (2, 3, 1)], 1, "1 2"),
        (4, [(1, 2, 1), (2, 3, 2), (3, 4, 3)], 2, "1 2 5")
    ]

    for i, (n, edges, s, expected) in enumerate(test_cases):
        print(f"Executando Teste {i + 1}:")
        print(f"Entrada: n = {n}, edges = {edges}, s = {s}")
        result = shortestReach(n, edges, s)
        print(f"Saída Esperada: {expected}")
        print(f"Saída Obtida: {result}")
        assert result == expected, f"Teste {i + 1} falhou: esperado {expected}, obtido {result}"
        print(f"Teste {i + 1} passou\n")

# Menu para selecionar entre testes automáticos ou entradas do usuário
def main():
    print("Escolha uma opção:")
    print("1. Executar testes automáticos")
    print("2. Inserir dados manualmente")
    choice = input("Digite 1 ou 2: ")
    
    if choice == "1":
        run_tests()
    elif choice == "2":
        n, edges, s = get_user_input()
        result = shortestReach(n, edges, s)
        print(f"Distâncias mais curtas: {result}")
    else:
        print("Opção inválida")

if __name__ == "__main__":
    main()
