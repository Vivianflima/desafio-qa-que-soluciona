# Desafio do Dia 03: Dias Belos

## Descrição do Desafio

Lily gosta de jogar com números e criou um novo jogo onde determina a diferença entre um número e seu inverso. Por exemplo, dado o número 123, seu inverso é 321. A diferença entre eles é 198. O número 120 revertido é 21, e sua diferença é 99.

Ela decidiu aplicar seu jogo para tomar decisões, olhando para um intervalo numerado de dias e indo ao cinema apenas em um "dia belo".

**Definição de um Dia Belo**: 
Um dia é considerado belo se a diferença entre o número do dia e seu inverso é divisível por `k`.

**Objetivo**:
Dado um intervalo de dias numerados, `i` e `j`, e um número `k`, determine o número de dias no intervalo que são belos. Retorne o número de dias belos no intervalo.

## Exemplos

Dado `i = 20`, `j = 23` e `k = 6`, a saída seria 2, pois existem apenas 2 dias belos entre os dias 20 e 23.

### Explicação:

- Dia 20 é belo porque a seguinte avaliação resulta em um número inteiro: `(20 - 2) / 6 = 3`
- Dia 21 não é belo porque a seguinte avaliação não resulta em um número inteiro: `(21 - 12) / 6 = 1.5`
- Dia 22 é belo porque a seguinte avaliação resulta em um número inteiro: `(22 - 22) / 6 = 0`
- Dia 23 não é belo porque a seguinte avaliação não resulta em um número inteiro: `(23 - 32) / 6 = -1.5`

## Solução

### Conhecimentos necessários:

1. **Manipulação de Strings e Números**: Converter números em strings e vice-versa para poder inverter os números.
2. **Divisibilidade e Operações Matemáticas**: Usar operações matemáticas básicas e entender o conceito de divisibilidade.
3. **Loops**: Iterar sobre uma sequência de números, verificando cada dia no intervalo dado.

### Código

```python
def reverse_number(n):
    return int(str(n)[::-1])

def beautifulDays(i, j, k):
    beautiful_days_count = 0

    for day in range(i, j + 1):
        reversed_day = reverse_number(day)
        if abs(day - reversed_day) % k == 0:
            beautiful_days_count += 1

    return beautiful_days_count

# Função principal para realizar os testes
def main():
    # Testes fornecidos no desafio
    print("Teste 1:")
    i, j, k = 20, 23, 6
    resultado = beautifulDays(i, j, k)
    print(f"Entrada: i={i}, j={j}, k={k}\nResultado: {resultado}\n")  # Saída Esperada: 2

    print("Teste 2:")
    i, j, k = 13, 45, 3
    resultado = beautifulDays(i, j, k)
    print(f"Entrada: i={i}, j={j}, k={k}\nResultado: {resultado}\n")  # Saída Esperada: 33

    print("Teste 3:")
    i, j, k = 1, 2000000, 2000000
    resultado = beautifulDays(i, j, k)
    print(f"Entrada: i={i}, j={j}, k={k}\nResultado: {resultado}\n")  # Saída Esperada: 2998

    print("Teste 4:")
    i, j, k = 1, 2000000, 23047885
    resultado = beautifulDays(i, j, k)
    print(f"Entrada: i={i}, j={j}, k={k}\nResultado: {resultado}\n")  # Saída Esperada: 2998

    # Loop para permitir mais testes com entrada do usuário
    while True:
        try:
            i = int(input("\nDigite o dia inicial (i) (ou 'sair' para finalizar): "))
            j = int(input("Digite o dia final (j): "))
            k = int(input("Digite o divisor (k): "))
        except ValueError:
            print("Saindo...")
            break

        resultado = beautifulDays(i, j, k)
        print(f"Entrada: i={i}, j={j}, k={k}\nNúmero de dias belos: {resultado}")

if __name__ == "__main__":
    main()
```
### Explicação do Código

1. **Função `reverse_number(n)`**:
    - Converte o número `n` em uma string.
    - Inverte a string.
    - Converte a string invertida de volta para um número inteiro.

2. **Função `beautifulDays(i, j, k)`**:
    - Inicializa um contador `beautiful_days_count`.
    - Itera sobre o intervalo de dias de `i` a `j` (inclusive).
    - Para cada dia, calcula seu inverso usando a função `reverse_number`.
    - Verifica se a diferença entre o dia e seu inverso é divisível por `k`.
    - Incrementa o contador se a condição for satisfeita.
    - Retorna o número total de dias belos.

3. **Função `main()`**:
    - Executa os testes fornecidos no desafio para verificar se a função `beautifulDays` está correta.
    - Entra em um loop para permitir que o usuário insira intervalos e divisores, e exibe o número de dias belos encontrados.
    - O loop pode ser interrompido com uma entrada inválida (para simular 'sair').

## Como Executar

1. Certifique-se de ter o Python instalado em seu sistema.
2. Salve o código acima em um arquivo chamado `beautiful_days.py`.
3. Abra o terminal e navegue até a pasta onde o arquivo foi salvo.
4. Execute o comando:

```
   python beautiful_days.py
```
5. Observe as saídas para os testes iniciais e, em seguida, insira diferentes intervalos e divisores conforme solicitado pelo programa. Para sair, insira uma entrada inválida para i.

## Exemplos de Saída
```
Teste 1:
Entrada: i=20, j=23, k=6
Resultado: 2

Teste 2:
Entrada: i=13, j=45, k=3
Resultado: 33

Teste 3:
Entrada: i=1, j=2000000, k=2000000
Resultado: 2998

Teste 4:
Entrada: i=1, j=2000000, k=23047885
Resultado: 2998

Digite o dia inicial (i) (ou 'sair' para finalizar): 20
Digite o dia final (j): 30
Digite o divisor (k): 7
Entrada: i=20, j=30, k=7
Número de dias belos: 1

Digite o dia inicial (i) (ou 'sair' para finalizar): sair
Saindo...
```

