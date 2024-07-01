# Desafio do Dia 02: Contador de Vales

## Descrição do Desafio

Um ávido caminhante mantém registros meticulosos de suas caminhadas. Durante a última caminhada que durou exatamente `N` passos, foi registrado se cada passo era uma subida (`U`) ou uma descida (`D`). As caminhadas sempre começam e terminam ao nível do mar, e cada passo para cima ou para baixo representa uma mudança de uma unidade de altitude. Definimos os seguintes termos:

- **Montanha**: uma sequência de passos consecutivos acima do nível do mar, começando com um passo para cima do nível do mar e terminando com um passo para baixo até o nível do mar.
- **Vale**: uma sequência de passos consecutivos abaixo do nível do mar, começando com um passo para baixo do nível do mar e terminando com um passo para cima até o nível do mar.

Dado a sequência de passos de subida e descida durante uma caminhada, descubra e imprima o número de vales percorridos.

## Solução

O desafio foi solucionado criando uma função `countingValleys` que recebe uma string representando o caminho percorrido. A função rastreia a altitude atual para determinar quando um vale começa e termina.

### Código

```python
def countingValleys(path):
    altitude = 0
    vales = 0
    in_vale = False

    for step in path:
        if step == 'U':
            altitude += 1
        elif step == 'D':
            altitude -= 1

        # Entrando em um vale
        if altitude < 0 and not in_vale:
            in_vale = True

        # Saindo de um vale
        if altitude == 0 and in_vale:
            vales += 1
            in_vale = False

    return vales

# Função principal para realizar os testes
def main():
    # Testes fornecidos no desafio
    print("Teste 1:")
    path = "DDUUDDUDUUUD"
    resultado = countingValleys(path)
    print(f"Entrada: path = \"{path}\"\nResultado: {resultado}\n")  # Saída Esperada: 2

    print("Teste 2:")
    path = "UDUUUDUDDD"
    resultado = countingValleys(path)
    print(f"Entrada: path = \"{path}\"\nResultado: {resultado}\n")  # Saída Esperada: 0

    print("Teste 3:")
    path = "DUDUDUDUDUDUDU"
    resultado = countingValleys(path)
    print(f"Entrada: path = \"{path}\"\nResultado: {resultado}\n")  # Saída Esperada: 7

    print("Teste 4:")
    path = "DDUUUUDDDUUUDDDU"
    resultado = countingValleys(path)
    print(f"Entrada: path = \"{path}\"\nResultado: {resultado}\n")  # Saída Esperada: 3

    # Loop para permitir mais testes com entrada do usuário
    while True:
        path = input("\nDigite a sequência de passos (ou 'sair' para finalizar): ")
        if path.lower() == 'sair':
            print("Saindo...")
            break
        resultado = countingValleys(path)
        print(f"Número de vales percorridos: {resultado}")

if __name__ == "__main__":
    main()
```
### Explicação
Função `countingValleys(path)`:

Inicializa altitude, vales, e in_vale.
Itera sobre cada passo na string path.
Atualiza a altitude com base no passo ('U' para subir, 'D' para descer).
Se a altitude é negativa e in_vale é False, significa que estamos entrando em um vale, então define in_vale como True.
Se a altitude volta a 0 e in_vale é True, significa que saímos de um vale, então incrementa vales e define in_vale como False.

Função `main()`:

Executa os testes fornecidos no desafio para verificar se a função countingValleys está correta.
Entra em um loop para permitir que o usuário insira sequências de passos e exibe o número de vales percorridos.
O loop pode ser interrompido digitando 'sair'.

### Como Executar
1. Certifique-se de ter o Python instalado em seu sistema.

2. Salve o código acima em um arquivo chamado `contador_vales.py`.

2. Abra o terminal e navegue até a pasta onde o arquivo foi salvo.

4. Execute o comando:
`python counting_valleys.py`

5. Observe as saídas para os testes iniciais e, em seguida, insira diferentes sequências de passos conforme solicitado pelo programa. Para sair, digite 'sair'.

### Exemplos de Execução
```Teste 1:
Entrada: path = "DDUUDDUDUUUD"
Resultado: 2

Teste 2:
Entrada: path = "UDUUUDUDDD"
Resultado: 0

Teste 3:
Entrada: path = "DUDUDUDUDUDUDU"
Resultado: 7

Teste 4:
Entrada: path = "DDUUUUDDDUUUDDDU"
Resultado: 3

Digite a sequência de passos (ou 'sair' para finalizar): DDUU
Número de vales percorridos: 1

Digite a sequência de passos (ou 'sair' para finalizar): sair
Saindo...
```
Dessa forma, o script inclui os testes iniciais com as entradas e saídas esperadas detalhadas, além de permitir que o usuário realize testes adicionais interativamente.

