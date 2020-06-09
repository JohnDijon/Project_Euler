import numpy as np
import math 
import time 

def gcd(a, b):
    '''
    Euclidean algorithm to find greatest common divider (GCD) 
    refer to section 2.1 documentation
    '''
    if a < b:
        a, b = b, a
    if (b == 0):
        return a
    else:
        return gcd(b, a%b)

def sieve_of_eratosthenes(n):
    """
    Takes intager n - the limit (>1).
    Returns all prime numbers up to the limit (n) as a list
    
    refer to section 2.2 documentation
    """
    #initiates an arry
    if type(n) != int:
        raise TypeError('The input must be an integer >1')
    else:
        sieve = np.full(n+1, True)
    
    #sieve procedure
    sieve[0], sieve[1] = False, False
    for i in range(2, math.ceil(math.sqrt(n))+1):
        if sieve[i]:
            j = i**2
            while j<=n:
                sieve[j] = False
                j += i
    
    #unwrap the nubers
    prime_num = []
    for i in range(n+1):
        if sieve[i]:
            prime_num.append(i)
    
    return prime_num

def find_divisors(n):
    """ 
    Returns a list of all integer divisors for a given integer 
    refer to section 2.3 documentation
    """
    divisors_list = []
    for i in range(1, math.ceil(math.sqrt(n))):
        if n%i == 0:
            divisors_list.append(i)
            divisors_list.append(int(n/i))
    return sorted(divisors_list)

def binomial_coefficient(n, k):
    """
    Takes m, k. "From fixed n takes k". Return binomial_coefficient
    refer to section 2.4 documentation
    """
    assert 0 <= k <= n, "make sure that 0 <= k <= n"
    return  int(math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))

def timer(funct):
    """
    simple decorator for execution time 
    refer to section 2.5 documentation
    """
    def wrapper(*args, **kw):
        start = time.time()
        result = funct(*args, **kw)
        end = time.time()
        print("Wall-clock time of excetuon: ", end-start, "s")
        return result
    return wrapper

def sqr_pow(a, n):
    """
    Squaring exponentiation: a^n. Takes a, n.
    refer to section 2.6 documentation
    """
    assert (n>=0) &(type(n) == int), "the exponent(n) must be positive integer"
    if not n:
        return 1
    half_res = sqr_pow(a, int(n/2))
    if not (n%2):
        return int(half_res*half_res)
    else: 
        return int(a*half_res*half_res)
    
def prime_factors_only(n):
    """
    Input number, returns list of prime factors (no duplicates)
    The returned list might includes composite numbers. So need to be
    filtered for primes only 
    refer to section 2.7
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
    all_primes = sieve_of_eratosthenes(max(factorization_list))
    for num in factorization_list:
        if num in all_primes:
            prime_list.append(num)
    return prime_list
##############################################################################
######################### Other ############################################## 
##############################################################################


class simple_cache():
    """
    simple class for cache decorators
    """
    def __init__(self, funct):
        self.funct = funct 
        self.cache = {}
        
    def __call__(self, *args):
        if args in self.cache:
            return self.cache[args]
        else:
            n = self.funct(args)
            self.cache[args] = n
            return n
        
    