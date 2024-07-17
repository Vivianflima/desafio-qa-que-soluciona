def passwordCracker(passwords, loginAttempt):
    memo = {}
    
    def canCrack(attempt):
        if attempt in memo:
            return memo[attempt]
        if attempt == "":
            return []
        for password in passwords:
            if attempt.startswith(password):
                result = canCrack(attempt[len(password):])
                if result is not None:
                    memo[attempt] = [password] + result
                    return memo[attempt]
        memo[attempt] = None
        return None

    result = canCrack(loginAttempt)
    return " ".join(result) if result is not None else "WRONG PASSWORD"

def main():
    # Testes fornecidos no desafio
    print("Teste 1:")
    passwords = ["because", "can", "do", "must", "we", "what"]
    loginAttempt = "wedowhatwemustbecausewecan"
    resultado = passwordCracker(passwords, loginAttempt)
    print(f"Entrada: passwords={passwords}, loginAttempt={loginAttempt}\nResultado: {resultado}\n")  # Saída Esperada: "we do what we must because we can"

    print("Teste 2:")
    passwords = ["hello", "planet"]
    loginAttempt = "helloworld"
    resultado = passwordCracker(passwords, loginAttempt)
    print(f"Entrada: passwords={passwords}, loginAttempt={loginAttempt}\nResultado: {resultado}\n")  # Saída Esperada: "WRONG PASSWORD"

    print("Teste 3:")
    passwords = ["ab", "abcd", "cd"]
    loginAttempt = "abcd"
    resultado = passwordCracker(passwords, loginAttempt)
    print(f"Entrada: passwords={passwords}, loginAttempt={loginAttempt}\nResultado: {resultado}\n")  # Saída Esperada: "ab cd" ou "abcd"

    # Loop para permitir mais testes com entrada do usuário
    while True:
        try:
            passwords = input("\nDigite as senhas (separadas por espaço) ou 'sair' para finalizar: ").split()
            if 'sair' in passwords:
                print("Saindo...")
                break
            loginAttempt = input("Digite a tentativa de login: ")
        except ValueError:
            print("Entrada inválida. Saindo...")
            break

        resultado = passwordCracker(passwords, loginAttempt)
        print(f"Entrada: passwords={passwords}, loginAttempt={loginAttempt}\nResultado: {resultado}")

if __name__ == "__main__":
    main()
