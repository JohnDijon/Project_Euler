import time
import functools

def collatz_sequence_len(n):
    """
    Reqursion function.
    Takes an int and returns next Collatz sequence int
    If sequnce 
    """
    if n == 1:
        return 1
    elif n%2 == 0:
        x = n/2
    else:
        x = 3*n + 1
    return collatz_sequence_len(x) + 1

@functools.lru_cache(maxsize=None) #cache results using cache decorator
def problem_solve(limit):
    start = time.time()  #checking excecution time                                
    best_len_num = max(range(1, limit), key = collatz_sequence_len)
    end = time.time()    #checking excecution time
    print('Excecutiion time: ', (end - start), 's')
    return best_len_num

if __name__ == "__main__":
    print(problem_solve(1000_000))
    print(problem_solve.cache_info())
    #seems like for this proble cache doesn't speed it up, as it shows no hits