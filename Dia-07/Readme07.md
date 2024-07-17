# Desafio 07: Verificador de Senhas

## Introdução
Há n usuários registrados no site CuteKittens.com. Cada um deles tem uma senha única representada por `pass[1], pass[2], ..., pass[N]`. Como este é um site muito adorável, muitas pessoas querem acessar as fotos fofas dos gatinhos. Mas o administrador não quer que o site esteja disponível para o público em geral, então apenas aqueles que têm senhas podem acessá-lo.

Yu, sendo um hacker fabuloso, encontra uma brecha no sistema de verificação de senhas. Uma string que é uma concatenação de uma ou mais senhas, em qualquer ordem, também é aceita pelo sistema de verificação de senhas. Qualquer senha pode aparecer uma ou mais vezes nessa string. Dado o acesso a cada uma das senhas, e também a uma string de tentativa de login, determine se essa string será aceita pelo sistema de verificação de senhas do site. Se toda a string puder ser criada concatenando senhas, ela é aceita. Nesse caso, retorne as senhas na ordem em que devem ser concatenadas, separadas por um espaço em uma linha. Se a tentativa de senha não for aceita, retorne 'WRONG PASSWORD'.

## Como o desafio foi solucionado
A solução utiliza uma abordagem de busca recursiva com memoização para verificar se a string de tentativa de login pode ser formada concatenando as senhas fornecidas. A função principal `passwordCracker` chama uma função auxiliar `canCrack` que verifica se a string pode ser quebrada em substrings correspondentes às senhas fornecidas. A memoização é utilizada para armazenar resultados intermediários e evitar recomputações desnecessárias.

## Como executar o código
1. Salve o código no arquivo `passwords.py`.

2. Abra o terminal e navegue até o diretório onde o arquivo está salvo.

3. Execute o comando abaixo para rodar os testes e interagir com o programa:
    ```bash
    python passwords.py
    ```

## Testes Esperados

Teste 1:
- Entrada: `passwords = ["because", "can", "do", "must", "we", "what"], loginAttempt = "wedowhatwemustbecausewecan"`
- Saída Esperada: `"we do what we must because we can"`

Teste 2:
- Entrada: `passwords = ["hello", "planet"], loginAttempt = "helloworld"`
- Saída Esperada: `"WRONG PASSWORD"`

Teste 3:
- Entrada: `passwords = ["ab", "abcd", "cd"], loginAttempt = "abcd"`
- Saída Esperada: `"ab cd"` ou `"abcd"`

## Interação com o Usuário
O código permite que o usuário insira valores personalizados para `passwords` e `loginAttempt`. Durante a execução, você pode digitar os valores ou digitar 'sair' para finalizar o programa.

Exemplo de uso interativo:
```
Digite as senhas (separadas por espaço) ou 'sair' para finalizar: ab abcd cd
Digite a tentativa de login: abcd
Entrada: passwords=['ab', 'abcd', 'cd'], loginAttempt=abcd
Resultado: ab cd

Digite as senhas (separadas por espaço) ou 'sair' para finalizar: sair
Saindo...
```
