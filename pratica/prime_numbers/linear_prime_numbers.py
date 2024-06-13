class PrimeNumbers:
    """Classe que calcula os números primos até um determinado valor n"""

    def __init__(self):
        self.__prime_numbers = []  # Lista que armazenará os números primos

    def is_prime(self, k: int) -> bool:
        """Método que verifica se um número k é primo."""

        if k <= 2:
            return k == 2  # O único número primo menor ou igual a 2 é 2

        # Verifica se k é divisível por algum número entre 2 e k - 1, isto é,
        # se o resto da divisão de k por i é igual a 0 para algum i entre 2 e k - 1
        for i in range(2, k):
            if k % i == 0:
                return False  # Se k for divisível por algum número entre 2 e k - 1, então k não é primo
        return True  # Caso contrário, k é primo

    def calculate_prime_numbers(self, n: int) -> None:
        """Método que encontra todos os números primos de 2 até um determinado valor n.
           Cada um desses números é armazenado na lista __prime_numbers"""

        self.clear_prime_numbers()  # Limpa a lista de números primos

        # Se n for 0 ou 1, não existem números primos antecedentes a ele
        # então a lista de números primos é vazia
        if n == 0 or n == 1:
            self.__prime_numbers = []
            return

        # Se n for 2, o único número primo é 2, então a lista de números primos é [2]
        if n == 2:
            self.__prime_numbers = [2]
            return

        # Caso contrário, encontra todos os números primos de 2 até n
        # usando o método is_prime e os coloca na lista __prime_numbers
        for i in range(2, n + 1):
            if self.is_prime(i):
                self.__prime_numbers.append(i)
    
    # Método especial para representação em string da classe
    def __str__(self) -> None:
        return f"Os números primos até n são: {self.get_prime_numbers()}"

    # Método que retorna a lista de números primos,
    # já que a lista é um atributo privado da classe
    def get_prime_numbers(self) -> list[int]:
        return self.__prime_numbers

    def clear_prime_numbers(self) -> None:
        """Método que limpa a lista de números primos."""
        self.__prime_numbers = []

# Testa o programa, solicitando ao usuário o valor de n
# até que o usuário digite 'q' para sair do programa
if __name__ == "__main__":
    prime_numbers = PrimeNumbers()
    while True:
        n = input("Digite o valor de n ou 'q' para sair do programa: ")
        if n.lower() == 'q':
            break
        if not n.isdigit():
            print("n deve ser um número inteiro não negativo!")
            continue
        n = int(n)
        prime_numbers.calculate_prime_numbers(n)
        print(prime_numbers)

    print("Até a próxima!")
