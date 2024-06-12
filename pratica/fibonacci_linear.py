def fibonacci(n: int) -> int:
    """Calcula o n-ésimo valor da sequência de Fibonacci de forma linear / iterativa."""
    
    # Verifica se n é um número válido, ou seja, não negativo
    if n < 0:
        print("n deve ser uma inteiro não negativo!")
        return None

    # Caso n seja 0, o valor da sequência de Fibonacci é 0
    if n == 0:
        return 0

    # Caso n seja 1, o valor da sequência de Fibonacci é 1
    if n == 1:
        return 1

    # Caso contrário, calcula o n-ésimo valor da sequência de Fibonacci
    a = 0  # Valor inicial da sequência de Fibonacci
    b = 1  # Segundo valor da sequência de Fibonacci
    for _ in range(2, n + 1):  # Como já temos os dois primeiros valores, começamos a partir do terceiro
        result = a + b  # Calcula o próximo valor da sequência de Fibonacci
        a = b  # Atualiza o primeiro valor
        b = result  # Atualiza o segundo valor

    # Depois que o loop terminar, o valor de result será o n-ésimo valor da sequência de Fibonacci
    return result

# Testa a função, solicitando ao usuário o valor de n
if __name__ == "__main__":
    n = int(input("Digite o valor de n: "))
    print(f"O {n}-ésimo valor da sequência de Fibonacci é {fibonacci(n)}")