def timeInWords(h, m):
    # Dicionário para mapear números para palavras
    numbers = {
        0: "o' clock", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
        6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven",
        12: "twelve", 13: "thirteen", 14: "fourteen", 15: "quarter", 16: "sixteen",
        17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty",
        21: "twenty one", 22: "twenty two", 23: "twenty three", 24: "twenty four",
        25: "twenty five", 26: "twenty six", 27: "twenty seven", 28: "twenty eight",
        29: "twenty nine", 30: "half"
    }
    
    if m == 0:
        return f"{numbers[h]} {numbers[0]}"
    elif m == 1:
        return f"one minute past {numbers[h]}"
    elif m == 15 or m == 30:
        return f"{numbers[m]} past {numbers[h]}"
    elif m == 45:
        return f"{numbers[15]} to {numbers[h + 1 if h != 12 else 1]}"
    elif 1 < m < 30:
        return f"{numbers[m]} minutes past {numbers[h]}"
    else:
        return f"{numbers[60 - m]} minutes to {numbers[h + 1 if h != 12 else 1]}"

# Função principal para realizar os testes
def main():
    # Testes fornecidos no desafio
    test_cases = [
        (5, 0, "five o' clock"),
        (5, 1, "one minute past five"),
        (5, 10, "ten minutes past five"),
        (5, 15, "quarter past five"),
        (5, 28, "twenty eight minutes past five"),
        (5, 30, "half past five"),
        (5, 40, "twenty minutes to six"),
        (5, 45, "quarter to six"),
        (5, 47, "thirteen minutes to six")
    ]
    
    for h, m, expected in test_cases:
        result = timeInWords(h, m)
        assert result == expected, f"Erro: {h}:{m} -> {result}, Esperado: {expected}"
        print(f"Entrada: h={h}, m={m}\nResultado: {result}\n")

    # Loop para permitir mais testes com entrada do usuário
    while True:
        try:
            h = int(input("Digite a hora (h) ou 'sair' para finalizar: "))
            if h == 'sair':
                print("Saindo...")
                break
            m = int(input("Digite os minutos (m): "))
        except ValueError:
            print("Entrada inválida. Saindo...")
            break

        resultado = timeInWords(h, m)
        print(f"Entrada: h={h}, m={m}\nResultado: {resultado}")

if __name__ == "__main__":
    main()
