def problem_solve(n):
    ans = 1
    for i in range(1, n+1):
        ans *= i
    ans_sum = 0
    for num in str(ans):
        ans_sum += int(num)
    print(ans_sum)

if __name__ == "__main__":
    problem_solve(100)