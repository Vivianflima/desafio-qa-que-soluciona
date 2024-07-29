# Desafio 10: Dijkstra - Menor Distância em Grafos

## Descrição do Desafio

Dado um grafo não direcionado e um nó inicial, determine o comprimento dos caminhos mais curtos do nó inicial para todos os outros nós no grafo. Se um nó for inacessível, sua distância é -1. Os nós serão numerados consecutivamente de 1 a n, e as arestas terão distâncias variáveis.

## Solução

A solução implementa o algoritmo de Dijkstra para calcular as distâncias mais curtas a partir de um nó inicial para todos os outros nós em um grafo. A função `shortestReach` recebe o número de nós, uma lista de arestas (onde cada aresta é representada por um trio de números inteiros: nó inicial, nó final e comprimento da aresta), e o nó inicial.

### Estrutura do Código

1. **Função `shortestReach`**: Implementa o algoritmo de Dijkstra usando uma fila de prioridade (min-heap) para encontrar os caminhos mais curtos.
2. **Função `get_user_input`**: Solicita a entrada do usuário para criar o grafo e definir o nó inicial. Inclui validação de entrada para garantir que os dados estejam no formato correto.
3. **Função `run_tests`**: Executa casos de teste predefinidos para verificar a correção da função `shortestReach`.
4. **Função `main`**: Exibe um menu para o usuário escolher entre executar testes automáticos ou inserir dados manualmente.

### Como Executar o Código

1. Certifique-se de ter o Python instalado no seu sistema.
2. Salve o código abaixo em um arquivo chamado `Dijkstra.py`.

```python
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
```

### Executando o Código

Para executar o código, siga os passos abaixo:

1. Abra um terminal ou prompt de comando.
2. Navegue até o diretório onde o arquivo `Dijkstra.py` está salvo.
3. Execute o comando:

```sh
python Dijkstra.py
```

### Interagindo com o Código

Ao executar o script, você verá o seguinte menu:

```
Escolha uma opção:
1. Executar testes automáticos
2. Inserir dados manualmente
Digite 1 ou 2:
```

- **Opção 1**: Executa uma série de testes predefinidos para verificar a correção do algoritmo.
- **Opção 2**: Permite ao usuário inserir manualmente os dados do grafo e calcular as distâncias mais curtas a partir do nó inicial.

#### Inserir Dados Manualmente

1. **Número de nós (n)**: Digite um número inteiro representando o número de nós no grafo.
2. **Número de arestas**: Digite um número inteiro representando o número de arestas no grafo.
3. **Arestas**: Para cada aresta, digite os nós de origem e destino e o peso da aresta no formato `u v w` (por exemplo, `1 2 10`).
4. **Nó inicial (s)**: Digite o nó inicial a partir do qual as distâncias serão calculadas.

O programa calculará e exibirá as distâncias mais curtas do nó inicial para todos os outros nós, ou `-1` se um nó for inacessível.

