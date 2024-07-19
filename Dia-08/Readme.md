# Desafio 08: Criptografia de Texto

## Introdução
Um texto em inglês precisa ser criptografado usando o seguinte esquema de criptografia. Primeiro, os espaços são removidos do texto. Seja L o comprimento deste texto. Em seguida, os caracteres são escritos em uma grade, cujas linhas e colunas têm as seguintes restrições:

Se L for o comprimento da string sem espaços, então a grade deve ter floor(L) linhas e ceil(L) colunas, onde o número de linhas deve ser menor ou igual ao número de colunas e a área da grade (linhas x colunas) deve ser mínima, mas ainda capaz de conter L caracteres. A mensagem codificada é obtida exibindo os caracteres de cada coluna, com um espaço entre os textos das colunas.

## Como o desafio foi solucionado
A solução remove os espaços da string de entrada, calcula o número de linhas e colunas necessárias para a grade e, em seguida, lê os caracteres verticalmente para formar a mensagem criptografada. A função principal `encryption` utiliza a biblioteca `math` para calcular as dimensões da grade e um loop para construir a mensagem criptografada.

## Como executar o código
1. Salve o código no arquivo `encryption.py`.

2. Abra o terminal e navegue até o diretório onde o arquivo está salvo.

3. Execute o comando abaixo para rodar os testes e interagir com o programa:
    ```bash
    python encryption.py
    ```

## Testes Esperados

Teste 1:
- Entrada: `s = "haveaniceday"`
- Saída Esperada: `"hae and via ecy"`

Teste 2:
- Entrada: `s = "feedthedog"`
- Saída Esperada: `"fto ehg ee dd"`

Teste 3:
- Entrada: `s = "chillout"`
- Saída Esperada: `"clu hlt io"`

Teste 4:
- Entrada: `s = "iuo"`
- Saída Esperada: `"io u"`

Teste 5:
- Entrada: `s = "wclwfoznbmyycxvaxagjhtexdkwjqhlojykopldsxesbbnezqmixfpujbssrbfhlgubvfhpfliimvmnny"`
- Saída Esperada: `"wmgjpnull cyjqlejgi lyhhdzbui wctlsqsbm fxeoxmsvv ovxjeirfm zadysxbhn nxkkbffpn bawobphfy"`

## Interação com o Usuário
O código permite que o usuário insira valores personalizados para a string `s`. Durante a execução, você pode digitar os valores ou digitar 'sair' para finalizar o programa.

Exemplo de uso interativo:
```
Digite a string para criptografar ou 'sair' para finalizar: haveaniceday
Entrada: s=haveaniceday
Resultado: hae and via ecy

Digite a string para criptografar ou 'sair' para finalizar: sair
Saindo...
```

