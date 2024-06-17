class PrimeNumbers:
    """Classe que calcula os números primos até um determinado valor n"""
    def __init__(self) -> None:
        self.__prime_numbers = []

    def is_prime(self, k: int) -> bool:
        """Método que verifica se um número k é primo."""

        if k <= 1:
            return False  # Nenhum número menor ou igual a 1 é primo

        if k == 2:
            return True  # O único número primo par é 2

        if k % 2 == 0:
            return False  # Nenhum número par diferente de 2 é primo

        # Utilizando o método do Trial Division para verificar se k é primo
        # Só precisamos verificar divisores até a raiz quadrada de k
        max_divisor = int(k ** 0.5) + 1

        # Começamos a verificar divisores a partir de 3, pulando os números pares
        for i in range(3, max_divisor, 2):
            if k % i == 0:
                return False  # Se k for divisível por algum número entre 2 e k - 1, então k não é primo
        return True  # Caso contrário, k é primo

    def calculate_prime_numbers(self, n: int) -> None:

        # Caso base, não existe número primo menor igual a 1
        if n <= 1:
            return
        
        # Caso geral. Se n é primo, é adicionado ao início da lista
        if self.is_prime(n):
            self.__prime_numbers.insert(0, n)

        # Chama a função recursivamente, para o número anterior
        self.calculate_prime_numbers(n - 1)

    # Função especial para representação da classe em string
    def __str__(self) -> None:
        return f"Os números primos até n são: {self.get_prime_numbers()}"

    # Função que retorna a lista de primos gerada e limpa a lista gerada
    def get_prime_numbers(self) -> list[int]:
        prime_numbers_str = self.__prime_numbers
        self.clear_prime_numbers()
        return prime_numbers_str

    # Função que limpa a lista, para que não reste elementos da utilização anterior
    def clear_prime_numbers(self) -> None:
        self.__prime_numbers = []

# Testa o funcionamento do programa solicitando um valor de n ao usuário
# até que ele digite 'q' para sair do programa
if __name__ == "__main__":
    prime_numbers = PrimeNumbers()
    while True:
        n = input("Digite um número inteiro não negativo ou 'q' para sair do programa: ")

        if n.lower() == 'q':
            break

        if not n.isdigit():
            print("Digite um número inteiro não negativo.")
            continue

        n = int(n)
        prime_numbers.calculate_prime_numbers(n)
        print(prime_numbers)

    print("Até a próxima!")