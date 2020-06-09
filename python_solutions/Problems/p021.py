import eulerlib

@eulerlib.timer
def problem_solve(n):
    """ 
    Evaluates the sum of all the amicable numbers under n
    Complexity is approximately O(n*sqrt n)
    """
    amicable_list = []
    for x in range(1, n+1):
        y = sum(eulerlib.find_divisors(x)[:-1])
        if y > x:  
            if x == sum(eulerlib.find_divisors(y)[:-1]) and x != y:
                amicable_list.append(x)
                amicable_list.append(y)
    return sum(amicable_list)        
    
if __name__ == "__main__":
    print(problem_solve(10000))
