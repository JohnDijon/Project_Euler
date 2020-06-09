import eulerlib
import math

def problem_solve():
    """
    The number of ways is equal to central binominal coefficient (Pascal's triangle)
    where n (row) equals to the total number of squares (in 20x20: 40 squares)
    Num. of elements in n row equals to n+1, starting from 0: [0, n]
    see more: https://www.robertdickau.com/lattices.html
    """
    square_num = 40
    central_el = int(math.ceil(square_num/2))
    ans = eulerlib.binomial_coefficient(40, central_el)
    return ans

if __name__ == "__main__":
    print(problem_solve())