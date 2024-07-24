def similarity(s):
    def common_prefix_length(s1, s2):
        count = 0
        for a, b in zip(s1, s2):
            if a == b:
                count += 1
            else:
                break
        return count

    total_similarity = 0
    for i in range(len(s)):
        total_similarity += common_prefix_length(s, s[i:])
    
    return total_similarity

def main():
    # Testes fornecidos no desafio
    print("Teste 1:")
    s = "ababaa"
    resultado = similarity(s)
    print(f"Entrada: s={s}\nResultado: {resultado}\n")  # Saída Esperada: 11

    print("Teste 2:")
    s = "aa"
    resultado = similarity(s)
    print(f"Entrada: s={s}\nResultado: {resultado}\n")  # Saída Esperada: 3

    print("Teste 3:")
    s = "abcabccba"
    resultado = similarity(s)
    print(f"Entrada: s={s}\nResultado: {resultado}\n")  # Saída Esperada: 13

    print("Teste 4:")
    s = "eabdcbbeeedbdaebdedbcbdcdeeaebbdbedbdbccbaaeababba"
    resultado = similarity(s)
    print(f"Entrada: s={s}\nResultado: {resultado}\n")  # Saída Esperada: 63

    print("Teste 5:")
    s = "bcdedeccaabdaebdddaeedabedccdddccbbaaadcbbabccbaadbbbeddecacddbababbabadcbbbacecdaee"
    resultado = similarity(s)
    print(f"Entrada: s={s}\nResultado: {resultado}\n")  # Saída Esperada: 105

    print("Teste 6:")
    s = "aeccbdaadbcebddbadbaedeceedbcdaaadcbdebecaddedebccdbadaeed"
    resultado = similarity(s)
    print(f"Entrada: s={s}\nResultado: {resultado}\n")  # Saída Esperada: 70

    # Loop para permitir mais testes com entrada do usuário
    while True:
        try:
            s = input("\nDigite a string para calcular a similaridade com seus sufixos ou 'sair' para finalizar: ")
            if s.lower() == 'sair':
                print("Saindo...")
                break
        except ValueError:
            print("Entrada inválida. Saindo...")
            break

        resultado = similarity(s)
        print(f"Entrada: s={s}\nResultado: {resultado}")

if __name__ == "__main__":
    main()
