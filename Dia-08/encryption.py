import math

def encryption(s):
    # Remove spaces from the string
    s = s.replace(" ", "")
    
    # Length of the string after removing spaces
    L = len(s)
    
    # Calculate the number of rows and columns
    rows = math.floor(math.sqrt(L))
    cols = math.ceil(math.sqrt(L))
    
    # If the number of rows * columns is less than the length of the string, increase rows
    if rows * cols < L:
        rows += 1
    
    # Create the encrypted message
    encrypted_message = []
    for col in range(cols):
        encrypted_message.append("".join([s[row * cols + col] for row in range(rows) if row * cols + col < L]))
    
    # Join the encrypted message with spaces
    return " ".join(encrypted_message)

def main():
    # Testes fornecidos no desafio
    print("Teste 1:")
    s = "haveaniceday"
    resultado = encryption(s)
    print(f"Entrada: s={s}\nResultado: {resultado}\n")  # Saída Esperada: "hae and via ecy"

    print("Teste 2:")
    s = "feedthedog"
    resultado = encryption(s)
    print(f"Entrada: s={s}\nResultado: {resultado}\n")  # Saída Esperada: "fto ehg ee dd"

    print("Teste 3:")
    s = "chillout"
    resultado = encryption(s)
    print(f"Entrada: s={s}\nResultado: {resultado}\n")  # Saída Esperada: "clu hlt io"

    print("Teste 4:")
    s = "iuo"
    resultado = encryption(s)
    print(f"Entrada: s={s}\nResultado: {resultado}\n")  # Saída Esperada: "io u"

    print("Teste 5:")
    s = "wclwfoznbmyycxvaxagjhtexdkwjqhlojykopldsxesbbnezqmixfpujbssrbfhlgubvfhpfliimvmnny"
    resultado = encryption(s)
    print(f"Entrada: s={s}\nResultado: {resultado}\n")  # Saída Esperada: "wmgjpnull cyjqlejgi lyhhdzbui wctlsqsbm fxeoxmsvv ovxjeirfm zadysxbhn nxkkbffpn bawobphfy"

    # Loop para permitir mais testes com entrada do usuário
    while True:
        try:
            s = input("\nDigite a string para criptografar ou 'sair' para finalizar: ")
            if s.lower() == 'sair':
                print("Saindo...")
                break
        except ValueError:
            print("Entrada inválida. Saindo...")
            break

        resultado = encryption(s)
        print(f"Entrada: s={s}\nResultado: {resultado}")

if __name__ == "__main__":
    main()
