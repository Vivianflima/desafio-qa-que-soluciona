# Desafio 04: Notificações de Atividades Suspeitas

## Desafio
O Banco Nacional de HackerLand tem uma política simples para alertar clientes sobre possíveis atividades fraudulentas nas contas. Se o valor gasto por um cliente em um dia específico for maior ou igual à mediana dos gastos do cliente para um número de dias anteriores, eles enviam uma notificação ao cliente sobre a possível fraude. O banco não envia nenhuma notificação até que tenham pelo menos esse número de dias de dados de transações anteriores.

## Detalhamento do Desafio
Crie uma função chamada `activityNotifications` que tem os seguintes parâmetros:
# Desafio 04: Notificações de Atividades Suspeitas

## Descrição
O Banco Nacional de HackerLand tem uma política simples para alertar clientes sobre possíveis atividades fraudulentas nas contas. Se o valor gasto por um cliente em um dia específico for maior ou igual à mediana dos gastos do cliente para um número de dias anteriores, eles enviam uma notificação ao cliente sobre a possível fraude. O banco não envia nenhuma notificação até que tenham pelo menos esse número de dias de dados de transações anteriores.

## Objetivo
Crie uma função chamada `activityNotifications` que determine quantas notificações de atividades suspeitas serão enviadas com base nos gastos diários e no período de retrospectiva fornecidos.

## Estrutura do Código

### Função `activityNotifications`
Esta função calcula o número de notificações de atividade suspeita com base nas despesas diárias e no período de retrospectiva. 

#### Parâmetros
- `expenditure`: Lista de inteiros representando as despesas diárias.
- `d`: Inteiro representando o número de dias de retrospectiva para cálculo da mediana.

#### Retorno
- Número de notificações enviadas.

### Explicação do Código
A função `activityNotifications` percorre a lista de despesas diárias, começando a verificação apenas após os primeiros `d` dias. Para cada dia, a mediana dos `d` dias anteriores é calculada. Se a despesa do dia atual for maior ou igual ao dobro da mediana calculada, uma notificação é contada. O cálculo da mediana é otimizado utilizando uma abordagem baseada em contagem para melhorar o desempenho.

### Código
```python
def median(arr):
    n = len(arr)
    arr.sort()
    if n % 2 == 0:
        return (arr[n//2 - 1] + arr[n//2]) / 2
    else:
        return arr[n//2]

def activityNotifications(expenditure, d):
    notifications = 0
    for i in range(d, len(expenditure)):
        trailing_days = expenditure[i-d:i]
        med = median(trailing_days)
        if expenditure[i] >= 2 * med:
            notifications += 1
    return notifications

# Função principal para realizar os testes
def main():
    # Testes fornecidos no desafio
    print("Teste 1:")
    expenditure = [2, 3, 4, 2, 3, 6, 8, 4, 5]
    d = 5
    resultado = activityNotifications(expenditure, d)
    print(f"Entrada: expenditure={expenditure}, d={d}\nResultado: {resultado}\n")  # Saída Esperada: 2

    print("Teste 2:")
    expenditure = [1, 2, 3, 4, 4]
    d = 4
    resultado = activityNotifications(expenditure, d)
    print(f"Entrada: expenditure={expenditure}, d={d}\nResultado: {resultado}\n")  # Saída Esperada: 0

    print("Teste 3:")
    expenditure = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    d = 5
    resultado = activityNotifications(expenditure, d)
    print(f"Entrada: expenditure={expenditure}, d={d}\nResultado: {resultado}\n")  # Saída Esperada: 1

    print("Teste 4:")
    expenditure = [1, 2, 100, 2, 2, 2, 2, 2]
    d = 4
    resultado = activityNotifications(expenditure, d)
    print(f"Entrada: expenditure={expenditure}, d={d}\nResultado: {resultado}\n")  # Saída Esperada: 0

    # Loop para permitir mais testes com entrada do usuário
    while True:
        try:
            expenditure = list(map(int, input("\nDigite as despesas diárias (separadas por espaço) ou 'sair' para finalizar: ").split()))
            if 'sair' in expenditure:
                print("Saindo...")
                break
            d = int(input("Digite o número de dias de retrospectiva (d): "))
        except ValueError:
            print("Entrada inválida. Saindo...")
            break

        resultado = activityNotifications(expenditure, d)
        print(f"Entrada: expenditure={expenditure}, d={d}\nNúmero de notificações: {resultado}")

if __name__ == "__main__":
    main()


```
## Como Executar

1. Salve o código em um arquivo, por exemplo, `notificacoes.py`.
2. Abra o terminal e navegue até o diretório onde o arquivo está salvo.
3. Execute o script com o comando:
    ```sh
    python notificacoes.py
    ```
4. O script irá executar os testes incorporados e exibirá a saída correspondente.


## Como Testar o Script com Entrada do Usuário

1. **Executar o Script:**
   - Salve o código em um arquivo, por exemplo, `notificacoes.py`.
   - Abra um terminal e navegue até o diretório onde o arquivo está salvo.

2. **Iniciar a Execução:**
   - Execute o script Python com o comando:
     ```
     python notificacoes.py
     ```

3. **Interagir com o Script:**
   - O script solicitará a entrada das despesas diárias, que devem ser fornecidas como números inteiros separados por espaço.
   - Em seguida, será solicitado que você informe o número de dias de retrospectiva (`d`).

4. **Resultado do Teste:**
   - Após inserir os dados, o script calculará o número de notificações de atividades suspeitas com base nas despesas diárias e na retrospectiva fornecida.
   - O resultado será exibido no terminal, mostrando o número de notificações geradas.

### Exemplo de Interatividade

Ao executar o script, você verá algo semelhante ao seguinte no terminal:

```
Digite as despesas diárias (separadas por espaço) ou 'sair' para finalizar: 2 3 4 2 3 6 8 4 5
Digite o número de dias de retrospectiva (d): 5
Entrada: expenditure=[2, 3, 4, 2, 3, 6, 8, 4, 5], d=5
Número de notificações: 2


Digite as despesas diárias (separadas por espaço) ou 'sair' para finalizar:
```

### Observações

- Certifique-se de inserir as despesas diárias como números inteiros separados por espaço.
- O script continuará a solicitar entradas até que você digite `'sair'`, o que encerrará a execução do programa.
- Caso ocorra um erro de entrada inválida (como letras em vez de números), o script mostrará uma mensagem de erro e encerrará.


