import eulerlib 

def prime_only_loop(n):
    """
    Input number, returns list of prime factors (no duplicates)
    The returned list might includes composite numbers. So need to be
    filtered for primes only 
    """
    prime_list = []
    factorization_list=[]
    q = 1
    check = 0
      
    if n%2 == 0:
        factorization_list.append(2)
        n /= 2
    if n%3 == 0:
        factorization_list.append(3)
        n /= 3
    while  check < n:
        check = 6*q - 1
        if n % check == 0:
            factorization_list.append(check)
            n /= check
        check += 2
        if n % check == 0:
            factorization_list.append(check)
            n /= check
        q += 1

    #clean all composite numbers
    all_primes = eulerlib.sieve_of_eratosthenes(max(factorization_list))
    for num in factorization_list:
        if num in all_primes:
            prime_list.append(num)
    return prime_list

if __name__ == "__main__":
    print(max(prime_only_loop(600851475143)))
    print(prime_only_loop(600851475143))
