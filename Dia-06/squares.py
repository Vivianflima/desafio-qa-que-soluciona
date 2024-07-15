import math

def squares(a, b):
    # Calcular as raízes quadradas dos limites
    start = math.ceil(math.sqrt(a))
    end = math.floor(math.sqrt(b))
    
    # Contar os inteiros quadrados
    return max(0, end - start + 1)

# Função principal para realizar os testes
def main():
    # Testes fornecidos no desafio
    print("Teste 1:")
    a, b = 3, 9
    resultado = squares(a, b)
    print(f"Entrada: a={a}, b={b}\nResultado: {resultado}\n")  # Saída Esperada: 2

    print("Teste 2:")
    a, b = 24, 49
    resultado = squares(a, b)
    print(f"Entrada: a={a}, b={b}\nResultado: {resultado}\n")  # Saída Esperada: 3

    print("Teste 3:")
    a, b = 17, 24
    resultado = squares(a, b)
    print(f"Entrada: a={a}, b={b}\nResultado: {resultado}\n")  # Saída Esperada: 0

    print("Teste 4:")
    a, b = 35, 70
    resultado = squares(a, b)
    print(f"Entrada: a={a}, b={b}\nResultado: {resultado}\n")  # Saída Esperada: 3

    print("Teste 5:")
    a, b = 100, 1000
    resultado = squares(a, b)
    print(f"Entrada: a={a}, b={b}\nResultado: {resultado}\n")  # Saída Esperada: 22

    print("Teste 6:")
    a, b = 59, 999999922
    resultado = squares(a, b)
    print(f"Entrada: a={a}, b={b}\nResultado: {resultado}\n")  # Saída Esperada: 31615

    print("Teste 7:")
    a, b = 9, 999999966
    resultado = squares(a, b)
    print(f"Entrada: a={a}, b={b}\nResultado: {resultado}\n")  # Saída Esperada: 31620

    print("Teste 8:")
    a, b = 12, 999999988
    resultado = squares(a, b)
    print(f"Entrada: a={a}, b={b}\nResultado: {resultado}\n")  # Saída Esperada: 31619

    # Loop para permitir mais testes com entrada do usuário
    while True:
        try:
            user_input = input("\nDigite os valores de 'a' e 'b' (separados por espaço) ou 'sair' para finalizar: ")
            if user_input.lower() == 'sair':
                print("Saindo...")
                break
            a, b = map(int, user_input.split())
        except ValueError:
            print("Entrada inválida. Saindo...")
            break

        resultado = squares(a, b)
        print(f"Entrada: a={a}, b={b}\nNúmero de inteiros quadrados: {resultado}")

if __name__ == "__main__":
    main()
