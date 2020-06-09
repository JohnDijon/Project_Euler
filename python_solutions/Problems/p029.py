import eulerlib

# solution using sqt_pow - brute force 
# x2 for loops
@eulerlib.timer
#def problem_solution():
#    num_set = set()
#    for a in range(2, 1001):
#        for b in range(2, 1001):
#            num_set.add(eulerlib.sqr_pow(a, b))
#    return len(num_set)

def problem_silution():
    for a in range(1000_000):
        eulerlib.sqr_pow(5, a)



@eulerlib.timer
#def compute():
#	seen = set(a**b for a in range(2, 1001) for b in range(2, 1001))
#	return str(len(seen))

def compute():
    for a in range(1000_000):
        5**a

if __name__ == "__main__":
    print(problem_solution())

if __name__ == "__main__":
	print(compute())
    
