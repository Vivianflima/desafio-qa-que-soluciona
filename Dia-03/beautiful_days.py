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
