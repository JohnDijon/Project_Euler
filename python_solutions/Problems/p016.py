import eulerlib
#as 2**1000 is a fast computatuion, no need in optimization
#moreover 2**1000 buind-in method is already fast 
#here is coparising of loop multiplication, build-in and square exponentiation

@eulerlib.timer
def problem_solve1():
    ans = str(2**1000_000)
    sum_ans = 0
    for char in ans:
        sum_ans += int(char)   
    return sum_ans

@eulerlib.timer
def problem_solve2():
    ans = 1
    for _ in range(1, 1000_001):
        ans *= 2
    sum_ans = 0
    for char in str(ans):
        sum_ans += int(char)   
    return sum_ans

@eulerlib.timer
def problem_solve3():
    ans = eulerlib.sqr_pow(2, 1000_000)
    sum_ans = 0
    for char in str(ans):
        sum_ans += int(char)   
    return sum_ans

if __name__ == "__main__":
    print("Answer (in-build): ", problem_solve1())
    print("Answer (loop): ", problem_solve2())
    print("Answer (square exponentiation): ", problem_solve3())
    