# 2.1 Helper and algorithmic functions 
## 2.1  Greatest common divider (GCD)
### Call 
`gcd(a, b)`
Finds greatest common divider for a and b, using Euclidean recursion algorithm
- The main idea is that gcd is in the division remainder t1=a%b. Then a, b and t1 will have the same gcd, so we find t2=b%t1 etc utill tn=0
### Other 
- GCD(x1, x2, x3, ...,xn) = GCD(xn, GCD(x(n-1), (GCD(..., GCD(x1,x2))...))) 
- Lowest common multiple: LCD(x, y) = x * y / GCD(x, y)

## 2.2 Sieve of Eratosthenes

[wikipedia](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)
- Helps to find all prime numbers up to N (so it cannot find 10001th prime number directly)
- It creats an all-True boolian array of size N. Then goes though multiples of prime numbers and change correspondin indexes to False. Return all True indexes. 
- Complexity O(n log log n)
### Call
`sieve_of_eratosthenes(n)`
Takes intager n - the limit (>1). Returns all prime numbers up to the limit (n) as a list
### Peudocode 
```
Input: an integer n > 1.

 Let A be an array of Boolean values, indexed by integers 2 to n,
 initially all set to true.
 
 for i = 2, 3, 4, ..., not exceeding √n:
   if A[i] is true:
     for j = i^2, i^2+i, i^2+2i, i^2+3i, ..., not exceeding n:
       A[j] := false.
 
 Output: all i such that A[i] is true.
 ```
**Common optimizations:**
- Go up to *√n*, as it is the max posible divider (exept *n* itself). 
- Prime multiples start at *i^2*, because all numbers before are either prime or *i* multiples of previous numbers  

## 2.3 All integer divisors finder
- Complexity O(sqrt(n))
### Call
`find_divisors(n)`
Takes an integer (n). Returns a list of all integer divisors for a given number  

**Common optimizations:**
- Go up to *√n*, as it is the max posible divider (exept *n* itself). 
- If i is divisor (n%i == 0), then n/i is also a divisor

## 2.4  Binomial coefficient finder
### Call
`binomial_coefficient(n, k)`  
Take n (fixed subset) and k (an (unordered) subset of k). Returns the binominal coefficient
### Other
- It can be used to find all elements of Pascal triangle: n(starting from 0)  - row, k - element (starting from 0) 
- Central binomial coefficients (the middle coefficint in the rows where odd number of elements) can be used to 
find number of ways to get from one corner of lattice to another (only in diagonal, NxN square). See [Lattice path](https://www.robertdickau.com/lattices.html)

## 2.5 Execution time decorator
## Call
`@timer`  
Shows wall-clock time of exectuoin 

## 2.6 Squaring exponentiation: a^n
- Complexity: O(log n)
- Calculated recursively
## Call
`sqr_pow(a, n)`

## 2.7 Prime factors of a number
### Call
`prime_factors_only(n)`
Takes an advantage of the fact that all prime numbers satisfy n=6*q +- 1 (although some factor numbers satisfy too, so they need to filtered using sieve_of_eratosthenes)
- Worst complexity O(n*sqrt n) for the case when n has (1, n) as the divisors