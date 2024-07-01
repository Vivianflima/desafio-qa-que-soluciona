def countingValleys(path):
    altitude = 0
    vales = 0
    in_vale = False

    for step in path:
        if step == 'U':
            altitude += 1
        elif step == 'D':
            altitude -= 1

        # Entrando em um vale
        if altitude < 0 and not in_vale:
            in_vale = True

        # Saindo de um vale
        if altitude == 0 and in_vale:
            vales += 1
            in_vale = False

    return vales

# Função principal para realizar os testes
def main():
    # Testes fornecidos no desafio
    print("Teste 1:")
    path = "DDUUDDUDUUUD"
    resultado = countingValleys(path)
    print(f"Entrada: path = \"{path}\"\nResultado: {resultado}\n")  # Saída Esperada: 2

    print("Teste 2:")
    path = "UDUUUDUDDD"
    resultado = countingValleys(path)
    print(f"Entrada: path = \"{path}\"\nResultado: {resultado}\n")  # Saída Esperada: 0

    print("Teste 3:")
    path = "DUDUDUDUDUDUDU"
    resultado = countingValleys(path)
    print(f"Entrada: path = \"{path}\"\nResultado: {resultado}\n")  # Saída Esperada: 7

    print("Teste 4:")
    path = "DDUUUUDDDUUUDDDU"
    resultado = countingValleys(path)
    print(f"Entrada: path = \"{path}\"\nResultado: {resultado}\n")  # Saída Esperada: 3

    # Loop para permitir mais testes com entrada do usuário
    while True:
        path = input("\nDigite a sequência de passos (ou 'sair' para finalizar): ")
        if path.lower() == 'sair':
            print("Saindo...")
            break
        resultado = countingValleys(path)
        print(f"Número de vales percorridos: {resultado}")

if __name__ == "__main__":
    main()
