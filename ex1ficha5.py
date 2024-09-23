# Função para ler um valor inteiro positivo
def ler_valor_positivo():
    while True:
        try:
            valor = int(input("Digite um valor inteiro positivo: "))
            if valor > 0:
                return valor
            else:
                print("O número deve ser positivo. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")

# Função para imprimir asteriscos
def imprimir_asteriscos(valor):
    print('*' * valor)

# Execução do programa
def main():
    valor = ler_valor_positivo()
    imprimir_asteriscos(valor)

# Chamando a função principal
if __name__ == "__main__":
    main()