# Desafio 09: Similaridade de Sufixos

## Introdução
Para duas strings A e B, definimos a similaridade das strings como o comprimento do prefixo mais longo comum a ambas as strings. Neste desafio, você deve calcular a soma das similaridades de uma string S com cada um de seus sufixos.

## Como o desafio foi solucionado

Para resolver o desafio, foi implementada uma função `common_prefix_length` que calcula o comprimento do prefixo comum mais longo entre duas strings. Esta função percorre os caracteres das duas strings em paralelo e conta quantos caracteres consecutivos são iguais, até encontrar uma diferença ou chegar ao fim da menor das duas strings.

A função principal, `similarity`, é responsável por calcular a soma das similaridades da string original com cada um de seus sufixos. Ela faz isso seguindo estes passos:

1. **Iteração sobre a string original**: 
   - A função itera sobre a string, gerando todos os seus sufixos. 
   - Um sufixo é obtido removendo-se os primeiros caracteres da string original.
2. **Cálculo da similaridade**: 
   - Para cada sufixo gerado, a função chama `common_prefix_length` para calcular o comprimento do prefixo comum mais longo entre a string original e o sufixo atual.
3. **Soma das similaridades**: 
   - Todos os comprimentos dos prefixos comuns calculados são somados para obter a soma total das similaridades.

Essa abordagem garante que todas as similaridades entre a string original e seus sufixos sejam contabilizadas corretamente, resultando na soma total desejada.

## Como executar o código
1. Salve o código no arquivo `similarity.py`.

2. Abra o terminal e navegue até o diretório onde o arquivo está salvo.

3. Execute o comando abaixo para rodar os testes e interagir com o programa:
    ```bash
    python similarity.py
    ```

## Testes Esperados

Teste 1:
- Entrada: `s = "ababaa"`
- Saída Esperada: `11`

Teste 2:
- Entrada: `s = "aa"`
- Saída Esperada: `3`

Teste 3:
- Entrada: `s = "abcabccba"`
- Saída Esperada: `13`

Teste 4:
- Entrada: `s = "eabdcbbeeedbdaebdedbcbdcdeeaebbdbedbdbccbaaeababba"`
- Saída Esperada: `63`

Teste 5:
- Entrada: `s = "bcdedeccaabdaebdddaeedabedccdddccbbaaadcbbabccbaadbbbeddecacddbababbabadcbbbacecdaee"`
- Saída Esperada: `105`

Teste 6:
- Entrada: `s = "aeccbdaadbcebddbadbaedeceedbcdaaadcbdebecaddedebccdbadaeed"`
- Saída Esperada: `70`

## Interação com o Usuário
O código permite que o usuário insira valores personalizados para a string `s`. Durante a execução, você pode digitar os valores ou digitar 'sair' para finalizar o programa.

Exemplo de uso interativo:
```
Digite a string para calcular a similaridade com seus sufixos ou 'sair' para finalizar: ababaa
Entrada: s=ababaa
Resultado: 11

Digite a string para calcular a similaridade com seus sufixos ou 'sair' para finalizar: sair
Saindo...
```


