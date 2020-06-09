from eulerlib import sieve_of_eratosthenes

def problem_solve():
    n = 2_000_000
    list_of_primes = sieve_of_eratosthenes(n)
    return sum(list_of_primes)

if __name__ == "__main__":
    print(problem_solve())