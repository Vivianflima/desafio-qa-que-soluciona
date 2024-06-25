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
            n = int(input("\nDigite o tamanho da escadaria que você deseja construir (ou 0 para sair): "))
            if n == 0:
                print("Saindo...")
                break
            escadaria(n)
        except ValueError:
            print("Por favor, insira um número inteiro válido.")

if __name__ == "__main__":
    main()
