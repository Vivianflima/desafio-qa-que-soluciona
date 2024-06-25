# Desafio do Dia 01: Escadaria

## Descrição do Desafio

O objetivo deste desafio é criar uma escadaria de tamanho `n` utilizando símbolos `#` e espaços. A base e a altura da escadaria são iguais ao valor de `n`, e a última linha não é precedida por espaços.

### Exemplo

Para uma escadaria de tamanho 4, o resultado deve ser:


## Solução

O desafio foi solucionado criando uma função `escadaria` que recebe um parâmetro `n` representando o tamanho da escadaria. A função utiliza um loop `for` para iterar de 1 até `n` e, em cada iteração, calcula e imprime a quantidade correta de espaços e símbolos `#` para formar a escadaria.

### Código

```python
def escadaria(n):
    for i in range(1, n + 1):
        espacos = ' ' * (n - i)
        hashtags = '#' * i
        print(espacos + hashtags)

# Função principal para realizar os testes
def main():
    # Testes iniciais fornecidos no desafio
    print("Teste 1:")
    escadaria(2)
    print("\nTeste 2:")
    escadaria(7)
    print("\nTeste 3:")
    escadaria(20)

    # Loop para permitir mais testes com entrada do usuário
    while True:
        try:
            # Recebe o tamanho da escadaria do usuário
            n = int(input("\nDigite o tamanho da escadaria (ou 0 para sair): "))
            if n == 0:
                print("Saindo...")
                break
            escadaria(n)
        except ValueError:
            print("Por favor, insira um número inteiro válido.")

if __name__ == "__main__":
    main()
```
## Explicação
### Função escadaria:

A função escadaria recebe um parâmetro n que representa o tamanho da escadaria.
Utiliza um loop for que vai de 1 até n (inclusive).
Para cada iteração, calcula a quantidade de espaços (' ' * (n - i)) e a quantidade de símbolos # ('#' * i).
Concatena os espaços e símbolos # e imprime a linha resultante.
Função main:

Executa os testes iniciais conforme fornecido no desafio.
Entra em um loop while True para permitir mais testes com entrada do usuário.
Se o usuário digitar 0, o loop termina e o programa sai.
Utiliza try-except para capturar possíveis entradas inválidas (não inteiros).
Como Executar
Certifique-se de ter o Python instalado em seu sistema.

Salve o código acima em um arquivo chamado escadaria.py.

Abra o terminal e navegue até a pasta onde o arquivo foi salvo.

Execute o comando:
`python escadaria.py`

O programa executará os testes iniciais e, em seguida, solicitará que você insira o tamanho da escadaria. Você pode continuar inserindo diferentes tamanhos até que digite 0 para sair.

## Exemplo de Execução
```
Teste 1:
 #
##

Teste 2:
      #
     ##
    ###
   ####
  #####
 ######
#######

Teste 3:
                   #
                  ##
                 ###
                ####
               #####
              ######
             #######
            ########
           #########
          ##########
         ###########
        ############
       #############
      ##############
     ###############
    ################
   #################
  ##################
 ###################
####################

Digite o tamanho da escadaria (ou 0 para sair): 5
    #
   ##
  ###
 ####
#####

Digite o tamanho da escadaria (ou 0 para sair): 0
Saindo...
```

### Dessa forma, o script permite que o usuário realize múltiplos testes interativamente, fornecendo diferentes tamanhos de escadarias conforme desejado.
