import math

def pythagorean_triplet():
    """ brute force a**2+b**2 = c**2. List of triplets (a, b, c)"""
    triplet_list = []
    for a in range(1, 500):
        for b in range(1, 500):
            c = int(math.sqrt((a**2 + b**2)))
            if c**2 == (a**2 + b**2):
                triplet_list.append((a, b, c))
            
    return triplet_list

def problem_solv():
    triplet_list = pythagorean_triplet()
    for a, b, c in triplet_list:
        if (a + b + c) == 1000:
        return a*b*c
        
if __name__ == "__main__":
    print(problem_solv())