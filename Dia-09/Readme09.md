# Desafio 09: Similaridade de Sufixos

## Introdução
Para duas strings A e B, definimos a similaridade das strings como o comprimento do prefixo mais longo comum a ambas as strings. Neste desafio, você deve calcular a soma das similaridades de uma string S com cada um de seus sufixos.

## Como o desafio foi solucionado
A solução implementa uma função `common_prefix_length` que calcula o comprimento do prefixo comum mais longo entre duas strings. A função principal `similarity` calcula a soma das similaridades da string original com cada um de seus sufixos, chamando `common_prefix_length` para cada sufixo gerado a partir da string original.

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


