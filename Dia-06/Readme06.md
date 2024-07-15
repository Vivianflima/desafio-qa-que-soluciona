# Desafio 06: Números Quadrados

## Introdução
Watson gosta de desafiar a habilidade matemática de Sherlock. Ele fornecerá um valor inicial e final que descrevem um intervalo de inteiros, inclusive nos limites. Sherlock deve determinar o número de inteiros quadrados dentro desse intervalo.

Um inteiro quadrado é um número que é o quadrado de um inteiro, por exemplo, 1 (1²), 4 (2²), 9 (3²), etc.

## Como o desafio foi solucionado
Para resolver o desafio de determinar o número de inteiros quadrados dentro de um intervalo, seguimos os passos abaixo:

1. **Calcular as raízes quadradas dos limites do intervalo**: Primeiramente, calculamos a raiz quadrada do limite inferior e superior do intervalo.
2. **Arredondar as raízes quadradas**: Arredondamos a raiz quadrada do limite inferior para cima e a raiz quadrada do limite superior para baixo.
3. **Contar os inteiros quadrados**: Contamos os inteiros quadrados entre os valores arredondados.

## Como executar o código
1. Salve o código no arquivo `squares.py`.

2. Abra o terminal e navegue até o diretório onde o arquivo está salvo.

3. Execute o comando abaixo para rodar os testes e interagir com o programa:
    ```bash
    python squares.py
    ```

## Testes Esperados

Teste 1:
- Entrada: `a = 3, b = 9`
- Saída Esperada: `2`

Teste 2:
- Entrada: `a = 24, b = 49`
- Saída Esperada: `3`

Teste 3:
- Entrada: `a = 17, b = 24`
- Saída Esperada: `0`

Teste 4:
- Entrada: `a = 35, b = 70`
- Saída Esperada: `3`

Teste 5:
- Entrada: `a = 100, b = 1000`
- Saída Esperada: `22`

Teste 6:
- Entrada: `a = 59, b = 999999922`
- Saída Esperada: `31615`

Teste 7:
- Entrada: `a = 9, b = 999999966`
- Saída Esperada: `31620`

Teste 8:
- Entrada: `a = 12, b = 999999988`
- Saída Esperada: `31619`

## Interação com o Usuário
O código permite que o usuário insira valores personalizados para `a` e `b`. Durante a execução, você pode digitar os valores ou digitar 'sair' para finalizar o programa.

Exemplo de uso interativo:

```
Digite os valores de 'a' e 'b' (separados por espaço) ou 'sair' para finalizar: 3 9
Entrada: a=3, b=9
Número de inteiros quadrados: 2

Digite os valores de 'a' e 'b' (separados por espaço) ou 'sair' para finalizar: 10 100
Entrada: a=10, b=100
Número de inteiros quadrados: 8

Digite os valores de 'a' e 'b' (separados por espaço) ou 'sair' para finalizar: sair
Saindo...
```
