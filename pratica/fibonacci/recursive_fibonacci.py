def fibonacci(n: int) -> int:
    """Calcula o n-ésimo valor da sequência de Fibonacci de forma recursiva."""

    # Verifica se n é um número válido, ou seja, não negativo
    if n < 0:
        print("n deve ser um número não negativo!")
        return None

    # Primeira condição de parada da recursão
    if n == 0:
        return 0

    # Segunda condição de parada da recursão
    elif n == 1:
        return 1

    # Caso geral
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Testa a função, solicitando ao usuário o valor de n
# até que o usuário digite 'q' para sair do programa
if __name__ == "__main__":
    while True:
        n = input("Digite o valor de n ou digite 'q' para sair do programa: ")
        if n.lower() == 'q':
            break
        if not n.isdigit():
            print("n deve ser um número inteiro não negativo!")
            continue
        n = int(n)
        print(f"O {n}-ésimo valor da sequência de Fibonacci é {fibonacci(n)}")
    print("Até a próxima!")