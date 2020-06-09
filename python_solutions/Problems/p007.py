from eulerlib import sieve_of_eratosthenes
import time #execution time

start_time = time.time() 

n = 2000000
prime_list = sieve_of_eratosthenes(n)

if len(prime_list) >= 10001:
    print(prime_list[10000])
    print(len(prime_list))
    

print("execution time: --- %s seconds ---" % (time.time() - start_time))