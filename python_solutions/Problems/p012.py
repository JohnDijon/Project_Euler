from eulerlib import find_divisors

def problem_solve(num_divisors, limit):
    triangle = 0
    for i in range(1, limit):
        triangle += i
        if len(find_divisors(triangle)) > num_divisors:
            return triangle
        
if __name__ == "__main__":
    limit = 60000
    num_divisors = 500
    print(problem_solve(num_divisors, limit))
