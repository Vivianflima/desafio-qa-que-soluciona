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
